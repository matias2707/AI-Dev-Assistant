# Prompts

Prompts reutilizables para tareas frecuentes con Claude Code.

## Qué va aquí

Prompts en markdown listos para copiar y pegar en sesiones con la IA. Sirven para estandarizar cómo se piden tareas comunes y evitar tener que reescribir contexto cada vez.

Ejemplos de archivos que podrían vivir aquí:
- `new-endpoint.md` — prompt para agregar un endpoint nuevo siguiendo la arquitectura
- `add-field.md` — prompt para agregar un campo a un modelo existente
- `review-service.md` — prompt para revisar la lógica de un service

## Cómo escribirlos

Un buen prompt reutilizable incluye:
1. Contexto mínimo necesario (qué capa, qué entidad)
2. Qué se quiere lograr
3. Restricciones que aplican (no tocar X, usar el patrón Y)
4. Qué se espera como output (schema, test, etc.)

Evitar prompts genéricos que la IA no pueda ejecutar sin adivinar contexto.
