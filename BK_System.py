import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from model import BookRecommender

st.title("Book Recommendation System")

# Load data from database
engine = create_engine('sqlite:///books.db')
df = pd.read_sql('books', engine)

# Convert publication_year to integer
df['publication_year'] = pd.to_numeric(df['publication_year'], errors='coerce')

# Initialize recommender
recommender = BookRecommender(df)

# Sidebar filters
st.sidebar.header("Filters")
selected_genre = st.sidebar.selectbox("Select Genre:", ["All"] + sorted(df['genre'].unique().tolist()))
min_rating = st.sidebar.slider("Minimum Rating:", 0.0, 5.0, 0.0, 0.1)
min_year = st.sidebar.number_input("Minimum Publication Year:", min_value=1900, max_value=2024, value=1900)

# Filter books based on sidebar selections
filtered_df = df.copy()
if selected_genre != "All":
    filtered_df = filtered_df[filtered_df['genre'] == selected_genre]
filtered_df = filtered_df[filtered_df['rating'] >= min_rating]
filtered_df = filtered_df[filtered_df['publication_year'] >= min_year]

# Main content
book_list = filtered_df['title'].tolist()
book_choice = st.selectbox("Select a book you like:", book_list)

if st.button("Recommend"):
    recommendations = recommender.recommend(book_choice)
    if recommendations:
        st.write("Recommended Books:")
        for title, author, genre, year, publisher, rating, description in recommendations:
            st.write(f"**{title}** by {author}")
            st.write(f"Genre: {genre} | Year: {year} | Publisher: {publisher}")
            st.write(f"Rating: {rating}/5.0")
            st.write(f"Description: {description}")
            st.write("---")
    else:
        st.write("No recommendations found. Try another book.")

# Display book statistics
st.sidebar.header("Book Statistics")
st.sidebar.write(f"Total Books: {len(df)}")
st.sidebar.write(f"Average Rating: {df['rating'].mean():.2f}")
st.sidebar.write(f"Oldest Book: {df['publication_year'].min()}")
st.sidebar.write(f"Newest Book: {df['publication_year'].max()}")
