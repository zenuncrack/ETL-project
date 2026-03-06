from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
port = os.getenv("port")
database = os.getenv("database")
username = os.getenv("username")
password = os.getenv("password")

def load_data(df, table_name):
    engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")
    try:
      df.to_sql(table_name, engine, if_exists='replace', index=False)
    except Exception as e:
        print(f"Error loading data into {table_name}: {e}")