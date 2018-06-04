# Manufacturing Progress Updater

A script that scrapes the Solar Car Team's task lists and sends out reminders to team members.
This helps keep people accountable for the work they do.

## Overview

This project uses the Google Drive API to connect to the S&T Solar Car Team's ASC 2018 task lists. 
It then scrapes the task lists, matches up names to emails, and sends each team member the tasks they still need to complete.

## *Secret* File Formats

There are a few *secret* files used by the scripts.

The first is `client_secret.json` which contains the API information for the application. Contact [William Lorey](mailto:wwlorey@gmail.com) for more information about this file.

The others are configuration files. `team_config.py` contains a dictionary called `emails` that maps string names (found in the task lists) to string emails.
`email_config.py` contains configuration information for the bot email account, such as the email address, password, etc.

## Usage

**Note**: Python 2.7 or greater is required

Run the following commands to first generate the emails and their reminder messages, then to send the emails out.

```
python gen_emails.py
python send_emails.py
```
