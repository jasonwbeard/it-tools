from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Admin SDK Directory API
SCOPES = 'https://www.googleapis.com/auth/admin.directory.user'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('admin', 'directory_v1', http=creds.authorize(Http()))

# Initialize the page iterator
nextPageToken = None

# Call the Admin SDK Directory API
while True:
	results = service.users().list(customer='my_customer', maxResults='100',
	                               orderBy='email', pageToken=nextPageToken).execute()
	users = results.get('users', [])
	nextPageToken = results.get('nextPageToken', None)

	if not users:
	    print('No users in the domain.')
	else:
	    for user in users:
	    	if ("2015" in user['creationTime'] or
	    		"2014" in user['creationTime'] or
	    		"2013" in user['creationTime'] or
	    		"2012" in user['creationTime'] or
	    		"2011" in user['creationTime'] or
	    		"2010" in user['creationTime'] or
	    		"2009" in user['creationTime']):
	        		print('{0} ({1}) ({2})'.format(user['primaryEmail'], user['name']['fullName'], user['creationTime']))
	
	if nextPageToken is None:
		break