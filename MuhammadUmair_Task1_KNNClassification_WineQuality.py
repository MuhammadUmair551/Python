from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = load_wine()
X = data.data[:, :4]
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print("accuracy:", acc)
alcoholic = data.data[:, 0]
malic_acid = data.data[:, 1]
plt.scatter(alcoholic, malic_acid, c=y)
plt.xlabel("Alcohol")
plt.ylabel("malic acid")
plt.title("wine classes based on alcohol and malic acid")
plt.show()
