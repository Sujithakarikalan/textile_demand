import csv
from datetime import date
from pathlib import Path


def month_year_n_months_ago(months_ago: int):
    today = date.today()
    year = today.year
    month = today.month - months_ago
    while month <= 0:
        month += 12
        year -= 1
    return year, month


def build_dataset_rows():
    # Product code mapping aligned with app.py PRODUCT_MAP.
    products = [
        {"code": 0, "name": "Shirts", "base": 2600, "fabric_factor": 1.78},
        {"code": 1, "name": "Innerwear", "base": 3400, "fabric_factor": 1.65},
        {"code": 2, "name": "Kids Wear", "base": 1850, "fabric_factor": 1.82},
        {"code": 3, "name": "Trousers", "base": 2200, "fabric_factor": 1.74},
    ]
    seasonality = {
        1: 0.94, 2: 0.96, 3: 1.01, 4: 1.05, 5: 1.08, 6: 1.11,
        7: 1.13, 8: 1.10, 9: 1.07, 10: 1.04, 11: 1.00, 12: 0.97
    }
    rows = []

    # Build 36 months of historical records ending at current month.
    for product in products:
        prev_demand = int(product["base"] * 0.92)
        for months_ago in range(35, -1, -1):
            year, month = month_year_n_months_ago(months_ago)
            trend = 0.985 + (35 - months_ago) * 0.004
            seasonal = seasonality[month]

            previous_month_demand = prev_demand
            fabric_stock = int(previous_month_demand * product["fabric_factor"] + (product["code"] + 1) * 85)

            # Demand target follows realistic progression from previous demand + stock + season.
            demand = int(previous_month_demand * 0.70 + fabric_stock * 0.11 + product["base"] * 0.09 * seasonal)
            demand = int(demand * trend)

            rows.append(
                {
                    "year": year,
                    "month": month,
                    "month_key": f"{year:04d}-{month:02d}",
                    "product_type_code": product["code"],
                    "product_type_name": product["name"],
                    "previous_month_demand": previous_month_demand,
                    "fabric_stock": fabric_stock,
                    "demand": demand,
                }
            )

            prev_demand = demand

    return rows


def main():
    project_root = Path(__file__).resolve().parents[1]
    dataset_path = project_root / "data" / "garment_historical_dataset.csv"
    dataset_path.parent.mkdir(parents=True, exist_ok=True)

    rows = build_dataset_rows()
    fieldnames = [
        "year",
        "month",
        "month_key",
        "product_type_code",
        "product_type_name",
        "previous_month_demand",
        "fabric_stock",
        "demand",
    ]

    with dataset_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Historical dataset created: {dataset_path}")
    print(f"Total rows: {len(rows)}")


if __name__ == "__main__":
    main()
