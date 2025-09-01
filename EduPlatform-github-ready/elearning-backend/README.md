# EduPlatform - Backend (Flask)

## Como rodar (dev)
```bash
cd elearning-backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m src.seed_data  # cria o banco e dados de exemplo
python -m src.main
```
A API sobe em `http://localhost:5000/api`.

## Build do Frontend
No projeto `elearning-frontend`:
```bash
npm i
npm run build
```
Copie a pasta `elearning-frontend/dist` para `elearning-backend/src/static/` (ou aponte o `static_folder` para ela).
