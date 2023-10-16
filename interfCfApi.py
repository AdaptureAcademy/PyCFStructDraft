# Description: This file contains the classes and methods to interact with the Cloudflare API
import pandas as pd
from credentials import Credentials
import apiLayer



class Account:
    def __init__(self, id, name, settings):
        self.id = id
        self.name = name
        self.settings = settings

    def __str__(self):
        return f"Account name: {self.name:<40}\t account id: {self.id}"



class Accounts:
    def __init__(self, credentials: Credentials):
        self.credentials = credentials
        self.account_list: list[Account] = []
        self._call_api_list_accounts()

    def _call_api_list_accounts(self):
        accounts = apiLayer.list_accounts(self.credentials)
        for account in accounts:
            self.account_list.append(
                Account(account["id"], account["name"], account["settings"])
            )

    def get_account(self, name: str) -> Account:
        for account in self.account_list:
                if account.name == name:
                    return account
        else:
            print (f"Account {name} not found in accounts list of profile {self.credentials.X_Auth_Email}")
            return Account("NOT FOUND",f'NOT FOUND "{name}"',"")
        
    def get_account_by_id(self, id: str) -> Account:
        for account in self.account_list:
                if account.id == id:
                    return account
        else:
            print (f"Account {id} not found in accounts list of profile {self.credentials.X_Auth_Email}")
            return Account(f'NOT FOUND "{id}"',f"NOT FOUND","")
        
    def show_accounts(self):
        print(f"Accesible accounts for profile {self.credentials.X_Auth_Email}")
        for account in self.account_list:
            print(account)
        print(f"Total accounts: {len(self.account_list)}\n")

    def to_csv(self):
        index = self.credentials.X_Auth_Email.find('@')
        name = self.credentials.X_Auth_Email[:index]
        filename = f'{name}_Accounts.csv'
        data = {'Account Name': [account.name for account in self.account_list],
                'Account Id': [account.id for account in self.account_list] }
        table = pd.DataFrame(data)
        table.to_csv(filename, index=False)



# Get credentials from file and return a Credentials object
carles_credentials = Credentials("personal_credentials.txt")
print(carles_credentials.X_Auth_Email, carles_credentials.X_Auth_Key, sep="\n")
client_accounts = Accounts(carles_credentials)
# now we can work with the accounts_list and get what we want
client_accounts.show_accounts()
my_account = client_accounts.get_account(name="esen_suteki")
adapture_account = client_accounts.get_account("adapture")
print(my_account, adapture_account, sep="\n")
client_accounts.to_csv()
