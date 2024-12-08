import numpy as np
from flask import Flask, render_template, request
import pickle  # Ensure this import is present
import pandas as pd

# Load the pickle file correctly
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values),
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_book', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    if not user_input:
        return render_template('recommend.html', error="Please enter a book name")

    try:
        # Check if the book exists in the data
        if user_input not in pt.index:
            return render_template('recommend.html', error="Book not found. Please try again with a different title.")

        # Get the index of the input book
        index = np.where(pt.index == user_input)[0][0]

        # Get similar items
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)

        # Check if no data was found
        if not data:
            return render_template('recommend.html', error="No recommendations available for this book.")

        return render_template('recommend.html', data=data)

    except Exception as e:
        print(e)
        return render_template('recommend.html', error="An error occurred. Please try again later.")


if __name__ == "__main__":
    app.run(debug=True)
