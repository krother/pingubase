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


#conns = os.environ["POSTGRES_CONNECTION_STRING"]
#print(conns)

db = create_engine("sqlite:///penguins.db")
#db = create_engine(conns)
db.execute("DROP TABLE IF EXISTS penguins")

df = sns.load_dataset("penguins")
print(df.shape)

df.to_sql("penguins", db)  # name of table, db connection

df = pd.read_sql("SELECT * FROM penguins", db)

st.write("""
# Penguin Dashboard

*a nice dashboard about penguins*
""")
st.write(df.head(3))

min_flip = st.slider("minimum flipper length", 0, 300)
max_flip = st.slider("maximum flipper length", 0, 300)

#df = df[(df["flipper_length_mm"] >= min_flip) & (df["flipper_length_mm"] <= max_flip)]
df = df[df["flipper_length_mm"].between(min_flip, max_flip)]

# use a streamlit plotting function
st.bar_chart(df["species"].value_counts())

# use the matplotlib stack
figure = plt.figure()
sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species")

st.pyplot(figure)
