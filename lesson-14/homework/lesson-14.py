#Task: JSON Parsing
#write a Python script that reads the students.jon JSON file and prints details of each student.
with open(file_path, 'r') as file:
            students = json.load(file)
  for student in students['students']:
    print(student)

# ask: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import requests
city='Tashkent'

API_KEY='bc4d19fc780a22d76079836e0d982290'
units='metric'

url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}'
response=requests.get(url)
my_data=response.json()
    

temperature=my_data['main']['temp']
feels_like=my_data['main']['feels_like']
city_name=my_data['name']
wind_speed=my_data['wind']['speed']
print(f'In {city} the temperature is {temperature} but it feels like {feels_like}')

#Task: JSON Modification
#Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.

import json
import os

BOOKS_FILE = 'books.json'

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()
    book_id = int(input("Enter book ID: "))
    if any(book['id'] == book_id for book in books):
        print("Book with this ID already exists.")
        return

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter year of publication: ")

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": int(year)
    }
    books.append(new_book)
    save_books(books)
    print("Book added successfully.")

def update_book():
    books = load_books()
    book_id = int(input("Enter the ID of the book to update: "))
    for book in books:
        if book['id'] == book_id:
            print(f"Current title: {book['title']}")
            book['title'] = input("Enter new title (leave blank to keep current): ") or book['title']
            print(f"Current author: {book['author']}")
            book['author'] = input("Enter new author (leave blank to keep current): ") or book['author']
            print(f"Current year: {book['year']}")
            new_year = input("Enter new year (leave blank to keep current): ")
            if new_year:
                book['year'] = int(new_year)
            save_books(books)
            print("Book updated successfully.")
            return
    print("Book not found.")

def delete_book():
    books = load_books()
    book_id = int(input("Enter the ID of the book to delete: "))
    new_books = [book for book in books if book['id'] != book_id]
    if len(new_books) == len(books):
        print("Book not found.")
    else:
        save_books(new_books)
        print("Book deleted successfully.")

def list_books():
    books = load_books()
    if not books:
        print("No books found.")
        return
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

def main():
    while True:
        print("\nBook Manager")
        print("1. List all books")
        print("2. Add a new book")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
#4.Task: Movie Recommendation System
#Use this url http://www.omdbapi.com/ to fetch information about movies.
#Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random

OMDB_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OMDb API key
OMDB_URL = "http://www.omdbapi.com/"

# A predefined collection of popular movies by genre
MOVIE_POOL = {
    "action": ["Mad Max: Fury Road", "Die Hard", "John Wick", "Gladiator", "The Dark Knight"],
    "comedy": ["The Hangover", "Superbad", "Step Brothers", "Groundhog Day", "Bridesmaids"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather", "Fight Club", "The Pursuit of Happyness"],
    "sci-fi": ["Inception", "The Matrix", "Interstellar", "Blade Runner", "Arrival"],
    "romance": ["Pride and Prejudice", "La La Land", "The Notebook", "Titanic", "Notting Hill"]
}

def fetch_movie_details(title):
    params = {
        "t": title,
        "apikey": OMDB_API_KEY
    }
    try:
        response = requests.get(OMDB_URL, params=params)
        data = response.json()
        if data.get("Response") == "True":
            return data
        else:
            print(f"Could not fetch movie: {title} - Reason: {data.get('Error')}")
            return None
    except Exception as e:
        print("Error connecting to OMDb API:", e)
        return None

def recommend_movie_by_genre(genre):
    genre = genre.lower()
    if genre not in MOVIE_POOL:
        print(f"Genre '{genre}' not found in our database.")
        print("Available genres:", ", ".join(MOVIE_POOL.keys()))
        return

    movies = MOVIE_POOL[genre]
    random.shuffle(movies)

    for title in movies:
        details = fetch_movie_details(title)
        if details and genre.capitalize() in details.get("Genre", ""):
            print("\n🎬 Movie Recommendation:")
            print(f"Title : {details['Title']}")
            print(f"Year  : {details['Year']}")
            print(f"Genre : {details['Genre']}")
            print(f"Plot  : {details['Plot']}")
            print(f"IMDB Rating: {details['imdbRating']}")
            return
    print("Couldn't find a movie in that genre from our list.")

def main():
    print("🎞️ Welcome to the Movie Recommender!")
    user_genre = input("Enter a genre (e.g., Action, Comedy, Drama, Sci-Fi, Romance): ").strip()
    recommend_movie_by_genre(user_genre)

if __name__ == "__main__":
    main()


    
