Docker
===============================================================================

[TOC]

-------------------------------------------------------------------------------
# References

- Docker
  https://github.com/arun-gupta/oreilly-docker-book

- Docker Training
  http://training.play-with-docker.com/


_Docker Images_

- Alpine
  - https://www.alpinelinux.org/about/
  - https://wiki.alpinelinux.org/wiki/Docker


_Artikel_

- Alpine vs Debian, Ubuntu and others
  - https://www.turnkeylinux.org/blog/alpine-vs-debian
  - https://coderwall.com/p/s4ofoq/docker-why-i-prefer-alpine-as-base-instead-of-ubuntu
  - https://nickjanetakis.com/blog/the-3-biggest-wins-when-using-alpine-as-a-base-docker-image


-------------------------------------------------------------------------------
# Commands

## machine

Command                           | Description
--------------------------------- | -------------------------------------------
docker-machine start default      | docker vm start
docker-machine restart default    | docker vm restart
docker-machine stop default       | docker vm stop

## image

Command                           | Description
--------------------------------- | -------------------------------------------
docker images                     | show images in the local repository
docker run [image-id]             | start image latest
docker run [image-id]:[tag]       | start image with given tag
docker stop [image-id]            | stop image
docker rmi [image-id]             | delete images
docker rmi $(docker images –q)    | delete all images!

## docker compose
Command                         | Description
------------------------------- | ---------------------------------------------
docker-compose up -d            | start container from compose.yml (-d show logs)
docker-compose stop             | stop container from compose.yml 
docker-compose rm               | delete container from compose.yml
docker-compose down             | stop & delete container from compose.yml


## container

Command                           | Description
--------------------------------- | -------------------------------------------
docker ps                         | show running containers
docker ps -a                      | show running containers and stopped ones
docker stop [container-id]        | stop container
docker rm [container-id]          | remove container (must be stopped before)
docker rm $(docker ps –a –q)      | remove all containers! 
docker logs [id]                  | show log of the image's application
docker exec -it [id] bash         | open bash in running container

## misc

### build
```
docker build --tag=[docker-registry]/[image-name] 
Ein neues Docker-Image aus dem Docker-File in . bauen
```

### cleanup
```
Docker aufrich bei Fehlermeldungen wie  z.Bsp. no space left on device
docker volume rm $(docker volume ls -qf dangling=true)
 docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```

### edit file on running container 
```
Files im laufenden Container editieren (z.Bsp. standalone.xml)

ssh in Docker Maschine: docker-machine ssh default
die Container id herausfinden: docker ps -a
ssh in Container: sudo docker exec -i -t bfdc962ca67a /bin/bash
Man kann jetzt die gewohnten Verzeichnisse von JBoss sehen und die Files können mit vi bearbeitet werden
```


-------------------------------------------------------------------------------
# Intro  

## Basics 1 - Run some simple Docker containers

### Run a single command (hostname) in the 'alpine linux container'
```
docker container run alpine hostname
```

- Containers which do one task and then exit can be very useful.
- You could build a Docker image that executes a script to configure something.
- Anyone can execute that task just by running the container - they don’t need the actual scripts or configuration information.


### List all containers
```
docker container list --all
```

### Run an interactive Ubuntu container
```
docker container run --interactive --tty --rm ubuntu bash
```
> Parameters:
--interactive says you want an interactive session.
--tty allocates a psuedo-tty.
--rm tells Docker to go ahead and remove the container when it’s done executing.

Run some commands:
Command                       | Description
----------------------------- | -----------------------------------------------
- ls /                        | list root directory content)
- ps aux                      | show running processes
- cat /etc/issue              | show upuntu version
- exit                        | exit shell

- You can commit a container to make an image from it - but you should avoid that wherever possible.
- It’s much better to use a repeatable Dockerfile to build your image. You’ll see that shortly.

-------------------------------------------------------------------------------
# TODO

- Current http://training.play-with-docker.com/beginner-linux/
- Developer Training     http://training.play-with-docker.com/
- Administrator Training http://training.play-with-docker.com/




-------------------------------------------------------------------------------
_The end._
