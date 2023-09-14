# Project Background
## Goal: 
To easily invite multiple people to a Mist Org
## Language: 
Python

# How to use

## Info Needed: 
Admin API token, Mist Org ID, sample_invites.csv (contacts info)

## Files:
- admin_features.py\
Where admin API token and Mist Org ID needs to be put in, host features get_admins, invite_admin and revoke_admin
- main.py\
Main logic of this project, including, read entries from 'sample_invites.csv' file as List, call invite_admin feature for each entry from the List. Contains optional revoke_admin call which has been commented out
- sample_invites.csv\
Spreadsheet about contacts info in below format

|first_name |last_name |email |role | scope |       
|-----------|----------|------|-----|-------|
|Bob |Green |bob.green@email.com |read |org |

- requirement.txt\
pip modules that needs to be installed for smooth run

# Output
Successfully invited/revoked admins will be shown at terminal.\
Otherwise error message will be shown.
                                 
