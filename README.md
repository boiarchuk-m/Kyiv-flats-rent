# Flats rent price prediction in Kyiv
## Table of contents
- [Project description](https://github.com/boiarchuk-m/Kyiv-flats-rent/blob/main/README.md#problem-description)
- [Technologies](https://github.com/boiarchuk-m/Kyiv-flats-rent/blob/main/README.md#technologies)
- [Repository files and directories](https://github.com/boiarchuk-m/Kyiv-flats-rent/blob/main/README.md#repository-files-and-directories)
- [Models performance](https://github.com/boiarchuk-m/Kyiv-flats-rent/blob/main/README.md#models-performance)

### Link to the Streamlit app: https://kyiv-flats-rent-price.streamlit.app/

## Problem description
This project was made for rent price analysis and prediction in Kyiv city. The data was scraped on 21-25 January 2024. This dataset contains general information about flats like total area, kitchen area, number of rooms, district, floor, total number of floors in the house, and nearby metro stations. However, it doesn't contain private information like exact addresses, names, numbers, etc.

## Technologies:
- Python libraries: Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn, Plotly
- Deployment: Streamlit
- Version control: Git, Github
 


## Repository files and directories
- `datasets` folder with uncleaned datasets
- `Data_cleaning.ipynb` jupyter notebook with data cleaning
- `Data_analysis.ipynb` jupyter notebook with data analysis
- `Model_training.ipynb` jupyter notebook with models development
- `model&pipeline.bin` binary file with trained model and pipeline for data preprocessing
- `flats.csv` dataset
- `flats_cleaned.csv` cleaned dataset for web application
- `Pipfile` and `Pipfile.lock` files with dependencies for the environment
- `web_application` files with Streamlit pages
- `export.geojson` Geogson file created with https://overpass-turbo.eu/ with districts polygons for map 

## Models performance
- Lasso Regression - R2 score = 0.743437
- Ridge Regression - R2 score = 0.743419
- DecisionTree Regression - R2 score = 0.861405
- RandomForest Regression - R2 score = 0.876345	
- GradientBoosting Regression - R2 score = 0.921689

