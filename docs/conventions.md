# Convenciones de Git para el proyecto

## Estructura de Ramas

Las ramas seguirán la estructura: `<TIPO>/[CODIGO-DE-ISSUE]<DESCRIPCION-DEL-BRANCH>`

El `CODIGO-DE-ISSUE` es el ID de Jira de la tarjeta asociada.

Los tipos de ramas y sus usos se clasifican de la siguiente manera

Tipo          | Ejemplo                                                      | Descripción
------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------
`feature`     | `feature/SNT-1-agregar-modelo-zona-segura`                | Nuevas características o mejoras que tienen impacto en el usuario
`fix`      | `fix/error-al-editar-variable-empresa`                    | Correcciones a bugs y errores 
`docs`        | `docs/guia-estilo-ramas`                                     | Nueva documentación de funcionalidades o mejoras de la existente
`refactor`    | `refactor/cambiar-nombre-funcion`                             | Cambios internos en el código que no tienen impacto para el usuario
`test`        | `test/agregar-test-servicios-firebase`                 | Agrega, corrige o mejora tests
`chore`       | `chore/agregar-libreria-x`                                          | Cambios al proceso de build y herramientas auxiliares

Todas las ramas deben salir y apuntar hacia `main`

## Mensajes de Commits

1. **Convención de Mensajes de Commit**

Los mensajes de commit deben ser claros y descriptivos, siguiendo el siguiente formato:
     ```<tipo>: <mensaje>```

2. **Tipos de Commits**
   - **feat**: Nueva característica (feature).
   - **fix**: Corrección de bug (bugfix).
   - **docs**: Cambios en la documentación.
   - **refactor**: Refactorización de código (ni corrección de bug ni adición de feature).
   - **test**: Añadir pruebas o corregir pruebas existentes.
   - **chore**: Cambios en la configuración del build o herramientas auxiliares.

3. **Ejemplos de Mensajes de Commit**
   - `feat: agregar funcionalidad de login`
   - `fix: corregir problema de carga de perfil de usuario`
   - `docs: actualizar instrucciones de instalación`

## Pull Requests (PRs)

1. **Creación de PR**
   - Todas las ramas deben pasar por un PR antes de ser fusionadas en `main`.

2. **Aprobación de PR**
   - Al menos una persona debe revisar y aprobar el PR antes de que pueda ser mergeado (a menos que sean cambios que no tendrán una mayor repercusión, utilizar el criterio).

3. **Descripción del PR**
   - Cada PR debe tener una descripción clara de los cambios realizados, el propósito del PR, y cualquier detalle relevante. En caso de haber cambios visuales, agregar un screenshot y si hay que probar alguna funcionalidad se recomienda agregar el paso a paso de cómo probarla para agilizar la revisión.

4. **Checklist para PRs**
   - Descripción clara de los cambios.
   - Incluir pruebas si es necesario.
   - Revisado y aprobado por al menos un revisor.

## Ejemplo de Proceso

1. **Crear una Rama de Feature**

   ```bash
   git checkout -b feature/login-feature main
   ```

2. **Realizar Commits**

    ```bash
    git commit -m "feat: agregar funcionalidad de login"
    ```

3. **Push y Crear PR**

    ```bash
    git push origin feature/login-feature
    ```

4. **Crear PR en GitHub**

    Seleccionar main como base y feature/login-feature como la rama de comparación.
Rellenar la descripción del PR y enviar para revisión.

5. **Revisión y Aprobación**

    Al menos una persona revisa y aprueba el PR.

6. **Merge del PR**

    Una vez aprobado, se puede hacer merge del PR en main.