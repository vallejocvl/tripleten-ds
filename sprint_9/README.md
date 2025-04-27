# 📈 Megaline Telecom Plan Recommendation

This project was developed as part of a Data Science Bootcamp and focuses on helping **Megaline**, a telecom operator, improve its mobile plan recommendation system. By analyzing customer behavior and usage patterns, we aim to build a machine learning model that can suggest the most suitable plan—**Smart** or **Ultra**—for each user.

---

## 🗂️ Project Structure
├── sprint9_cvl_revision.ipynb     # Main Jupyter notebook with analysis and modeling
├── README.md                      # Project overview and instructions
└── data/                          # (Optional) Folder for storing data files

---

## 📊 Dataset Overview

The dataset includes anonymized customer records with the following key features:

- **Call duration and frequency**
- **Messages sent**
- **Internet usage (MB)**
- **Current plan (Smart or Ultra)**

Each row represents one customer. The task is to analyze this data and build a model that recommends either the **Smart** or **Ultra** plan for a given customer.

---

## 🔍 Key Objectives

- Explore customer behavior across different plans  
- Preprocess and prepare data for modeling  
- Build and evaluate multiple classification models  
- Recommend a plan based on predicted customer needs  
- Generate business insights for better marketing targeting  

---

## 🛠️ Tools & Libraries

- Python  
- Pandas & NumPy  
- Matplotlib & Seaborn  
- Scikit-learn (LogisticRegression, DecisionTree, RandomForest)  
- Jupyter Notebook  

---

## ✅ Results

After preprocessing and feature scaling, we evaluated multiple models using accuracy, precision, recall, and F1-score. The best-performing model achieved:
	•	Accuracy: ~ add actual score here
	•	F1-Score: ~ add actual score here

The model showed solid performance in distinguishing customers who would benefit more from the Ultra plan over the Smart one, helping Megaline tailor its offerings more effectively.

## 💡 Business Value

By accurately predicting customer preferences, Megaline can:
	•	Improve customer satisfaction with tailored plans
	•	Reduce churn by preventing plan mismatch
	•	Optimize marketing campaigns and upselling strategies