# AI Dev Assistant — Claude Code Rules

## Propósito del proyecto

API REST construida con FastAPI para gestión de tareas. Proyecto pequeño usado como base para práctica de desarrollo asistido por IA. El objetivo es mantener el código limpio, testeable y coherente con la arquitectura definida aquí.

## Arquitectura actual

```
app/
  core/        → configuración de la app (settings, variables de entorno)
  db/          → sesión, engine, dependencias de SQLAlchemy
  models/      → modelos ORM (SQLAlchemy, definición de tablas)
  routers/     → endpoints HTTP, thin layer
  schemas/     → modelos Pydantic (request/response)
  services/    → lógica de negocio
  main.py      → punto de entrada FastAPI
tests/         → pytest, todos deben pasar antes de push
instructions/  → reglas adicionales para la IA
prompts/       → prompts reutilizables
specs/         → especificaciones de requerimientos
```

Base de datos: SQLite para desarrollo. Compatible con Docker.

## Reglas de capas

- `schemas/` → solo formas de datos (Pydantic). Sin lógica.
- `models/` → solo definición de tablas ORM. Sin lógica de negocio.
- `db/` → sesión, engine, `get_db`. No acceder a la DB desde routers directamente.
- `services/` → toda la lógica de negocio. Único punto que toca la DB.
- `routers/` → solo: validar input, llamar al service, devolver response.
- `core/` → configuración y constantes globales.

## Qué puede tocar la IA

Permitido sin restricciones:
- `app/schemas/` — agregar o modificar schemas
- `app/services/` — agregar o modificar lógica de negocio
- `app/routers/` — agregar endpoints nuevos (thin, sin lógica)
- `tests/` — agregar tests para endpoints nuevos
- `instructions/`, `prompts/`, `specs/` — documentación de IA
- `README.md`, `CLAUDE.md` — documentación

Permitido solo si es estrictamente necesario:
- `app/models/` — solo si se agrega una tabla nueva o campo requerido
- `app/db/` — solo si cambia la configuración de base de datos
- `app/core/config.py` — solo si se necesita una variable de configuración nueva

No tocar:
- `.claude/settings.local.json` — configuración local del entorno
- `.git/` — nunca
- `requirements.txt` — solo si se agrega una dependencia explícitamente solicitada

## Flujo recomendado de trabajo

1. Leer `specs/` si hay una spec para la tarea en curso.
2. Leer `instructions/` si hay reglas adicionales que apliquen.
3. Revisar los archivos existentes en las capas afectadas antes de escribir.
4. Escribir schema → service → router → test (en ese orden).
5. Ejecutar `pytest` antes de dar la tarea por completa.
6. No hacer commits si los tests no pasan (el pre-push hook lo bloquea de todas formas).

## Convención para cambios pequeños y seguros

- Un cambio = una responsabilidad. No mezclar features en el mismo bloque de trabajo.
- Preferir editar archivos existentes antes de crear nuevos.
- Si se necesita un archivo nuevo, seguir exactamente la misma estructura que los existentes del mismo tipo.
- Nunca agregar imports no usados ni código muerto.
- Mantener los tipos explícitos (Python typing).

## Testing y validación

- Comando: `pytest` (desde la raíz del proyecto)
- El pre-push hook corre pytest automáticamente; nada se sube si falla.
- Todo endpoint nuevo requiere al menos un test de happy path y uno de error.
- Los tests usan SQLite in-memory para aislamiento.
- No mockear la DB en tests; usar el override de `get_db` ya definido en `tests/test_tasks.py`.

## Docker

- Mantener compatibilidad con el setup de Docker existente.
- No agregar dependencias que rompan el build del contenedor.

## Código Style

- Usar snake_case.
- Funciones pequeñas y enfocadas.
- Preferir legibilidad sobre brevedad.

## Fase futura (no implementado aún)

Lo siguiente queda reservado para cuando el proyecto lo requiera explícitamente:
- Configuración MCP
- `agents/` y `skills/`
- Automatizaciones y hooks avanzados
- CI/CD pipelines
