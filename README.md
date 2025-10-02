# Telco Customer Churn Prediction 

Project ini bertujuan untuk memprediksi kemungkinan pelanggan melakukan **churn** (berhenti berlangganan) pada layanan telekomunikasi. Model machine learning dibangun menggunakan dataset pelanggan telco, kemudian dideploy menggunakan **Streamlit** agar dapat diakses secara interaktif melalui web.

## Latar Belakang

Churn pelanggan adalah salah satu tantangan terbesar dalam industri telekomunikasi. Dengan memprediksi churn sejak dini, perusahaan dapat melakukan tindakan preventif seperti memberikan promosi atau layanan khusus untuk mempertahankan pelanggan.

## Dataset

Dataset yang digunakan adalah **Telco Customer Churn Dataset**, yang berisi informasi pelanggan meliputi:

* Informasi demografi
* Layanan yang digunakan (internet, phone, dll.)
* Lama berlangganan
* Biaya bulanan dan total biaya
* Status churn (Yes/No)

## Alur Project

1. **Data Preprocessing**

   * Menangani missing values
   * Encoding fitur kategorikal
   * Normalisasi/standarisasi data

2. **Exploratory Data Analysis (EDA)**

   * Distribusi churn
   * Hubungan variabel dengan churn
   * Visualisasi pola penggunaan layanan

3. **Modeling**

   * Algoritma yang diuji: Logistic Regression, Random Forest, Gradient Boosting
   * Evaluasi model menggunakan Accuracy, Precision, Recall, F1-score, dan ROC-AUC
   * Model terbaik dipilih dan disimpan menggunakan `joblib`

4. **Deployment**

   * Aplikasi berbasis web menggunakan **Streamlit**
   * Input fitur pelanggan → Prediksi churn probability
   * Tampilan hasil prediksi dalam bentuk teks dan visual

## Deploy

Aplikasi sudah dapat dicoba secara online di sini:
👉 [Telco Churn Prediction App](https://telco-churn-prediction-andrilaksono.streamlit.app/)

## ✨ Hasil

* Model terbaik: **Gradient Boosting Classifier**
* ROC-AUC: 0.84
* Aplikasi web interaktif berhasil dibuat dan dideploy

## 📌 Portfolio

Proyek ini merupakan bagian dari portfolio saya di bidang **Data Science & Machine Learning**, khususnya terkait **Customer Analytics**.
