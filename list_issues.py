# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# It is a simple example of how to use the Jira REST API to list all projects in a Jira instance.
# It uses HTTP Basic Authentication with an API token.
# Make sure to replace the URL, email, and API token with your own values.
# The API token can be generated from your Atlassian account settings.
# For more information, see the Jira REST API documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("email@example.com", "<api_token>")
# Replace with your email and API token from Atlassian account

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

for project in output:
    print(project['name'])
