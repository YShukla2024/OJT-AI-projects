# OJT-AI-projects

# 📊 Project Architecture

This project is structured into four main layers:

### 1. **Data Layer**
- `restaurant_data.csv` → Restaurant dataset  
- `Zomato-data-.csv` → Zomato dataset for EDA  
- `superstore_sales_full.csv` → Sales dataset for Power BI  

### 2. **Processing Layer**
- `Data-Analysis.ipynb` → Performs EDA and feature engineering  
- `project.ipynb` → Trains machine learning models and generates model pickle  

### 3. **Serving / UI Layer**
- `app.py (Streamlit)` → Streamlit app for chatbot & model deployment  
- `Regional Sales Tracker.pbix` → Power BI dashboard for regional sales analysis  

### 4. **Documentation & Config**
- `README.md` → Main project overview  
- `requirements.txt` → Dependencies for running the project  
- `Readme.md (Chatbot-Streamlit)` → Documentation for the chatbot app  

---

## 🔗 Architecture Diagram  

Below is the flow of how data moves through the project:

![Project Flowchart](https://gitdiagram.com/YShukla2024/OJT-AI-projects/diagram.svg)

> 👉 [View interactive version here](https://gitdiagram.com/YShukla2024/OJT-AI-projects)  
(Click nodes to open files directly in the repository.)
