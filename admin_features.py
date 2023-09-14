import json

mist_api_path = "https://api.mist.com"
mist_api_token = "your_api_token"  # API Token
org_id = "your_org_id"  # Org ID
headers = {
    "Content-Type": "application/json",
    "Authorization": "Token " + mist_api_token,
}


def get_admins(session, org_id):
    # get current admins from Org, READ-ONLY
    url = mist_api_path + "/api/v1/orgs/{}/admins".format(org_id)

    result = session.get(url, headers=headers)
    # pp.pprint(result)  # <Response [200]>

    if result.status_code != 200:
        print("Failed to GET")
        print("URL: {}".format(url))
        print("Response: {} ({})".format(result.text, result.status_code))
        return []

    result = json.loads(result.text)
    return result


def invite_admin(session, new_admin):
    # Invite new admin(s)
    url = "{}/api/v1/orgs/{}/invites".format(mist_api_path, org_id)

    result = session.post(url, data=json.dumps(new_admin), headers=headers)

    if result.status_code != 200:
        print("Failed to POST")
        print("URL: {}".format(url))
        print("Response: {} ({})".format(result.text, result.status_code))
        return []
    else:
        print(
            "Successfully invited {} {} ({})! ({})".format(
                new_admin["first_name"],
                new_admin["last_name"],
                new_admin["email"],
                result.status_code,
            )
        )

    return


def revoke_admin(session, email):
    # Revoke invitation if needed
    admin_first_name = ""
    admin_last_name = ""
    admin_invite_id = ""
    invite_flag = False

    admins = get_admins(session, org_id)

    for admin in admins:
        if admin["email"] == email:
            if "invite_id" in admin:
                admin_invite_id = admin["invite_id"]
                invite_flag = True
            else:
                admin_invite_id = admin["admin_id"]
            admin_first_name = admin["first_name"]
            admin_last_name = admin["last_name"]
            break
    if not admin_invite_id:
        print("Cannot find admin with email {}.".format(email))
        print("Please Double Check!\n")
        return

    if invite_flag:
        url = "{}/api/v1/orgs/{}/invites/{}".format(
            mist_api_path, org_id, admin_invite_id
        )
    else:
        url = "{}/api/v1/orgs/{}/admins/{}".format(
            mist_api_path, org_id, admin_invite_id
        )

    result = session.delete(url, headers=headers)

    if result.status_code != 200:
        print("Failed to DELETE")
        print("URL: {}".format(url))
        print("Response: {} ({})\n".format(result.text, result.status_code))
        return []
    else:
        print(
            "Successfully deleted {} {} (admin or invite id: {})! ({})\n".format(
                admin_first_name,
                admin_last_name,
                admin_invite_id,
                result.status_code,
            )
        )

    return
