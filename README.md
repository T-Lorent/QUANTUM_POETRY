# QUANTUM_POETRY

## DEVELOPMENT

### Backend

#### A) First install

1. Create local server in backend folder: <kbd>python3 -m venv venv</kbd>
2. Type in command prompt from backend folder: <kbd>source venv/bin/activate</kbd>
3. Install Dependencies: <kbd>pip install -r requirements.txt</kbd>

### B) Run after install

1. Start backend: <kbd>export $(xargs <.env) && fastapi dev backend/app.py</kbd>

### Frontend

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```
