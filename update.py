import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
# Create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
 
# Open the tasks spreadsheet file
file = client.open("SCT Tasks")

'''
Mechanical sheet processing
'''
mech_sheet = file.sheet1
 
# Extract and print the sheet dictionaries
list_of_row_dicts = mech_sheet.get_all_records()
print(list_of_row_dicts)
