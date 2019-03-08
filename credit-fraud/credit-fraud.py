import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("creditcard.csv")

df_train, df_test = train_test_split(df, test_size=0.2)

model = SGDClassifier(max_iter=1000, tol=1e-5)
model.fit(df_train.iloc[:, 0:30], df_train["Class"])
prediction = model.predict(df_test.iloc[:, 0:30])

print(classification_report(df_test["Class"], prediction, target_names=["Legal", "Fraud"]))