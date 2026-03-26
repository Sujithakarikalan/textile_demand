import csv
from pathlib import Path

import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def load_dataset_rows(dataset_path):
    rows = []
    with dataset_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def main():
    project_root = Path(__file__).resolve().parents[1]
    dataset_path = project_root / "data" / "garment_historical_dataset.csv"
    model_path = project_root / "model" / "demand_model.pkl"

    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {dataset_path}. Run model/create_historical_dataset.py first."
        )

    rows = load_dataset_rows(dataset_path)

    X = np.array(
        [
            [
                int(r["month"]),
                int(r["product_type_code"]),
                float(r["previous_month_demand"]),
                float(r["fabric_stock"]),
            ]
            for r in rows
        ]
    )
    y = np.array([float(r["demand"]) for r in rows])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=12,
        min_samples_leaf=2,
        random_state=42,
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    joblib.dump(model, model_path)
    print(f"Model trained and saved: {model_path}")
    print(f"Dataset used: {dataset_path}")
    print(f"Rows: {len(rows)} | Test MAE: {mae:.2f} | Test R2: {r2:.4f}")


if __name__ == "__main__":
    main()
