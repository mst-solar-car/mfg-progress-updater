import team_config
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Open the task list output file
output = open('email_lists.py', 'w')
 
# Open the tasks spreadsheet file
file = client.open("SCT Tasks")

# Define each spreadsheet
mech_sheet = file.worksheet('Mechanical')
elec_sheet = file.worksheet('Electrical')
sheets = [mech_sheet, elec_sheet]

# Define each spreadsheet's name
sheet_names = {mech_sheet : 'mech', elec_sheet : 'elec'}

# Sanity check
assert(len(sheets) == len(sheet_names))

# Dictionary mapping team member name to list of uncompleted tasks
member_tasks = {}

for sheet in sheets:
    # Extract data (list of row dictionaries) from sheet, where each row is a task
    list_of_row_dicts = sheet.get_all_records()

    for row_dict in list_of_row_dicts:
        # Don't remind people about completed tasks
        if row_dict['Completed? (for bot)'] != 'Yes':
            # Get assignee(s) for current task
            assignees = row_dict["Assignee"].split(',')

            # Strip away unwanted assignees, remove spaces in names
            cleaned_assignees = [name.strip() for name in assignees if name != '' and name != 'NA']

            for assignee in cleaned_assignees: 
                task_entry = [row_dict['Sub Tasks'], row_dict['Completion Date'], row_dict['Road Blocks'], row_dict['Notes']]

                # Assign the task to its assignee
                if assignee in member_tasks:
                    member_tasks[assignee].append(task_entry)
                else:
                    member_tasks[assignee] = [task_entry]


# Dictionary mapping email to list of task messages
email_tasks = {}

# Populate notification emails to send to each member
for member in member_tasks:
    # If we have an email for this member
    if member in team_config.emails:
        email = team_config.emails[member]
    else:
        email = team_config.emails['default']

    for task_lst in member_tasks[member]:
        message = 'Task: ' + task_lst[0] + '\n' + 'Completion Date: ' + str(task_lst[1]) + '\n' + 'Road Blocks: ' + task_lst[2] + '\n' + 'Notes: ' + task_lst[3] + '\n'

        # If we have a message already written for this email
        if email in email_tasks:
            email_tasks[email].append(message)
        else:
            email_tasks[email] = [message]

output.write('tasks = ' + str(email_tasks) + '\n')