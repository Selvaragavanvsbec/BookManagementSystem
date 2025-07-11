import pandas as pd
from sqlalchemy import create_engine
import os

def setup_database():
    try:
        # Check if book_data.csv exists
        if not os.path.exists('book_data.csv'):
            print("Error: book_data.csv not found!")
            return False

        # Read sample data
        print("Reading book data...")
        df = pd.read_csv('book_data.csv')
        print(f"Found {len(df)} books in the dataset.")

        # Create SQLite database and save data
        print("Creating database...")
        engine = create_engine('sqlite:///books.db')
        df.to_sql('books', engine, if_exists='replace', index=False)

        # Verify the data was inserted
        verification_df = pd.read_sql('SELECT COUNT(*) as count FROM books', engine)
        count = verification_df['count'].iloc[0]
        
        if count == len(df):
            print(f"Success! Database created with {count} books.")
            return True
        else:
            print(f"Warning: Expected {len(df)} books but found {count} in database.")
            return False

    except Exception as e:
        print(f"Error setting up database: {str(e)}")
        return False

if __name__ == "__main__":
    success = setup_database()
    if success:
        print("Database setup completed successfully!")
    else:
        print("Database setup failed. Please check the error messages above.")

