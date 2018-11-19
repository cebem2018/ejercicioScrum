## Ejercicio completo para practicar scrum y github



#Vamos a crear un proyecto en git usando la metodología scrum completa.

- El proyecto se va a alojar en GitHub
  - Se usará el workflow: Flujo de trabajo centralizado con gestor de integraciones 
    - Ver la diapositiva 137 Flujo de trabajo centralizado 
    - Existirá un repositorio centralizado en el que todos tendremos permisos de escritura.
    - Se optará por la técnica de rebase en lugar de merge
    - El gestor de integraciones (integrator) será el profe
    - Cada alumno desarrolla en una rama nueva que comiteará con pull-request al integrator (profe)
  - Para almacenar el product backlog con las historias de usuario se usará un "proyect" de GitHub, que hará las veces de tablero Scrum Taskboard (Kanban) ("To Do", "In Progress", and "Done")
    - Las tareas de cada historia de usuario las simularemos con checkboxes.
  - Para documentar todo el proceso usaremos una wiki de GitHub
- Se usará la metodología Scrum donde los roles serán:
  - Todos los alumnos serán Scrum Developers
  - Un alumno (cualquiera) hará también de Scrum Master
  - El profe hará de Product Owner
- Proyecto a desarrollar:
  - Para que el desarrollo sea sencillo y rápido, el trabajo de los alumnos consistirá en abrir el cuaderno python con el que estamos trabajando en clase, escoger algo que hayamos visto y hacer un pequeño ejemplo funcional.
  - Ese pequeño ejercicio en python se corresponderá con una historia de usuario.
  - Al Menos cada alumno tendrá que construir 3 historias de usuario (que estará dividida en tareas)

## Proceso

- Construcción del product backlog
  - Cada alumno rellenará en el "proyect" de github sus historia de usuario
  - Además cada historia de usuario se modelará como un issue de github
  - Se prioriza (por valor de negocio) cada historia de usuario (por el método MoSCow)
  - Se hace grooming de las historias de usuario (si procede)
- Planificación de la iteración (Sprint Planning)
  - Se harán 3 sprints (mínimo)
  - Se usarán los milestones de github para crear los sprints
  - Se decide qué historias de usuario se van a implementar en el primer sprint
  - Se estima por esfuerzo cada una de las historias de usuario
    - Se elige una historia de usuario como pivote
    - Se usará la técnica de scrum poker
    - Usar esta herramienta online https://scrumpoker.online/ 
  - Se asocia cada historia de usuario a un Scrum Developer
  - Se dividen las historias de usuario en tareas
    - Se estiman en horas cada tarea
  - Todos los días se hace una reunión Daily scrum
  - Para el siguimiento completo del proyecto Agil se usará www.zenhub.com 
- Ejecución de la iteración (Sprint)
  - Cada alumno se pone a codificar en python en su ordenador su historia de usuario
  - Puedes ir haciendo commits al repositorio centralizado de vez en cuando.
  - Tendrás que ir actualizando el tablero Scrum Taskboard (kanban)
- Obtención el artefacto Product increment
  - Al finalizar el sprint generamos una release
  - Se creará una release en github
- Demostración de los requisitos completados (Sprint Review)
  - Reunión al final de cada sprint
- Retrospectiva (Sprint Retrospective)
  - Reunión al final de cada sprint
- Refinamiento de la lista de requisitos y cambios en el proyecto (Refinament)
  - Vuelta a empezar en un nuevo sprint


