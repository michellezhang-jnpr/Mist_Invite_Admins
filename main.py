import csv
import sys
import pprint
import requests
from admin_features import *

# Customized data

filename = "sample_invites.csv"  # file name, assume csv file under current directory

# Initialization

pp = pprint.PrettyPrinter(indent=4)

invitee_list = []


# Ensure variables are defined
if mist_api_token == "" or org_id == "":
    print("Missing variables:")
    print("mist_api_token={}".format(mist_api_token))
    print("org_id={}".format(org_id))

    sys.exit(1)

# Read from local csv file
with open(filename, "r", encoding="utf-8-sig") as data:
    for line in csv.DictReader(data):
        invitee_list.append(line)


# Create session
session = requests.Session()

# loop invitee_list and send invitation
for invitee in invitee_list:
    invitee["privileges"] = [{"scope": invitee["scope"], "role": invitee["role"]}]
    del invitee["scope"]
    del invitee["role"]
    invite_admin(session, invitee)

# To delete admin when necessary
# admin_email_revoke = "sample@email.com"
# revoke_admin(session, admin_email_revoke)
