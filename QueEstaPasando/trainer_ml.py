from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.linear_model import LogisticRegression
from scipy import stats
from QueEstaPasando import clean_data
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
import numpy as np
import matplotlib as plt


class Trainer_ML(object):
    def __init__(self):
        pass

    def read_file(self):
        pd.set_option('max_colwidth', 800)
        data = pd.read_csv("../QueEstaPasando/data/total.csv", index_col=0)
        return data

    def split_data(self, data, test_size=0.3):
        X = data['text']
        y = data['score']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
        return X_train, X_test, y_train, y_test

    def fit_model_Randomize(self,X_train,y_train):
        # Create Pipeline
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(lowercase = False)),
            ('model', MultinomialNB()),
        ])

        parameters = {
            'tfidf__ngram_range': [(1,1), (2,2), (1,2),],
            'tfidf__min_df': stats.loguniform(0.01, 0.2),
            'tfidf__max_df': stats.loguniform(0.01, 0.3),
            'tfidf__norm' : ['l1', 'l2'] ,
            'model__alpha': stats.uniform(0.5, 1)
        }

        # Perform grid search on pipeline
        grid_search = RandomizedSearchCV(pipeline, parameters, n_jobs=-1,verbose=1, scoring = "accuracy", cv=5, n_iter=200, refit=True)
        grid_search.fit(X_train,y_train)
        return grid_search.best_estimator_

    def trainer(self):
        data = self.read_file()
        cl = clean_data.Clean_Data()
        data = cl.clean_data(data)
        X_train, X_test, y_train, y_test = self.split_data(data)
        model = self.fit_model_Randomize(X_train,y_train)
        joblib.dump(model, 'model.joblib')
        return model,X_test,y_test

    def score_model(self,model,X_test,y_test):
        result = model.score(X_test, y_test)
        return result
    
    def predict_model(self,model,X_test):
        result = model.predict(X_test)
        return result

    def plot_learning_curves(self,model,X_train,y_train,cv=5):
        # se crea la lista de verificacion
        train_sizes = [25,50,75,100,250,500,750,1000,1150]
        # se crea la linea de regresion
        train_sizes, train_scores, test_scores = learning_curve(estimator=model, X=X_train, y=y_train, train_sizes=train_sizes, cv=cv)
        # Se calcula la media de los score de cada una de los cv ejecutados
        train_scores_mean = np.mean(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        # Se grafica los score
        plt.plot(train_sizes, train_scores_mean, label = 'Training score')
        plt.plot(train_sizes, test_scores_mean, label = 'Test score')
        plt.ylabel('r2 score', fontsize = 14)
        plt.xlabel('Training set size', fontsize = 14)
        plt.title('Learning curves', fontsize = 18, y = 1.03)
        plt.legend()
        return
           
    
    