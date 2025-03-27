import pandas as pd

class NetflixRecommender:
    def __init__(self):
        self.df = pd.read_csv('data/netflix_titles.csv')
        
    def get_similar_shows(self, show_title, n_recommendations=5):
        show_genres = self.df[self.df['title'] == show_title]['listed_in'].iloc[0]
        
        similar_shows = self.df[
            (self.df['listed_in'].str.contains(show_genres, na=False)) &
            (self.df['title'] != show_title)
        ].head(n_recommendations)
        
        return similar_shows[['title', 'type', 'listed_in', 'description']]
    
    def get_all_shows(self):
        return self.df['title'].tolist()
    
    def get_show_info(self, show_title):
        show = self.df[self.df['title'] == show_title].iloc[0]
        return {
            'title': show['title'],
            'type': show['type'],
            'genres': show['listed_in'],
            'description': show['description'],
            'year': show['release_year'],
            'rating': show['rating']
        } 