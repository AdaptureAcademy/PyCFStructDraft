# This script just calls the list all accounts Cloudflare API and prints the response
import requests, json


def list_accounts() -> str:
    url = "https://api.cloudflare.com/client/v4/accounts"

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": "my_Cloudflare@Email",  # replace with your email
        "X-Auth-Key": "My_Global_API_Key",  # replace with your Global API Key
        # "Authorization": "Bearer Ra7zWl7BXfsEK.......", #by the moment we don't need this
    }

    response = requests.request("GET", url, headers=headers)
    #convert response from  string to dictionary
    response = json.loads(response.text)
    return response


accounts_list = list_accounts()
