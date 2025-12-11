# SyMoNeuRaL Docker Bundle

This ZIP contains a working Docker environment for the SyMoNeuRaL backend + Caddy reverse proxy.

## Files
- **Dockerfile** — builds FastAPI backend container  
- **docker-compose.yml** — orchestrates backend + Caddy  
- **Caddyfile** — HTTPS reverse proxy (using Caddy's internal TLS)  
- **.dockerignore** — prevents unnecessary files from entering the image  

## Usage
### Build + Run
```
docker compose up --build -d
```

### Access
- Backend API → https://localhost  
- Uvicorn backend → http://localhost:8000  

Perfect for local dev + production testing.
