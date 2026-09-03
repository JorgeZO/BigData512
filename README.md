# Big Data

Repositorio de prácticas y proyectos desarrollados durante la materia de **Big Data**.

## Descripción

Este repositorio reúne las prácticas, ejercicios y proyectos realizados durante el curso. Cada práctica se organiza como un proyecto de datos independiente, con sus propios datos, código y dependencias.

Git y GitHub permiten mantener un historial de cambios y sincronizar el trabajo en un repositorio remoto.

## Estructura del repositorio

Cada carpeta de práctica conserva una estructura similar a la siguiente:

```text
bigdata/
├── .git/                              # Control de versiones local de Git
├── .gitignore                         # Archivos y carpetas excluidos del repositorio
├── README.md                          # Documentación general del curso
├── U1_1_probabilidad_estadistica/
│   ├── .venv/                         # Entorno virtual local (no se sube a GitHub)
│   ├── requirements.txt               # Dependencias de Python de la práctica
│   ├── data/
│   │   ├── raw/                       # Datos originales
│   │   └── processed/                 # Datos transformados
│   ├── notebooks/                     # Jupyter Notebooks
│   │   └── 01_evolucion_poblacional.ipynb
│   ├── src/                           # Código Python reutilizable
│   └── README.md                      # Documentación de la práctica
├── U1_2_.../
└── U2_1_.../
```

## Reglas de organización

- Se utiliza un solo repositorio local de Git y un solo repositorio en GitHub para toda la materia.
- Cada práctica es un proyecto independiente dentro de su propia carpeta.
- Cada práctica tiene su propio entorno virtual (`.venv`) y su archivo `requirements.txt`.
- La carpeta `.venv` nunca se sube a GitHub; el entorno se puede reconstruir desde `requirements.txt`.
- Para trabajar en una práctica, abre su carpeta directamente en Visual Studio Code y activa el entorno virtual correspondiente.
- No ejecutes `git init` nuevamente al crear una práctica: el repositorio ya existe en la carpeta raíz.

## Configuración inicial de Git

Verifica que Git esté instalado y configura la identidad que aparecerá en los commits:

```bash
git --version
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@ejemplo.com"
```

Puedes comprobar la configuración con:

```bash
git config --global user.name
git config --global user.email
```

## Flujo de trabajo básico

Después de modificar archivos en una práctica, revisa, prepara, confirma y sincroniza los cambios:

```bash
git status
git add .
git commit -m "Describe el cambio realizado"
git push
```

Para consultar el historial de commits:

```bash
git log --oneline --graph --decorate
```

## Archivos ignorados

El archivo `.gitignore` debe excluir archivos locales y temporales, por ejemplo:

```gitignore
.DS_Store
.vscode/
**/.venv/
**/__pycache__/
**/.ipynb_checkpoints/
```

## Publicación en GitHub

El repositorio remoto se vincula una sola vez desde la carpeta raíz:

```bash
git remote add origin https://github.com/JorgeZO/BigData512.git
git push -u origin main
```

Después del primer envío, normalmente será suficiente ejecutar `git push` para publicar los nuevos commits.
