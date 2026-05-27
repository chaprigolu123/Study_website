from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

QUOTE_API = "https://api.quotable.io/random"
WIKI_SUMMARY = "https://en.wikipedia.org/api/rest_v1/page/summary/{}"
OPENLIB_SEARCH = "https://openlibrary.org/search.json"

# Rich subject metadata for the home page
SUBJECTS = {
    "Mathematics": {
        "description": "From algebra to calculus — build strong problem-solving skills.",
        "key_topics": ["Algebra","Calculus","Geometry","Probability"],
        "resources": [
            {"name": "Khan Academy - Math", "url": "https://www.khanacademy.org/math"},
            {"name": "Paul's Online Math Notes", "url": "http://tutorial.math.lamar.edu/"}
        ]
    },
    "Physics": {
        "description": "Learn the laws that govern the universe with experiments and intuition.",
        "key_topics": ["Mechanics","Electromagnetism","Thermodynamics"],
        "resources": [
            {"name": "HyperPhysics", "url": "http://hyperphysics.phy-astr.gsu.edu/"},
            {"name": "Khan Academy - Physics", "url": "https://www.khanacademy.org/science/physics"}
        ]
    },
    "Biology": {
        "description": "Explore life from cells to ecosystems — great for lab and theory.",
        "key_topics": ["Cell Biology","Genetics","Ecology"],
        "resources": [
            {"name": "OpenStax Biology", "url": "https://openstax.org/details/books/biology-2e"},
            {"name": "Khan Academy - Biology", "url": "https://www.khanacademy.org/science/biology"}
        ]
    },
    "History": {
        "description": "Understand the past to make sense of the present — timelines and primary sources.",
        "key_topics": ["World History","Modern History","Primary Sources"],
        "resources": [
            {"name": "World History Encyclopedia", "url": "https://www.worldhistory.org/"},
            {"name": "Library of Congress", "url": "https://www.loc.gov/"}
        ]
    },
    "Computer Science": {
        "description": "Programming, data structures, and algorithms to build real projects.",
        "key_topics": ["Programming","Algorithms","Data Structures","Web Dev"],
        "resources": [
            {"name": "freeCodeCamp", "url": "https://www.freecodecamp.org/"},
            {"name": "CS50", "url": "https://cs50.harvard.edu/"}
        ]
    }
}


def get_quote():
    try:
        r = requests.get(QUOTE_API, timeout=5)
        if r.ok:
            data = r.json()
            return f'"{data.get("content")}" — {data.get("author")}'
    except Exception:
        pass
    return "Keep learning — small steps every day."


def wiki_summary(topic):
    try:
        r = requests.get(WIKI_SUMMARY.format(requests.utils.requote_uri(topic)), timeout=5)
        if r.ok:
            data = r.json()
            return data.get("extract") or data.get("title")
    except Exception:
        pass
    return None


def openlib_books(query, limit=5):
    try:
        r = requests.get(OPENLIB_SEARCH, params={"q": query, "limit": limit}, timeout=6)
        if r.ok:
            data = r.json()
            books = []
            for doc in data.get("docs", [])[:limit]:
                books.append({
                    "title": doc.get("title"),
                    "author": ", ".join(doc.get("author_name", [])[:2]) if doc.get("author_name") else "",
                    "cover_id": doc.get("cover_i")
                })
            return books
    except Exception:
        pass
    return []


@app.route('/')
def index():
    q = request.args.get('q', '')
    quote = get_quote()
    results = None
    books = []
    if q:
        results = wiki_summary(q)
        books = openlib_books(q)
    return render_template('index.html', quote=quote, results=results, books=books, query=q, subjects=SUBJECTS)


@app.route('/subject/<name>')
def subject(name):
    quote = get_quote()
    results = wiki_summary(name)
    books = openlib_books(name)
    subject_meta = SUBJECTS.get(name)
    return render_template('topic.html', quote=quote, results=results, books=books, topic=name, subject=subject_meta)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
