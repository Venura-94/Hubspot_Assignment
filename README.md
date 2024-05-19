# Problem and Solution Break Down 
## Step 1 - First created the Python 3.8 environment with the dependencies 
![image](https://github.com/Venura-94/Hubspot_Assignment/assets/137409412/998df2c6-c5c8-41e2-b09a-db5bec397c43)
## Step 2 - Then created my personal CRM using Hubspot
![image](https://github.com/Venura-94/Hubspot_Assignment/assets/137409412/a2c17ebb-a46b-4c43-84f5-33a9241f90d5)
Step -3 - Check for the endpoints to interact with in order to fetch the data from emails and tickets assigned.
### 1.	Emails
Engagements | Email (hubspot.com) 
First use the basic get method to list what is returned via the properties with below endpoint
![image](https://github.com/Venura-94/Hubspot_Assignment/assets/137409412/c7ee8036-3004-4248-a559-20e20c35114f)
Then use post method with search endpoint and filtered the specific date range of emails and send query parameters to retrieve data in Json format.
![image](https://github.com/Venura-94/Hubspot_Assignment/assets/137409412/53f71d3d-7198-4932-8b76-adbcdfe3bfff)
### 2.	Tickets
CRM API | Tickets (hubspot.com)
Like above (in emails), first used get method with below basic endpoint to see what’s returned. 
![image](https://github.com/Venura-94/Hubspot_Assignment/assets/137409412/97cb8c12-1ff2-43ea-9edd-b31ead8f8ad3)
Then use post method with search endpoint and filtered the high priority tickets and send query parameters to retrieve data in Json format.
![image](https://github.com/Venura-94/Hubspot_Assignment/assets/137409412/6d7e3fda-6037-4d00-9e52-048a15b853dd)
### Step - 4 – Created private app and get API token by selecting the necessary objects mentioned in “Standard scopes” in each end point according to documentation.
![image](https://github.com/Venura-94/Hubspot_Assignment/assets/137409412/abbe4f47-06b7-4cc7-9e06-8871b7e0cc68)
### Step 5 - Verified above mentioned endpoints using Postman
![image](https://github.com/Venura-94/Hubspot_Assignment/assets/137409412/c680261b-d96f-45f7-9a4a-f55994b252fb)
### Step -6 - Define Python Script to cover the objectives mentioned.
1.	Load Environment variables – dotenv (.env)
2.	Header configurations - HTTP headers for API request including authorization token
3.	Function to extract and transform data into readable format 
extract_tickets ()
•	Sends a POST request to the HubSpot tickets API endpoint. 
•	Filters tickets with high priority and extracts properties such as hs_object_id, subject, content, hs_ticket_category, and hs_ticket_priority.
•	Converts the extracted ticket data into a Pandas Data Frame. 
extract_emails()
•	Sends a POST request to the HubSpot emails API endpoint. 
•	Filters emails created within a specific time range and extracts properties such as hs_object_id, hs_createdate.
•	Converts the extracted email data into a Pandas Data Frame.
4.	Load in to CSV
Visualization.xlsx










