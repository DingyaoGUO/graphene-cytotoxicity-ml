# ================================
# Graphene Cytotoxicity ML Demo
# 输入特征: Size, Layers, C/O ratio
# 输出变量: Cell Viability (%)
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# 1. 读取数据
filepath = r"C:\Users\GDY\Desktop\Background\In-Semester 2025\Part 2\Total.xlsx"
df = pd.read_excel(filepath, sheet_name="cytotoxicity")

# 2. 重命名关键列
df = df.rename(columns={
    "尺寸范围 （μm）": "Size",
    "层数范围 (层)": "Layers",
    "碳氧比": "CO_ratio",
    "细胞存活率 (%)": "Cell_Viability"
})

# 3. 将范围型数据转为均值
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

# 4. 去除缺失值
df_clean = df[["Size", "Layers", "CO_ratio", "Cell_Viability"]].dropna()

# 5. 定义特征和目标
X = df_clean[["Size", "Layers", "CO_ratio"]]
y = df_clean["Cell_Viability"]

# 6. 拆分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. 训练随机森林模型
model = RandomForestRegressor(random_state=42, n_estimators=200)
model.fit(X_train, y_train)

# 8. 提取特征重要性
importances = model.feature_importances_
feature_names = X.columns

print("Feature Importances:")
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")

# 9. 绘制条形图
plt.figure(figsize=(5, 3.5))
bars = plt.barh(feature_names, importances, color=["#5DADE2", "#48C9B0", "#F5B041"])
plt.xlabel("Feature Importance", fontsize=11)
plt.title("Feature Importance in Predicting Cell Viability", fontsize=12, weight="bold")
plt.xlim(0, 1)
plt.tight_layout()
plt.show()
# 10. 评估模型性能
print(f"Model R² score: {model.score(X_test, y_test):.3f}")