<p align="center">
  <img src="https://raw.githubusercontent.com/sadiya595/SmartEcoNet-AI-Energy-Optimization/main/assets/banner.png" alt="SmartEcoNet Banner" width="800"/>
</p>

# ⚡ SmartEcoNet: AI-Powered Energy Optimization

[![Python Version](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-orange?style=flat-square)](https://share.streamlit.io/sadiya595/SmartEcoNet-AI-Energy-Optimization/main/app.py)
[![Repo Size](https://img.shields.io/github/repo-size/sadiya595/SmartEcoNet-AI-Energy-Optimization?style=flat-square)](https://github.com/sadiya595/SmartEcoNet-AI-Energy-Optimization)
[![Downloads](https://img.shields.io/github/downloads/sadiya595/SmartEcoNet-AI-Energy-Optimization/total?style=flat-square)](https://github.com/sadiya595/SmartEcoNet-AI-Energy-Optimization/releases)

**SmartEcoNet** is an intelligent solution for **optimizing energy consumption** and promoting sustainable appliance usage.  
It leverages **machine learning** to analyze usage patterns and provides **actionable insights** to reduce energy wastage.  


## 🚀 Key Features
- 🔍 **Predict & Analyze** appliance energy consumption  
- 💡 **Smart Recommendations** for energy-efficient usage  
- 📊 **Interactive Streamlit Dashboard** for real-time visualization  
- 🎯 **User-Friendly Interface** with easy navigation  

---

## 🛠 Tech Stack
- **Python 3.11** – Core programming  
- **Streamlit** – Dashboard & UI  
- **Joblib** – Load & save ML models  
- **NumPy / Pandas** – Data handling & analysis  
- **Scikit-learn** – Machine learning models  

---

## 📂 Project Structure
```text
SmartEcoNet-AI-Energy-Optimization/
│
├── app.py                   # Main Streamlit app
├── final_energy_model.pkl    # Trained ML model
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .gitignore                # Ignore unnecessary files


# 1. Clone the repository
git clone https://github.com/<your-username>/SmartEcoNet-AI-Energy-Optimization.git
cd SmartEcoNet-AI-Energy-Optimization

# 2. Create & activate a virtual environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
