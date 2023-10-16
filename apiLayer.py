
import requests, json
from credentials import Credentials


def get_headers(credentials: Credentials) -> dict:
        headers = {
                    "Content-Type": "application/json",
                    "X-Auth-Email": credentials.X_Auth_Email,
                    "X-Auth-Key": credentials.X_Auth_Key,
                    # "Authorization": "Bearer {Ra7zWl7BXfsEK.......}", #by the moment we don't need this,
                }
        return headers

def list_accounts(credentials: Credentials) -> list:
        url= "https://api.cloudflare.com/client/v4/accounts"
        headers = get_headers(credentials)
        response = requests.request("GET",url = url, headers=headers)
        # Convert the response to a dictionary to can work with it
        response = json.loads(response.text)
        return response['result']

def list_zones(credentials: Credentials) -> list:
        url= "https://api.cloudflare.com/client/v4/zones"
        headers = get_headers(credentials)
        response = requests.request("GET",url = url, headers=headers)
        # Convert the response to a dictionary to can work with it
        response = json.loads(response.text)
        return response['result']

