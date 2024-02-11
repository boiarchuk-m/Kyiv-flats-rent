import streamlit as st
import pickle
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Prediction")

MODEL_PATH = "model&pipeline.bin"


@st.cache_data
def load_model(path):
    with open(path, 'rb') as f_in:
        column_transformer, model = pickle.load(f_in)
    return column_transformer, model


def predit_price(flat):
    column_transformer, model = load_model(MODEL_PATH)
    flat_df = pd.DataFrame([flat])
    flat_df = column_transformer.transform(flat_df)
    price = model.predict(flat_df)
    return price


st.header("Flats price prediction in Kyiv")

district = st.selectbox("Choose the district", ('Печерський', 'Деснянський',
                                                'Шевченківський', 'Дніпровський', 'Голосіївський', "Солом'янський",
                                                'Святошинський', 'Оболонський', 'Дарницький', 'Подільський'))

rooms = st.selectbox("Choose the number of rooms", ('1', '2', '3', '4', '5', '6'))
floor = st.number_input("Input the flat floor number", min_value=1, max_value=60)
floor_total = st.number_input("Input the house floor number", min_value=1, max_value=60)
total_area = st.number_input("Input total flat area", min_value=9.0, max_value=600.0, value=40.0)
kitchen_area = st.number_input("Input kitchen area", min_value=1.0, max_value=60.0, value=10.0)
metro = int(st.checkbox("Near the metro", ))

flat_data = {'district': district, 'rooms': rooms, 'floor': floor, 'floor_total': floor_total,
             'total_area': total_area, 'kitchen_area': kitchen_area, 'metro': metro}

button = st.button("Predict", type="primary")
if button:
    price = predit_price(flat_data)
    price = np.exp(price)

    st.write('Price: ', round(price[0]), 'грн')
