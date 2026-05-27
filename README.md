# StudyHub — Free Study Material for Students

A lightweight Flask web app that combines **free public APIs** (Wikipedia, Open Library, Quotable) to deliver study material, book suggestions, and curated learning resources for students.

## Features

- **Search for any topic** — get Wikipedia summaries and suggested books
- **Popular subjects** — explore Mathematics, Physics, Biology, History, Computer Science
- **Rich subject cards** — key topics, curated resources, and free learning links
- **Responsive design** — optimized for all devices (Bootstrap 5)
- **Production-ready** — configured for Vercel, Heroku, or Render

## Quick Start (Local)

### Prerequisites
- Python 3.8+

### Installation & Run

```bash
# Clone repo
git clone https://github.com/chaprigolu123/Study_website.git
cd Study_website

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

## Deployment

### Vercel (Recommended)

1. Install Vercel CLI:
```bash
npm i -g vercel
vercel login
```

2. Deploy:
```bash
cd Study_website
vercel
```

Vercel will auto-detect `vercel.json` and deploy using the Python builder.

### Heroku or Render

The `Procfile` is configured for any WSGI server:

```bash
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

Deploy normally and set environment variables as needed.

## Project Structure

```
.
├── app.py              # Flask app with subject metadata and API routes
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel deployment config
├── Procfile            # Server command for Heroku/Render
├── templates/          # Jinja2 HTML templates
│   ├── base.html       # Navigation and layout
│   ├── index.html      # Home page with subjects and search
│   └── topic.html      # Subject detail page
└── static/style.css    # Custom styles
```

## Free APIs Used

- **Quotable** (https://api.quotable.io) — Inspirational quotes
- **Wikipedia** (https://en.wikipedia.org/api/rest_v1) — Topic summaries
- **Open Library** (https://openlibrary.org/search.json) — Book suggestions

## License

MIT
study
