import sklearn
from sklearn import datasets 
from sklearn import svm
from sklearn import metrics

cancer = datasets.load_breast_cancer()

print(cancer.feature_names)
print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

print(x_train,y_train)

classes = ['malignant','benign']

#Svm try to create a hyper plan, dividing the data 
#using something straight, a linear way to divide a dataset
#finding the same distance of the closest points of the classes 
#making the margin as big as possible 
#larger the margin, larger is the distance between the 2 classes
#and more accurate is the model
#It uses a kernel, to make the data 3 dimensional and possible
#to create a hyperplane in a more complex data 

clf = svm.SVC(kernel="linear")
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test,y_pred)

print(acc)

#The accuracy of the model stays between 92 - 97