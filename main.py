from ETL.transform import transform_product_data, transform_customer_data
from ETL.load import load_data
from ETL.get_data import extract_product_data, extract_customer_data
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    url = os.getenv("DUMMY_URL")

    product_df = extract_product_data(url)
    customer_df = extract_customer_data(url)

    transformed_product_df = transform_product_data(product_df)
    transformed_customer_df = transform_customer_data(customer_df)

    load_data(transformed_product_df, "products")
    load_data(transformed_customer_df, "customers")

if __name__ == "__main__":
    main()