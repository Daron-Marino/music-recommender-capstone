from sklearn.metrics import pairwise_distances
import pandas as pd
import numpy as np


class EuclideanItemRecommender():
    '''
    Content based item recommender
    '''
    def __init__(self, similarity_measure=pairwise_distances):
        self.similarity_matrix = None
        self.item_names = None
        self.similarity_measure = similarity_measure

    
    def fit(self, X, titles=None):
        
        if isinstance(X, pd.DataFrame):
            self.item_counts = X
            self.item_names = X.index
            self.similarity_df = pd.DataFrame(self.similarity_measure(X.values, X.values),
                 index = self.item_names)
        else:
            self.item_counts = X
            self.similarity_df = pd.DataFrame(self.similarity_measure(X, X),
                 index = titles)
            self.item_names = self.similarity_df.index

        
    def get_recommendations(self, item, n=5):

        return self.item_names[self.similarity_df.loc[item].values.argsort()[:n]].values[::]


    def get_user_profile(self, items):

        user_profile = np.zeros(self.item_counts.shape[1])
        for item in items:
            user_profile += self.item_counts.loc[item].values

        return user_profile


    def get_user_recommendation(self, items, n=5):

        num_items = len(items)
        user_profile = self.get_user_profile(items)

        user_sim =  self.similarity_measure(self.item_counts, user_profile.reshape(1,-1))

        return self.item_names[user_sim[:,0].argsort()[:(num_items+n)]].values[::]