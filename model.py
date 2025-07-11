import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

class BookRecommender:
    def __init__(self, df):
        self.df = df
        self.tfidf = TfidfVectorizer(stop_words='english')
        # Combine title, author, genre, and description for better recommendations
        self.book_features = self.tfidf.fit_transform(
            self.df['title'] + ' ' + 
            self.df['author'] + ' ' + 
            self.df['genre'] + ' ' + 
            self.df['description']
        )
        self.model = NearestNeighbors(metric='cosine', algorithm='brute')
        self.model.fit(self.book_features)

    def recommend(self, book_title, n=5):
        idx = self.df[self.df['title'].str.lower() == book_title.lower()].index
        if len(idx) == 0:
            return []
        idx = idx[0]
        n_neighbors = min(n+1, len(self.df))
        distances, indices = self.model.kneighbors(self.book_features[idx], n_neighbors=n_neighbors)
        rec_indices = indices.flatten()[1:]  # Skip the first one as it's the input book
        return self.df.iloc[rec_indices][
            ['title', 'author', 'genre', 'publication_year', 'publisher', 'rating', 'description']
        ].values.tolist()
