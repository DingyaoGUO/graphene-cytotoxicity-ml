# Graphene Cytotoxicity Machine Learning Demo
# Features: Size, Layers, C/O ratio
# Target: Cell Viability (%)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_excel("data/graphene_cytotoxicity_dataset.xlsx", sheet_name="cytotoxicity")

# Rename columns to English
df = df.rename(columns={
    "尺寸范围 （μm）": "Size",
    "层数范围 (层)": "Layers",
    "碳氧比": "CO_ratio",
    "细胞存活率 (%)": "Cell_Viability"
})

# Convert range values (e.g. 0.1~0.5) to average
def parse_range(val):
    if isinstance(val, str) and "~" in val:
        try:
            low, high = val.split("~")
            return (float(low) + float(high)) / 2
        except:
            return np.nan
    try:
        return float(val)
    except:
        return np.nan

for col in ["Size", "Layers", "CO_ratio", "Cell_Viability"]:
    df[col] = df[col].apply(parse_range)

# Remove missing values
df_clean = df[["Size", "Layers", "CO_ratio", "Cell_Viability"]].dropna()

# Define features and target
X = df_clean[["Size", "Layers", "CO_ratio"]]
y = df_clean["Cell_Viability"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Print feature importance
importances = model.feature_importances_
features = X.columns

print("Feature Importances:")
for f, imp in zip(features, importances):
    print(f"{f}: {imp:.4f}")

# Plot feature importance
plt.figure(figsize=(5,3.5))
plt.barh(features, importances)

plt.xlabel("Feature Importance")
plt.title("Feature Importance for Cell Viability Prediction")

plt.tight_layout()

# Save figure
plt.savefig("figures/feature_importance.png", dpi=300)

plt.show()

# Model performance
print("Model R² score:", model.score(X_test, y_test))
