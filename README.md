# AI Dev Assistant

API REST con FastAPI para gestión de tareas. Proyecto pequeño que sirve como base para desarrollo asistido por IA con Claude Code.

## Qué es hoy

Una app FastAPI con un endpoint de tareas (CRUD básico), base de datos SQLite, estructura por capas y tests con pytest.

## Estructura

```
app/
  core/        → configuración
  db/          → sesión y engine (SQLAlchemy)
  models/      → ORM (SQLAlchemy)
  routers/     → endpoints HTTP
  schemas/     → modelos Pydantic (request/response)
  services/    → lógica de negocio
  main.py      → punto de entrada
tests/         → pytest
instructions/  → reglas adicionales para Claude Code
prompts/       → prompts reutilizables
specs/         → especificaciones previas al código
CLAUDE.md      → guía principal para la IA
```

## Quickstart

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest -q
```

## Preparado para IA

El repo incluye documentación estructurada para trabajo asistido por Claude Code:

- **`CLAUDE.md`** — guía principal: arquitectura, reglas de capas, qué puede tocar la IA, flujo de trabajo.
- **`instructions/`** — reglas adicionales o contexto específico que complementan `CLAUDE.md`.
- **`prompts/`** — prompts reutilizables para tareas frecuentes.
- **`specs/`** — especificaciones de requerimientos antes de escribir código.

El objetivo es que la IA tenga suficiente contexto para tomar decisiones correctas sin ambigüedad y sin necesidad de repetir las mismas instrucciones en cada sesión.
