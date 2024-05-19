
# Project Title
Airbnb Analysis

# Project objective:

1.This project aims to analyze Airbnb data using Python and perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.

2.Clean and prepare the dataset, addressing missing values, duplicates, and data type conversions for accurate analysis.

3.Develop a streamlit web application with interactive maps showcasing the distribution of Airbnb listings, allowing users to explore prices, ratings, and other relevant factors.

4.Conduct price analysis and visualization, exploring variations based on location, property type, and seasons using dynamic plots and charts.

5.Investigate location-based insights by extracting and visualizing data for specific regions or neighborhoods.

6.Create interactive visualizations that enable users to filter and drill down into the data.

7.Build a comprehensive dashboard using Tableau or Power BI, combining various visualizations to present key insights from the analysis.

# project workflow

Step 1: Collecting the Airbnb Json file And store it our local work environment

Step 2: Use  Python scripting to load the Json file in our notebook

step 3:Exploratory Data Analysis (EDA) for Data Preprocessing and removing the unwanted data

Step 4: Creating a data frame

Step 5: Converting the data frame into a csv file

Step6: Using streamlit and Power BI to create the dashboard to visualise the Data

Step7: Correcting the insights from the data visualisation and providing reasons for the insights with conclusion

# Python scripting
## Required libraries
json and pandas
We used following code to load the Json file in a variable
with open(r'path of the file', 'r') as file:
## Load the JSON data
    data = json.load(file)
1.Once data is loaded we create a dictionary file to store the values from data variable

2. We use the looping  method for loop to append the data one by one in the created dictionary from data variable.

3.Using the following code Df1=pd.DataFrame(D1) to convert the dictionary file (D1)  into a data frame called Df1



##  Exploratory Data Analysis (EDA)
After creating the data frame we explore the data first we find the duplicates values if there is no duplicate values then we will find null values in different columns. We will try to fill the null values with appropriate values using various methods.
### After EDA we convert the data frame into a csv file And store the file in our local Work environment.
## Creating a dashboard
We use streamlit and power bi to visualise the csv file that we created after EDA By creating various maps, charts and tables to analyse the data and to get various insights from that data, the dashboard is created in such a way that the user can visualise various price related and property related data with respect to various countries and various property types which helps the user to analyse the trend.
## Adding insights 
After creating the dashboard based on the dashboard visualisation we collect various insights from the data and provide the reasons for that insights with conclusions.