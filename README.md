# Book Recommendation System

This project is a **Book Recommendation System** that suggests books based on user input. It uses precomputed similarity scores and provides a web-based user interface to deliver recommendations.

---

## Features

- **Homepage**:
  - Displays popular books with their titles, authors, ratings, and cover images.
- **Recommendation Page**:
  - Accepts a book title as input.
  - Provides recommendations for books similar to the input book.
- **Dynamic Content Rendering**:
  - Renders recommendations dynamically using Flask and Jinja2 templates.
- **Interactive UI**:
  - Designed using Bootstrap for responsiveness and visual appeal.

---

## Tech Stack

### Backend:
- Flask
- Python (NumPy, Pandas, Pickle for data handling)

### Frontend:
- HTML5, CSS3, Bootstrap
- Jinja2 (templating engine for Flask)

### Data:
- Preprocessed datasets stored as `popular.pkl`, `pt.pkl`, `books.pkl`, and `similarity_scores.pkl`.

---

## Prerequisites

1. Python 3.8+
2. Required Python libraries:
   - Flask
   - NumPy
   - Pandas

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

---

## Setup and Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/book-recommender.git
cd book-recommender
```

2. **Place data files:**
   - Ensure `popular.pkl`, `pt.pkl`, `books.pkl`, and `similarity_scores.pkl` are in the project root directory.

3. **Run the Flask app:**

```bash
python app.py
```

4. **Access the application:**
   - Open a web browser and navigate to `http://127.0.0.1:5000`.

---

## File Structure

```
book-recommender/
├── app.py               # Main application file
├── templates/
│   ├── index.html       # Homepage template
│   ├── recommend.html   # Recommendation page template
├── static/
│   ├── css/             # Stylesheets
│   ├── images/          # Placeholder or custom images
├── popular.pkl          # Popular books dataset
├── pt.pkl               # Pivot table dataset
├── books.pkl            # Books metadata
├── similarity_scores.pkl# Precomputed similarity scores
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── ...                  # Additional files or directories
```

---

## Usage

1. Visit the homepage to browse popular books.
2. Navigate to the recommendation page.
3. Enter a book title to get recommendations.
4. Enjoy your personalized reading list!

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.

---
