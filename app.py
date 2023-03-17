import streamlit as st
import pickle
import numpy as np

filename = 'model.pickle'
model = pickle.load(open(filename, "rb"))

st.title("Revenue Prediction")
x = np.array(st.number_input("Input Temperature")).reshape(-1,1)
if st.button("Predict"):
  st.success(*model.predict(x))
