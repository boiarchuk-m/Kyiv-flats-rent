# Flats rent price prediction in Kyiv
## Table of contents
- [Project description](https://github.com/boiarchuk-m/Kyiv-flats-rent/blob/main/README.md#problem-description)
- [Technologies](https://github.com/boiarchuk-m/Kyiv-flats-rent/blob/main/README.md#technologies)
- [Repository files and directories](https://github.com/boiarchuk-m/Kyiv-flats-rent/blob/main/README.md#repository-files-and-directories)
- [Models performance](https://github.com/boiarchuk-m/Kyiv-flats-rent/blob/main/README.md#models-performance)

### Link to the Streamlit app: https://flats-rent-price-pred-d7ay5ycwta-uc.a.run.app/

## Problem description
This project was made for rent price prediction in Kyiv city. The data was scraped on 21-25 January 2024. This dataset contains general information about flats like total area, kitchen area, number of rooms, district, floor, the total number of floors in the house, and nearby metro stations. However, it doesn't contain private information like exact addresses, names, numbers, etc. To find the best model, Lasso, Ridge, Decision Forest, Random Forest, and Gradient Boosting Regressors were optimized by using GridSearchCV. Also, there is a web application where you can test the model's performance. 

## Technologies:
- Python libraries: Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn, Plotly
- Deployment: Streamlit, Docker, Google Cloud
- Version control: Git, Github
 


## Repository files and directories
- `notebook.ipynb` jupyter notebook with EDA and models development
- `model&pipeline.bin` binary file with trained model and pipeline for data preprocessing
- `flats.csv` dataset
- `flats_cleaned.csv` cleaned dataset for web application
- `Pipfile` and `Pipfile.lock` files with dependencies for the environment
- `web_application` files with Streamlit pages
- `Dockerfile` a script to generate a docker container
- `request_cloud.py` a Python script to send a request to the cloud service

## Models performance
- Lasso Regression - R2 score = 0.743437
- Ridge Regression - R2 score = 0.743419
- DecisionTree Regression - R2 score = 0.861405
- RandomForest Regression - R2 score = 0.876345	
- GradientBoosting Regression - R2 score = 0.921689

