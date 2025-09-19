# SmartEcoNet: AI for Energy Optimization ⚡🤖

SmartEcoNet is an AI-powered solution designed to promote **energy-efficient appliance usage**.  
It leverages machine learning to analyze patterns in energy consumption and provides smart insights that help reduce wastage and optimize usage.  

---

## 🚀 Features
- Predicts and analyzes appliance energy consumption  
- Offers insights for energy-efficient usage  
- Interactive **Streamlit dashboard** for real-time visualization  
- Simple and user-friendly interface  

---

## 🛠 Tech Stack
- **Python 3.11**  
- **Streamlit** (for dashboard and UI)  
- **Joblib** (for loading ML model)  
- **NumPy / Pandas** (for data handling)  
- **Scikit-learn** (for building the ML model)  

---

## 📂 Project Structure
SmartEcoNet-AI-Energy-Optimization/
│
├── app.py # Main Streamlit app
├── final_energy_model.pkl # Trained ML model
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .gitignore # Ignore unnecessary files


## ⚡ Installation & Setup

1. **Clone the repository**
   git clone https://github.com/<your-username>/SmartEcoNet-AI-Energy-Optimization.git
   cd SmartEcoNet-AI-Energy-Optimization

2. **Create a virtual environment**

python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

3. **Install dependencies**
    pip install -r requirements.txt

4. **Run the Streamlit app**
    streamlit run app.py
