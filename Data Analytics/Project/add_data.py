import pandas as pd
from sqlalchemy import create_engine

# ===========================
# Mysql Connection
# ===========================

username = 'root'
password = 'root'
host = '127.0.0.1'
port = 3306
database = '360_education_db'

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# =========================
# Excel File Path 
# =========================

excel_file = "360_Education_Business_Analytics_Dataset.xlsx"

# Read all sheets
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Load each sheet into msyql
for sheet_name, df in all_sheets.items():

    # Table name
    table_name = sheet_name.lower().replace(" ","_")

    # load Data
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"{table_name} uploaded successfully")

print("All sheet uploaded successfully")