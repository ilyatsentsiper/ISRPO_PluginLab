def generate_sklearn_code(task_type="classification", use_scaler=True):
    model = "RandomForestClassifier" if task_type == "classification" else "RandomForestRegressor"

    code = f"""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import {model}
"""
    if use_scaler:
        code += "from sklearn.preprocessing import StandardScaler\n"

    code += f"""
# DataLoad
df = pd.read_csv('data.csv')
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
"""
    if use_scaler:
        code += """
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
"""
    code += f"""
model = {model}()
model.fit(X_train, y_train)
print("Done")
"""
    return code


if __name__ == "__main__":
    print(generate_sklearn_code("classification", True))
