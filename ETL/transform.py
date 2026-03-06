import pandas as pd 

def transform_product_data(product_df):

    df = product_df.copy()

    df = df.rename(columns={
        "id": "product_id",
        "title": "product_title",
        "price": "product_price",
        "description": "product_description",
        "category": "product_category",
    })

    df = df[[
        "product_id", "product_title", "product_price", "product_description", "product_category"]]
    
    df['product_price']= df['product_price'].astype(float)

    return df

def transform_customer_data(customer_df):
    
    df = customer_df.copy()

    df = df.rename(columns={
        "id": "customer_id",
        "email": "customer_email",
        "username": "customer_username",
        
    })

    df = df[[
        "customer_id", "customer_email", "customer_username"]]

    return df