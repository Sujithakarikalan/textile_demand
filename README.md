# GarmentPro – Smart Garment Production Management System

## Setup & Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the Flask app:
```
python app.py
```

3. Open browser at: http://localhost:5000

## ML Model
The `model/demand_model.pkl` is a pre-trained Random Forest Regressor.
To retrain: `python model/train_model.py`

## Project Structure
```
project/
├── app.py                  # Flask backend + routes
├── requirements.txt
├── model/
│   ├── demand_model.pkl    # Trained ML model
│   └── train_model.py      # Model training script
├── templates/
│   ├── base.html           # Base layout with navbar/footer
│   ├── index.html          # Home page
│   ├── about.html          # Industry overview
│   ├── problems.html       # Industry challenges
│   ├── solution.html       # Proposed solution
│   ├── forecast.html       # AI Demand Forecasting (ML form)
│   ├── dashboard.html      # Analytics Dashboard
│   ├── orders.html         # Order Management
│   ├── production.html     # Production Tracking
│   └── contact.html        # Contact Page
└── static/
    └── css/style.css       # Custom styles
