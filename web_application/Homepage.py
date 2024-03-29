import streamlit as st


st.set_page_config(
    page_title="Homepage"
)
st.sidebar.success("Select a page above")

st.title("Flats rent price prediction in Kyiv")

st.subheader("About the project:")

st.markdown(" This project was made for rent price analysis and prediction in Kyiv city. "
"The data was scraped on 21-25 January 2024. This dataset contains general information "
            "about flats like total area, kitchen area, number of rooms, district, "
            "floor, total number of floors in the house, and nearby metro stations. "
            "However, it doesn't contain private information like exact addresses, "
            "names, numbers, etc."
            "You can test prediction model on page prediction. On page Data analysis, you "
            "can see some analysis of this dataset.")

st.subheader("Technologies:")

st.markdown(" - **Python libraries:** Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn, Plotly \n"
            " - **Deployment:** Streamlit, Docker \n"
            " - **Version control:** Git, Github")
