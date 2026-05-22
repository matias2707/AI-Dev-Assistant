# Specs

Especificaciones de requerimientos previas a la escritura de código.

## Qué va aquí

Documentos breves que describen qué se quiere construir antes de pedirle a la IA que lo implemente. Reducen la ambigüedad y evitan iteraciones innecesarias.

## Estructura recomendada para una spec

```markdown
## Nombre del feature

**Qué hace:** descripción en una oración.
**Endpoint(s):** método y ruta (ej: `POST /tasks/{id}/complete`)
**Input:** campos esperados con tipos
**Output:** shape de la respuesta
**Reglas de negocio:** validaciones o restricciones
**No incluye:** qué queda fuera del scope
```

## Cómo usarlas

1. Crear el archivo antes de abrir una sesión con la IA.
2. Referenciar el archivo en el prompt: "implementa según `specs/nombre.md`".
3. Una vez implementado, marcar la spec como completa o archivarla.
