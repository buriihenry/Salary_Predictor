import streamlit as st
from predict_page import show_predict_page
from explore import show_explore


page = st.sidebar.selectbox("Explore or Predict", ("Predict","Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore()
    