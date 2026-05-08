import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

fake = pd.read_csv("dataset/Fake.csv")
true = pd.read_csv("dataset/True.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake,true])

data = data[["text","label"]]

X = data["text"]
y = data["label"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

vectorizer = TfidfVectorizer(stop_words="english")

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()

model.fit(X_train_vec,y_train)

pred = model.predict(X_test_vec)

print("Accuracy:",accuracy_score(y_test,pred))

pickle.dump(model,open("model/model.pkl","wb"))
pickle.dump(vectorizer,open("model/vectorizer.pkl","wb"))