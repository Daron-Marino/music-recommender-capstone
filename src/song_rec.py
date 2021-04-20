import numpy as np
import pandas as pd
from math import cos
import warnings
warnings.filterwarnings('ignore')


class Song_Rec():
    '''
    Takes in a song and returns the top n songs based on cosine distance
    '''
    def __init__(self,data):
        self.data=data
        
    def get_recommendations(self, song_name, n=5):
        distances = []
        
        song = self.data[self.data.index.str.lower() == song_name.lower()].values[0]
                
        comparisons = self.data[self.data.index.str.lower() != song_name.lower()]
        
        for track in comparisons.values:
            dist = 0
            for col in np.arange(len(comparisons.columns)):
                if not col in [1,10]:
                    
                    dist += np.absolute(cos(float(song[col])) - cos(float(track[col])))
                    
                    
            distances.append(dist)
        comparisons['distances'] = distances
        
        comparisons = comparisons.sort_values('distances')
        
        columns = ['artists']
        
        return comparisons[columns][:n]