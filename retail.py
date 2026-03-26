import pandas as pd
import numpy as np

np.random.seed(42)

months = np.random.randint(1,13,500)
product_type = np.random.randint(0,4,500)
previous_demand = np.random.randint(1500,3000,500)
fabric_stock = np.random.randint(4000,6000,500)
production_capacity = np.random.randint(2500,3500,500)

demand = (
    0.6*previous_demand +
    0.25*production_capacity +
    0.05*fabric_stock +
    np.random.normal(0,100,500)
)

data = pd.DataFrame({
    "Month":months,
    "Product_Type":product_type,
    "Previous_Demand":previous_demand,
    "Fabric_Stock":fabric_stock,
    "Production_Capacity":production_capacity,
    "Demand":demand.astype(int)
})

data.to_csv("textile_demand_dataset.csv",index=False)

print("Dataset created")