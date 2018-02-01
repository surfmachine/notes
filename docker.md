Docker
===============================================================================

[TOC]


-------------------------------------------------------------------------------
# TODO

- Current http://training.play-with-docker.com/beginner-linux/
- Developer Training     http://training.play-with-docker.com/
- Administrator Training http://training.play-with-docker.com/


-------------------------------------------------------------------------------
# Referenzen

## Dokumentation

- Docker
  https://github.com/arun-gupta/oreilly-docker-book

- Docker Training
  http://training.play-with-docker.com/

## Docker Images

- Alpine
  - https://www.alpinelinux.org/about/
  - https://wiki.alpinelinux.org/wiki/Docker

## Artikel

- Alpine vs Debian, Ubuntu and others
  - https://www.turnkeylinux.org/blog/alpine-vs-debian
  - https://coderwall.com/p/s4ofoq/docker-why-i-prefer-alpine-as-base-instead-of-ubuntu
  - https://nickjanetakis.com/blog/the-3-biggest-wins-when-using-alpine-as-a-base-docker-image


## Beispiele
==TODO==

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
# Commands

## docker images (show images, version and size)
```
docker images | awk '{print $1"\t"$2"\t"$7" "$8}'
```


## general

Command                       | Description
----------------------------- | -----------------------------------------------
                              |



-------------------------------------------------------------------------------
_The end._
