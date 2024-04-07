import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import json

PATH_DATA = "flats_cleaned.csv"

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

df= load_data(PATH_DATA)


st.markdown("#### Number of flats by district")

pie_chart_dist = px.pie(df, names='district')

st.plotly_chart(pie_chart_dist)

st.write('In this dataset, about 25,2% of the apartments are placed in Pechersky district.'
         ' The smallest percent of the flats are placed in Desnyanskiy district(3.78%)')

category_mapping = {
    0 : 'No',
    1 : 'Yes'
}

df['metro_text'] = df['metro'].map(category_mapping)

st.markdown("#### Number of flats that are placed near the metro and no")

pie_chart_metro = px.pie(df, names='metro_text')

st.plotly_chart(pie_chart_metro)
st.write('About 40 percent of the flats from this dataset are placed near the metro')

st.markdown("#### Number of flats by rooms number")
pie_chart_rooms = px.pie(df, names='rooms')

st.plotly_chart(pie_chart_rooms)
st.write('The most popular number of rooms in flats is 2. '
         'Then goes flats with one room and with 3. Flats with 4 rooms take only 8 '
         'percent from all sample, and flats with 5 and 6 are about 2.39 and 0.3 '
         'respectively.')



st.markdown("#### Prices")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Max price", df.price.max())
col2.metric("Min price", df.price.min())
col3.metric("Average price", round(df.price.mean(), 2))
col4.metric("Median price", df.price.median())

histogram = px.histogram(df, x='price', nbins=50, title='Histogram of the prices')

st.plotly_chart(histogram)

st.write('The Distribution of prices is very right-skewed, so there is a big difference between '
         'average and median values.')

st.markdown("#### Median price by districts")

df_grouped = df.groupby(['district'])['price'].median().reset_index().sort_values('price', ascending=False)

df_grouped.district.replace("Солом'янський", "Солом’янський", inplace=True)

df_grouped.district = df_grouped.district.apply(lambda x : x + ' район')


bar_chart = px.bar(data_frame=df_grouped,
                   x='district', y='price')

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

st.write('Pechersky district has the highest median price and the smallest has Desnyanskiy')

st.markdown("#### Correlation")

corr_matrix = df.corr(numeric_only=True).round(2)

heatmap = px.imshow(corr_matrix, text_auto=True, title='Correlation matrix')

st.plotly_chart(heatmap)

st.write('Between numeric features area of the flat is the most correlated feature '
         'with price. Also, some other features with high correlation '
         'coefficients like rooms or kitchen areas depend on the total area.')


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


st.markdown("#### Price for flats placed near metro and no")

df_metro = df.groupby(by='metro').price.median().reset_index()
bar_chart_metro = px.bar(data_frame=df_metro, x='metro', y='price')

st.plotly_chart(bar_chart_metro)




