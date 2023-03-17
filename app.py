import streamlit as st
import pickle

filename = 'model.pickle'
model = pickle.load(open(filename, "rb"))

st.title("Revenue Prediction")
x = st.number_input("Input Temperature")
if st.button("Predict"):
  st.success(model.predict(x))
