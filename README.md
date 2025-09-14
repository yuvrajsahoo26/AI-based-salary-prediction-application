# AI-based-salary-prediction-application

# 💼 Salary Prediction Application

This project predicts whether a person’s income is **greater than 50K** or **less than or equal to 50K** per year using **Machine Learning**.  
It uses demographic and work-related features like age, gender, education, working hours, etc.

---

## 📌 Features
- Predicts salary class (<=50K or >50K)  
- User-friendly **Streamlit** web app interface  
- Uses **Scikit-learn** for ML pipeline  
- Trained on **Adult Census Income Dataset** (48,842 rows, 15 columns)

---

## 🛠️ Technologies Used
- **Python 3**  
- **Pandas / NumPy** – Data handling  
- **Matplotlib / Seaborn** – Visualization  
- **Scikit-learn** – Preprocessing, model training & evaluation  
- **Streamlit** – Web app deployment  

---

## 📂 Dataset
- **Source:** UCI Adult Census Income dataset  
- **Features:** age, workclass, education, marital-status, occupation, relationship, race, gender, capital-gain, capital-loss, hours-per-week, native-country  
- **Target:** `income` → (`<=50K`, `>50K`)

---

## 🔄 Workflow
1. **Data Preprocessing**  
   - Handle missing values (`?`)  
   - Encode categorical features (gender, workclass, education, etc.)  
   - Normalize/scale numeric features if needed  

2. **Data Splitting**  
   - Train/Test split (80% / 20%)  

3. **Model Training**  
   - Algorithms tried: Logistic Regression, Random Forest  
   - Final model: Random Forest (better accuracy)  

4. **Model Evaluation**  
   - Accuracy, Precision, Recall, F1-score, Confusion Matrix  

5. **Deployment**  
   - Interactive app built with **Streamlit**  
   - User enters inputs → App predicts salary class  

---

## 👨‍💻 Author

  -  Name: Yuvraj Sahoo
  -  Qualification: B.Tech in Computer Science and Engineering (CSE), BPUT University
  -  Year: 3rd Year (5th Semester)
  -  Skills & Interests: Artificial Intelligence, Machine Learning, Data Science, Web Development
