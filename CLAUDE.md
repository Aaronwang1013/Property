# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Architecture

This is a full-stack property management application with a microservices architecture:

- **Frontend**: React + TypeScript + Vite application in `/frontend/`
- **Auth Service**: FastAPI Python backend in `/auth-service/` handling authentication
- **Property Service**: Planned service in `/property_track/` (work in progress)

### Key Components

**Frontend (`/frontend/`)**:
- React 19 with TypeScript
- Vite for build tooling
- React Router for navigation
- Headless UI components
- Pages: LoginPage, RegisterPage, LoginModal
- API layer in `src/api/auth.ts`

**Auth Service (`/auth-service/`)**:
- FastAPI application with JWT authentication
- PostgreSQL database with SQLAlchemy ORM
- Alembic for database migrations
- Pydantic for data validation
- CORS middleware for frontend integration
- API endpoints: `/api/v1/auth/`, `/api/v1/health/`
- OAuth2.0 support (partially implemented)

## Development Commands

### Frontend Development
```bash
cd frontend
npm install          # Install dependencies
npm run dev          # Start development server
npm run build        # Build for production
npm run lint         # Run ESLint
npm run preview      # Preview production build
```

### Auth Service Development
```bash
cd auth-service
poetry install       # Install Python dependencies (if using Poetry)
pip install -r requirements.txt  # Or use pip directly

# Database setup
alembic upgrade head  # Run database migrations

# Development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# With Docker
docker-compose up -d  # Start PostgreSQL and auth service
```

## Database Management

The auth service uses Alembic for database migrations:
- Migration files are in `/auth-service/alembic/versions/`
- Run `alembic upgrade head` to apply migrations
- Database configuration is in `auth-service/alembic.ini`

## Configuration

**Environment Variables**:
- Auth service requires `.env` file with database credentials, JWT settings, and CORS origins
- Multiple environment files supported: `.env`, `.env.dev`, `.env.docker`
- Frontend development server runs on port 3000 (default Vite)
- Auth service runs on port 8000

**Key Settings**:
- CORS origins configured for frontend-backend communication
- JWT authentication with configurable expiration
- PostgreSQL connection settings
- Health check endpoint at `/api/v1/health/`

## Development Workflow

1. Start PostgreSQL database (via Docker Compose or local installation)
2. Run auth service: `uvicorn app.main:app --reload`
3. Start frontend development server: `npm run dev`
4. Access frontend at `http://localhost:3000` (or configured port)
5. API available at `http://localhost:8000`

## Testing and Linting

- Frontend: Use `npm run lint` for ESLint checking
- TypeScript compilation: `npm run build` includes type checking
- No specific test commands configured yet

## Notes

- OAuth2.0 implementation is partially complete (commented out in main.py)
- Property tracking service is in early development
- Database migrations are set up and ready to use
- CORS is configured for local development