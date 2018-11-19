# Clonar el repositorio

git clone https://github.com/cebem2018/ejercicioScrum.git


# Actualizar los posibles cambios que se produzcan en el repositorio remoto

Nos posicionamos en la rama master
git checkout master
Actualizamos nuestro repositorio local con los cambios que pudieran existir en el repositorio remoto
git pull


# Como contribuir

Creamos una nueva rama y nos posicionamos en ella 33=numero del issue
git checkout -b 33NombreIssue
Trabajamos en los cambios realizando commits
code xxx.py
git add .
git commit -m "xxxx"

# pusheamos los cambios a remoto

Actualizamos las ramas de seguimiento remoto
git fetch origin
Cogemos nuestros nuevos commits, separarlos de la base actualizamos la rama local y aplicamos los commits encima de esos cambios.
git rebase origin/master
Subimos la rama a remoto
git push -u origin 33NombreIssue


# Creamos un pull-request
Accedemos a github y abrimos un pull request pulsando compare & pull request
- Asociamos el pull-request al issue correspondiente
- Como texto del mensaje del pull-request escribimos closes #33
Esperamos a que el gestor de integraciones acepte el cambio


# Actualizamos nuestro repositorio local con los nuevos cambios en master

git checkout master
Actualizamos el repositorio
git pull
Podemos borrar la rama, tanto en local como en remoto pulsando el botón en Github (Delete branch)
git branch -d 33NombreIssue
