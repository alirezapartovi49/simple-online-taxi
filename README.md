# Simple Online Taxi App

### A modern online taxi application built with FastAPI (Python), Vue.js (frontend), Valkey (Redis-compatible), and Docker. The backend uses Bun as the runtime, SQLAlchemy for ORM, and Alembic for database migrations.

## Features

- User authentication (login/registration)
- Ride request and tracking
- Ride history
- Driver management
- Auto cache updates
- Responsive Vue.js frontend
- FastAPI backend with repository pattern
- Dockerized deployment

## Technologies

**Backend:**

- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- Alembic (database migrations)
- Valkey (Redis-compatible in-memory data store)

**Frontend:**

- Vue.js 3 (frontend framework)
- Pinia (state management)
- Tailwind CSS (styling)
- TypeScript
- Bun (JavaScript runtime)

**Infrastructure:**

- Docker
- Docker Compose
- Nginx (reverse proxy)

## Getting Started

### Prerequisites

- Docker (20.10+)
- Docker Compose (2.0+)
- Bun (optional for local development)

### Running with Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/alirezapartovi49/simple-online-taxi.git
   cd simple-online-taxi
   ```

```

```

2. Start the services:

   ```bash
   docker-compose up --build
   ```

3. The application will be available at:
   - Frontend: http://localhost
   - Backend API: http://localhost/api
   - API docs: http://localhost/api/docs

### Local Development

**Backend:**
i used uv rye as dependency management tool
you can install it with this command in linux

```
curl -sSf https://rye.astral.sh/get | bash

```

1. Install Python dependencies:

   ```bash
   rye synk
   ```

2. Set up the database:

   ```bash
   rye run migrate
   ```

3. Run the backend:
   ```bash
   rye run dev
   ```

**Frontend:**

1. Navigate to the frontend directory:

   ```bash
   cd src/frontend
   ```

2. Install dependencies:

   ```bash
   bun install
   ```

3. Run the development server:
   ```bash
   bun run serve
   ```

## Database Migrations

To create a new migration:

```bash
rye run makemigrations
```

To apply migrations:

```bash
rye run migrate
```

## API Documentation

After starting the backend, API documentation will be available at:

- Swagger UI: http://localhost/api/docs

## Deployment

For production deployment:

1. Update `docker-compose.prod.yml` with your production settings
2. Run:
   ```bash
   docker-compose -f docker-compose.prod.yml up --build -d
   ```

```

```
