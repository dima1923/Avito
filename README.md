### Welcome to Avito Chats Project
To run the project, you need to have Docker and Docker Compose installed.
Once Docker and Docker Compose is installed, run the following command:

```
$ cd Avito
$ docker-compose up
```

To start the containers in demon mode, use the following command instead:
```
$ docker-compose up -d
```

### Project Architecture
There are two Docker containers linked with each other in this project:
1. web (for django files) 
2. db (for postgresql database)
When you run _docker-compose up_, it builds these containers from **Dockerfile**, links them, installs the dependancies and starts the django apps.

### Author
Dmitrii Shchedrin (@dima1923)
