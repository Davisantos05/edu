# EduPlatform — Monorepo (Frontend + Backend)
Estrutura pronta para abrir no VS Code.

## Como rodar
### 1) Backend (API Flask)
```bash
cd elearning-backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m src.seed_data
python -m src.main
```
API em `http://localhost:5000/api`.

### 2) Frontend (React + Vite + Tailwind)
Em outro terminal:
```bash
cd elearning-frontend
npm i
npm run dev
```
Frontend em `http://localhost:5173` (usa `VITE_API_URL` do `.env.development`).

### 3) Build e servir pelo Flask (opcional)
```bash
cd elearning-frontend
npm run build
# copie dist/ para elearning-backend/src/static/
cp -r dist ../elearning-backend/src/static
```
Acesse `http://localhost:5000` para ver o SPA servido pelo backend.

## Observações
- Este projeto contém modal de autenticação simples (localStorage) e modal de compra chamando endpoints reais.
- Para produção, adicione autenticação com JWT e gateway de pagamento real (Stripe, PagSeguro).
