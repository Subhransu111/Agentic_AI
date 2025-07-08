import requests

class CurrencyConverter:
    def __init__(self,api_key: str):
        self.BASE_URL = f"https://v6.exchange-api.com/v6/{api_key}/latest/"
    
    def convert(self , amount:float , from_currency:str , to_currency:str):
        """Convert the amount from one currency to another currency """

        url = f"{self.BASE_URL}/{from_currency}"

        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("API call failed ",response.json())
        
        rates = response.json()["conversion rates"]
        if to_currency not in rates:
            raise ValueError(f"{ to_currency} not found in exchange rates . ")
        return amount*rates[to_currency]





    
