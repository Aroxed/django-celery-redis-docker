# Django Celery Redis WebSocket Example

This project demonstrates a Django application with Celery for background tasks, Redis for caching and message brokering, and WebSocket support using Django Channels. The application allows users to generate random numbers in real-time through WebSocket connections.

## Features

- Django web application with WebSocket support
- Celery for background task processing
- Redis for message brokering and caching
- Real-time updates using WebSockets
- Docker containerization with Docker Compose

## Prerequisites

- Docker
- Docker Compose

## Project Structure

```
.
├── core/                 # Django project settings
├── main/                 # Main application
│   ├── consumers.py      # WebSocket consumers
│   ├── tasks.py          # Celery tasks
│   └── templates/        # HTML templates
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile           # Docker configuration
└── requirements.txt     # Python dependencies
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/Aroxed/django-celery-redis-docker
cd django-celery-redis-docker
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. Access the application:
- Web interface: http://localhost:8000
- Redis: localhost:6379

## How It Works

1. User connects to the WebSocket endpoint
2. When the "Generate Random Number" button is clicked:
   - Frontend sends a WebSocket message
   - Backend triggers a Celery task
   - Celery generates a random number
   - Number is sent back to the frontend via WebSocket
   - Number is displayed on the page

## Services

- **web**: Django application with Daphne ASGI server
- **celery**: Celery worker for background tasks
- **redis**: Redis server for message brokering and caching

## Development

To make changes to the code:

1. Modify the files in your local environment
2. The changes will be reflected in the containers due to volume mounting
3. Restart the containers if needed:
```bash
docker-compose restart
```

## Environment Variables

- `REDIS_HOST`: Redis host (default: redis)
- `REDIS_PORT`: Redis port (default: 6379)
- `CELERY_BROKER_URL`: Celery broker URL (default: redis://redis:6379/0)
- `CELERY_RESULT_BACKEND`: Celery result backend URL (default: redis://redis:6379/0)

