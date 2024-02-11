import streamlit as st
import pandas as pd
import plotly.express as px

PATH_DATA = "flats_cleaned.csv"

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    data = df.sample(1000)
    return df, data

df, data = load_data(PATH_DATA)

st.markdown("###### Dataset")
st.write(data)

st.markdown("###### Descriptive statistics")
st.write(data.describe())

pie_chart_dist = px.pie(df, title="Total number of flats by districts",
                   names='district')

st.plotly_chart(pie_chart_dist)

df_grouped = df.groupby(['district']).mean().reset_index()

bar_chart = px.bar(data_frame=df_grouped,
                   x='district', y='price', title="Mean price by districts")


st.plotly_chart(bar_chart)

st.markdown("###### Histogram of the prices")
n_bins_selection = st.slider('nbins:', min_value=30, max_value=400, value=100)


histogram = px.histogram(df, x='price', nbins=n_bins_selection)

st.plotly_chart(histogram)

scatter_dist = px.scatter(data_frame=data, x='price', y='total_area', color='district', opacity=0.5, title="Price vs area")
st.plotly_chart(scatter_dist)


st.markdown("###### Price by rooms (sorted by districts)")

districts = ['Печерський', 'Деснянський','Шевченківський', 'Дніпровський', 'Голосіївський', "Солом'янський",
'Святошинський', 'Оболонський', 'Дарницький', 'Подільський']
district_section = st.multiselect('Districts:', districts, default=districts, )

mask = (df['district'].isin(district_section))

df_filter = df[mask]

box_plot = px.box(data_frame=df_filter, x='rooms', y='price')

st.plotly_chart(box_plot)

corr_matrix = df.corr(numeric_only=True).round(2)

heatmap = px.imshow(corr_matrix, text_auto=True, title="Correlation matrix")

st.plotly_chart(heatmap)
