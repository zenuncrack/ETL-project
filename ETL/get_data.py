import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

#url = os.getenv("DUMMY_URL")

def extract_product_data(url):
    response = requests.get(f"{url}/products")
    data = response.json()
    response.raise_for_status()

    product_df = pd.DataFrame(data)

    return product_df 

def extract_customer_data(url):
    response = requests.get(f"{url}/users")
    data = response.json()
    response.raise_for_status()
    customer_df = pd.DataFrame(data)
    return customer_df

