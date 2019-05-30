from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Admin SDK Directory API
SCOPES = ('https://www.googleapis.com/auth/admin.directory.group.readonly ' +
          'https://www.googleapis.com/auth/admin.directory.group.member.readonly' +
          'https://www.googleapis.com/auth/admin.directory.user.readonly')
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('admin', 'directory_v1', http=creds.authorize(Http()))

# Initialize the page iterators
group_nextPageToken = None
user_nextPageToken = None

# Call the Admin SDK Directory API
while True:
    group_results = service.groups().list(customer='my_customer', maxResults='100', orderBy='email', pageToken=group_nextPageToken).execute()
    groups = group_results.get('groups', [])
    group_nextPageToken = group_results.get('nextPageToken', None)

    if not groups:
        print('No groups in the domain.')
    else:
        for group in groups:
       	# Search the group members for a non-matching email
            while True:
                user_results = service.members().list(groupKey=group['email'], maxResults='100', pageToken=user_nextPageToken).execute()
                users = user_results.get('members', [])
                user_nextPageToken = user_results.get('nextPageToken', None)

                for user in users:
                    if ("@tradeshift.com" not in user['email'] and 
                        "@tradeshift.zendesk.com" not in user['email'] and
                        "@tradeshift.pagerduty.com" not in user['email']):
                        print('{0}: {1}'.format(group['email'], user['email']))
           
                if user_nextPageToken is None:
                   break

    if group_nextPageToken is None:
        break