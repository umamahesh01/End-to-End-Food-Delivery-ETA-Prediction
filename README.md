# 🍔 Food Delivery Time Prediction - End-to-End Machine Learning Project

An end-to-end Machine Learning system designed to predict **food delivery times** based on restaurant data, order costs, cuisine types, day of the week, and preparation times. This real-time project follows production-level ML standards with a fully modular pipeline and extensible architecture.

---

## 🚀 Highlights

- 🔄 End-to-End ML Workflow: Data → Preprocessing → Feature Engineering → Modeling → Evaluation  
- 🧱 Real-world Modular Codebase: Follows scalable design patterns  
- 🧠 Regression Models: Linear, Decision Tree, Random Forest, SVM  
- ⚙️ Custom missing value handling, encoding, scaling, and outlier removal  
- 📦 Model saving for future inference

---

## 📁 Project Structure

```
Delivery_Time_Prediction/
│
├── data/                       # Raw dataset (CSV)
├── artifacts/                  # Trained model (.pkl)
├── config/                     # YAML configuration
├── src/
│   ├── base/                   # Base strategies for missing value handler
│   ├── data/                   # Data loading
│   ├── preprocessing/
│   │   ├── feature_engineering/ # Encoding, Scaling, Outlier Removal
│   │   └── missing_value_handler.py
│   └── model/                  # Training and evaluation logic
├── main.py                     # Main ML driver script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 📊 Dataset Overview

Key columns used:
- `restaurant_name`
- `cuisine_type`
- `cost_of_the_order`
- `day_of_the_week`
- `food_preparation_time`
- `delivery_time` (target)

---

## ⚙️ How to Run

1. **Clone the repo**  
```bash
git clone https://github.com/umamahesh01/End-to-End-Machine-Learning.git
cd End-to-End-Machine-Learning
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Train the model**  
```bash
python main.py
```



## 🧠 Tech Stack

- Python
- pandas, NumPy
- scikit-learn
- YAML config
- Matplotlib / Seaborn (for EDA)

---

## 📌 Author

**Uma Mahesh Reddy**  
[GitHub Profile](https://github.com/umamahesh01)

---

> ⭐ Don’t forget to star the repo if you like it!
