# Shopping App (Full Stack)

A complete e-commerce application with React frontend and Django REST Framework backend. Features user authentication, product catalog, shopping cart, and wishlist functionality.

## Quick Start with Docker

```bash
# Clone the repository
git clone https://github.com/NeeteshNG/Shopping-App-Api.git
cd Shopping-App-Api

# Copy environment file
cp .env.example .env

# Start the application
docker-compose up --build
```

Access the app:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

---

## Features

### Authentication
- Custom user model with email-based authentication
- User registration with OTP email verification
- Token-based authentication (DRF Token Auth)
- Secure login/logout endpoints

### E-commerce Functionality
- **Products** - Product catalog with images, pricing, and stock management
- **Cart** - Add to cart, update quantities, remove items
- **Wishlist** - Save favorite products for later

### API Endpoints

#### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/accounts/register/` | Register new user (sends OTP) |
| POST | `/api/accounts/verify-otp/` | Verify OTP and create account |
| POST | `/api/accounts/login/` | User login (returns token) |
| POST | `/api/accounts/logout/` | User logout (requires auth) |

#### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List all products |
| GET | `/api/products/<id>/` | Get product details |

#### Cart
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/cart/` | Get user's cart items |
| POST | `/api/cart/add/` | Add product to cart |
| PUT | `/api/cart/increment/<id>/` | Increase item quantity |
| PUT | `/api/cart/decrement/<id>/` | Decrease item quantity |
| DELETE | `/api/cart/remove/<id>/` | Remove item from cart |

#### Wishlist
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/wishlist/` | Get user's wishlist |
| POST | `/api/wishlist/` | Add product to wishlist |
| DELETE | `/api/wishlist/<id>/` | Remove from wishlist |

## Tech Stack

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - API toolkit
- **Token Authentication** - Secure API access
- **SQLite** - Database (development)
- **CORS Headers** - Cross-origin requests support
- **Gunicorn** - Production WSGI server

### Frontend
- **React 18** - UI library
- **Material-UI (MUI)** - Component library
- **React Router v6** - Client-side routing
- **Axios** - HTTP client
- **Redux Toolkit** - State management

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Frontend web server & reverse proxy

## Project Structure

```
Shopping-App-Api/
├── docker-compose.yml      # Docker orchestration
├── .env.example            # Environment variables template
├── frontend/               # React application
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── AppController.js
│       └── components/
└── backend_api/            # Django application
    ├── Dockerfile
    ├── requirements.txt
    ├── manage.py
    ├── backend_api/        # Project configuration
    │   ├── settings.py
    │   └── urls.py
    ├── accounts/           # User authentication
    ├── products/           # Product catalog
    ├── cart/               # Shopping cart
    └── wishlist/           # Wishlist feature
```

## Getting Started

### Option 1: Docker (Recommended)

Prerequisites: Docker and Docker Compose

```bash
# Clone and start
git clone https://github.com/NeeteshNG/Shopping-App-Api.git
cd Shopping-App-Api
cp .env.example .env
docker-compose up --build
```

The database will be automatically seeded with **100 sample products** across 10 categories, each with multiple images.

### Option 2: Manual Setup

#### Prerequisites
- Python 3.8+
- Node.js 18+
- pip & npm

#### Backend Installation

```bash
# Clone the repository
git clone https://github.com/NeeteshNG/Shopping-App-Api.git

# Navigate to project directory
cd Shopping-App-Api/backend_api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django djangorestframework django-cors-headers

# Run migrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

The API will be available at `http://localhost:8000`

```bash
# Seed database with sample products (optional)
python manage.py seed_products
```

#### Frontend Installation

```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install

# Start development server
npm start
```

The frontend will be available at `http://localhost:3000`

### Email Configuration (for OTP)

Update `settings.py` with your email configuration:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Django debug mode | `True` |
| `SECRET_KEY` | Django secret key | Auto-generated |
| `ALLOWED_HOSTS` | Allowed hosts | `*` |
| `EMAIL_HOST_USER` | Gmail address for OTP | - |
| `EMAIL_HOST_PASSWORD` | Gmail app password | - |
| `REACT_APP_API_URL` | Backend API URL (for dev) | `http://127.0.0.1:8000` |

## Author

**Neetesh Gupta**

- GitHub: [@NeeteshNG](https://github.com/NeeteshNG)
- LinkedIn: [neetesh-gupta](https://linkedin.com/in/neetesh-gupta)

## License

This project is open source and available under the [MIT License](LICENSE).
