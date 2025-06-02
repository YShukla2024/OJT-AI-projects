📊 Zomato Dataset - Exploratory Data Analysis (EDA)
📁 Dataset Source
Name: Zomato Restaurants Dataset

Source: Kaggle - Zomato Bangalore Restaurants (exact link not provided here; user should locate it by searching "Zomato Bangalore dataset")

Format: CSV (Zomato-data-.csv)

🔍 Objective
To perform exploratory data analysis on Zomato’s restaurant data in order to understand:

Customer behavior

Restaurant characteristics

Service features like online orders and table booking

Cost patterns and popularity indicators

📦 Features Used
Column Name	Description
name	Restaurant name
online_order	Whether online ordering is available (0/1)
book_table	Whether table booking is available (0/1)
rate	Average rating (may require cleaning)
votes	Number of customer votes
approx_cost(for two people)	Approximate cost for two
listed_in(type)	Type of service (Delivery, Buffet, etc.)

📈 EDA Performed

✅ Univariate Analysis

✅ Bivariate Analysis

✅ Multivariate Analysis

✅ Correlation Analysis
Correlation matrix and heatmap for numeric variables:

votes, approx_cost, rate (if converted)

📌 Key Insights (Example)
Restaurants offering online ordering tend to have slightly higher average ratings.

High-vote restaurants are not always high-cost.

Table booking services are relatively rare among highly rated places.

🛠️ Tools Used
Python (Pandas, NumPy)

Visualization: Matplotlib, Seaborn
