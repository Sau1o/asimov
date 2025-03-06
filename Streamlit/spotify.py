import streamlit as st
import pandas as pd


df = pd.read_csv("01 Spotify.csv")

df.set_index("Artist", inplace=True)
st.line_chart(df[df["Stream"] > 1000000000]["Stream"])
