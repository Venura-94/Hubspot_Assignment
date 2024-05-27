import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API endpoint and headers
headers = {
    "Authorization": f"Bearer {os.getenv('HUBSPOT_API_KEY')}",
    "Content-Type": "application/json"
}

def extract_tickets():
    endpoint = "https://api.hubapi.com/crm/v3/objects/tickets/search"
    params = {
        "filterGroups": [
            {
                "filters": [
                    {
                        "propertyName": "hs_ticket_priority",
                        "operator": "EQ",
                        "value": "HIGH"
                    }
                ]
            }
        ],
        "properties": [
            "hs_object_id",
            "subject",
            "content",
            "hs_ticket_category",
            "hs_ticket_priority"
        ],
    }

    response = requests.post(endpoint, headers=headers, json=params)
    if response.status_code != 200:
        raise Exception(f"Request failed with status code: {response.status_code}")
    
    data = response.json()
    ticket_list = []
    for obj in data['results']:
        extracted_obj = {
            "ticket_id": obj['properties']['hs_object_id'],
            "subject": obj['properties']['subject'],
            "content": obj['properties']['content'],
            "ticket_category": obj['properties']['hs_ticket_category'],
            "ticket_priority": obj['properties']['hs_ticket_priority']
        }
        ticket_list.append(extracted_obj)

    return pd.DataFrame(ticket_list)

def extract_emails():
    endpoint = "https://api.hubapi.com/crm/v3/objects/emails/search"
    params = {
        "filterGroups": [
            {
            "filters": [
                {
                "propertyName": "hs_createdate",
                "operator": "BETWEEN",
                "value": "2024-05-19T07:00:17.801Z",
                "highValue" : "2024-05-20T08:00:17.801Z"
                }
            ]
            }
        ],
        "properties": [
                "hs_object_id",
                "hs_createdate",
                "hs_email_subject",
                "hs_email_text",
                "hs_email_status"
            ]
        }
    
    response = requests.post(endpoint, headers=headers, json=params)
    if response.status_code != 200:
        raise Exception(f"Request failed with status code: {response.status_code}")
    
    data = response.json()
    email_list = []
    for obj in data['results']:
        extracted_obj = {
            "create_date": obj['properties']['hs_createdate'],
            "email_id": obj['properties']['hs_object_id'],
            "email_subject": obj['properties']['hs_email_subject'],
            "email_text": obj['properties']['hs_email_text'],
            "email_status": obj['properties']['hs_email_status'],
        }
        email_list.append(extracted_obj)

    return pd.DataFrame(email_list)

def export_data():
    ticket_df = extract_tickets()
    email_df = extract_emails()

    with pd.ExcelWriter('visualization.xlsx') as writer:
        ticket_df.to_excel(writer, sheet_name='tickets', index=False)
        email_df.to_excel(writer, sheet_name='emails', index=False)

    return "Data written to visualization.xlsx"
