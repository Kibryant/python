import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")
print(
    "\nRelatório de Classificação:\n",
    classification_report(y_test, y_pred, target_names=iris.target_names),
)

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names,
)
plt.xlabel("Predito")
plt.ylabel("Verdadeiro")
plt.title("Matriz de Confusão")
plt.show()

import joblib

joblib.dump(model, "modelo_iris.pkl")

modelo_carregado = joblib.load("modelo_iris.pkl")

novos_dados = [[5.1, 3.5, 1.4, 0.2]]  # Exemplo de entrada
previsao = modelo_carregado.predict(novos_dados)
print("Previsão:", iris.target_names[previsao][0])
