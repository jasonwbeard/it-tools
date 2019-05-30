from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = ('https://www.googleapis.com/auth/apps.groups.settings ' +
          'https://www.googleapis.com/auth/admin.directory.group.readonly')

# Build the connections for 1) Admin SDK Directory API and 2) Groups Settings API
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
groups_service = build('admin', 'directory_v1', http=creds.authorize(Http()))
settings_service = build('groupssettings', 'v1', http=creds.authorize(Http()))

# Initialize the page iterators
group_nextPageToken = None
user_nextPageToken = None

# Iterate over each group
while True:
    group_results = groups_service.groups().list(customer='my_customer', maxResults='100', orderBy='email', pageToken=group_nextPageToken).execute()
    groups = group_results.get('groups', [])
    group_nextPageToken = group_results.get('nextPageToken', None)

    if not groups:
        print('No groups in the domain.')
    else:
        for group in groups:
            # Get the posting setting for a group
            settings = settings_service.groups()
            setting = settings.get(groupUniqueId=(group.get('email'))).execute()

            if setting.get('whoCanPostMessage') == "ANYONE_CAN_POST":
                print (group.get('email') + ": " + setting.get('whoCanPostMessage'))

    if group_nextPageToken is None:
        break