"""
install:
pip install -r requirements.txt 
"""
import os

import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib import pyplot as plt
from sqlalchemy import create_engine


conns = os.environ["POSTGRES_CONNECTION_STRING"]
print(conns)

# db = create_engine("sqlite:///penguins.db")
db = create_engine(conns)
db.execute("DROP TABLE IF EXISTS penguins")

df = sns.load_dataset("penguins")
print(df.shape)

df.to_sql("penguins", db)  # name of table, db connection

df = pd.read_sql("SELECT * FROM penguins LIMIT 3", db)
print(df)
