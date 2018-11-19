# Clonar el repositorio

```
git clone https://github.com/cebem2018/ejercicioScrum.git
```

# Actualizar los posibles cambios que se produzcan en el repositorio remoto
Esto lo haremos por ejemplo cada día al llegar al puesto de trabajo

Nos posicionamos en la rama master
```
git checkout master
```
Actualizamos nuestro repositorio local con los cambios que pudieran existir en el repositorio remoto
```
git pull
```

# Como contribuir con alguna nueva característica

Creamos una nueva rama y nos posicionamos en ella **33=numero del issue**
```
git checkout -b 33NombreIssue
```
Trabajamos en los cambios realizando commits
```
code xxx.py
git add .
git commit -m "xxxx"
```
# pusheamos los cambios a remoto

Actualizamos las ramas de seguimiento remoto
```
git fetch origin
```
Cogemos nuestros nuevos commits, separarlos de la base actualizamos la rama local y aplicamos los commits encima de esos cambios.
```
git rebase origin/master
```

> En caso de exitir algun conflicto:

> Abrimos el fichero xxxx.py y solucionamos el conflicto

> code xxxx.py

> Resolvemos el conflicto (normalmente hay que hablar con la persona con la hemos entrado en conflicto)

> git add xxxx.py

> git rebase --continue


Subimos la rama a remoto
```
git push -u origin 33NombreIssue
```


# Creamos un pull-request para que lo acepte el integrator (gestor de integraciones)
Accedemos a github y abrimos un pull request pulsando **compare & pull request**
- Asociamos el pull-request al issue correspondiente **connect with an issue**
- Opcional: Como texto del mensaje del pull-request escribimos __closes #33__ así conseguimos que cuando el integrator acepte el pull-request el issue se cierre automáticamente.
- Pulsamos el botón **create pull request**

Esperamos a que el gestor de integraciones/integrator (el profesor) acepte el cambio, ese mergueará los cambios en la rama master. También borrará la rama 33NombreIssue aunque tambine la puedes borrár tú con **git push origin :33NombreIssue**


# Cuando el itegrator acepte... Actualizamos nuestro repositorio local con los nuevos cambios en master
```
git checkout master
```
Actualizamos el repositorio
```
git pull
```
Podemos borrar la rama, tanto en local como en remoto pulsando el botón en Github (Delete branch)
```
git branch -d 33NombreIssue
```
