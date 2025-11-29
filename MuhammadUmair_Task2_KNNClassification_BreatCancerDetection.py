from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = load_breast_cancer()
X = data.data
y = data.target
X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size=0.2)
model1 = KNeighborsClassifier(n_neighbors=7)
model1.fit(X_train1, y_train1)
acc_unscaled = model1.score(X_test1, y_test1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_scaled, y, test_size=0.2)
model2 = KNeighborsClassifier(n_neighbors=7)
model2.fit(X_train2, y_train2)
acc_scaled = model2.score(X_test2, y_test2)
plt.bar(['Unscaled', 'Scaled'], [acc_unscaled, acc_scaled])
plt.ylabel('accuracy')
plt.title('KNN accuracy comparison')
plt.show()

print("Unscaled Accuracy:", acc_unscaled)
print("Scaled Accuracy:", acc_scaled)
