import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import json

PATH_DATA = "../flats_cleaned.csv"

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

df= load_data(PATH_DATA)


st.markdown("###### Descriptive statistics")
st.write(df.describe())

pie_chart_dist = px.pie(df, title="Total number of flats by districts",
                   names='district')

st.plotly_chart(pie_chart_dist)

category_mapping = {
    0 : 'No',
    1 : 'Yes'
}

df['metro_text'] = df['metro'].map(category_mapping)

pie_chart_metro = px.pie(df, title="Total number of flats by metro",
                   names='metro_text')

st.plotly_chart(pie_chart_metro)

pie_chart_rooms = px.pie(df, title="Total number of flats by number of rooms",
                   names='rooms')

st.plotly_chart(pie_chart_rooms)

df_grouped = df.groupby(['district'])['price'].median().reset_index().sort_values('price', ascending=False)

df_grouped.district.replace("Солом'янський", "Солом’янський", inplace=True)

df_grouped.district = df_grouped.district.apply(lambda x : x + ' район')


bar_chart = px.bar(data_frame=df_grouped,
                   x='district', y='price', title="Median price by districts")

st.plotly_chart(bar_chart)

with open("export.geojson", "r", encoding="utf-8") as file:
    kyiv_districts_geojson = json.load(file)

fig_map = px.choropleth_mapbox(df_grouped, geojson=kyiv_districts_geojson,
                           locations="district", featureidkey="properties.name",
                           color="price",
                           color_continuous_scale="haline",
                           mapbox_style="carto-positron",
                           opacity=0.8, center = {"lat": 50.4101, "lon": 30.5234},
                           labels= {'price' :'median price'},
                           zoom=9)

fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig_map)



st.markdown("###### Histogram of the prices")


histogram = px.histogram(df, x='price', nbins=50)

st.plotly_chart(histogram)

districts = df.district.unique()

fig = make_subplots(rows=5, cols=2, subplot_titles=districts)

dist_num = 0
for i in range(0, 5):
    for j in range(0, 2):
        fig.add_trace(go.Scatter(x=df[df.district == districts[dist_num]].price,
                                 y=df[df.district == districts[dist_num]].total_area, opacity=0.9,  mode='markers', name=districts[dist_num]), row = i+1, col=j+1)
        dist_num +=1

fig.update_layout(title_text="Flats price VS Area", autosize=False, width=900,  height=1100)


st.plotly_chart(fig)


st.markdown("###### Price by rooms")


box_plot = px.box(data_frame=df, x='rooms', y='price')

st.plotly_chart(box_plot)

corr_matrix = df.corr(numeric_only=True).round(2)

heatmap = px.imshow(corr_matrix, text_auto=True, title="Correlation matrix")

st.plotly_chart(heatmap)


