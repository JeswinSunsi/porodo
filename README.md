# PhoneMate - E-commerce Store

A full-stack e-commerce application with a FastAPI backend and Vue.js (Vite) frontend.

## Project Structure

```
ChanceCom/
├── main.py              # FastAPI backend
├── requirements.txt     # Python dependencies
├── frontend/            # Vue.js frontend
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── src/
│       ├── main.js
│       ├── App.vue
│       ├── router/
│       ├── stores/
│       ├── services/
│       ├── views/
│       └── components/
└── *.html               # Original HTML templates (reference)
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`
   API documentation at `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

   The Vue app will be available at `http://localhost:3000`

## Features

- **Home Page**: Hero carousel, featured products, trust badges, reviews
- **Product Page**: Product details, image gallery, color selection, add to cart
- **Cart Page**: Cart management, quantity updates, order summary

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/products` | Get all products |
| GET | `/products/{id}` | Get product by ID |
| GET | `/home/products` | Get trending products |
| GET | `/reviews` | Get customer reviews |
| GET | `/promotions` | Get active promotions |

## Tech Stack

### Backend
- FastAPI
- Pydantic
- Uvicorn

### Frontend
- Vue 3 (Composition API)
- Vite
- Vue Router
- Pinia (State Management)
- Tailwind CSS
- Axios

## Development

The Vite dev server is configured to proxy `/api` requests to the FastAPI backend at `http://localhost:8000`, so you can run both servers simultaneously during development.
