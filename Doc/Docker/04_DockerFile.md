#### What is Docker File?
A Docker File is a simple text file with instructions on how to build your images.
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/e40643cb-cfac-466d-b76c-a001aafe2fdc)

#### Syntax
```
# Comment
INSTRUCTION arguments
```
* Instructions can be given in lowercase or uppercase letters. But to differentiate from the instructions and arguments, we use uppercase letters.
* 
#### Dockerfile example:
```
#This is a sample Image 
FROM ubuntu 
MAINTAINER DEVOPS_TEAM 

RUN apt-get update 
RUN apt-get install –y nginx 
CMD [“echo”,”Image created”] 
```
#### FROM
* FROM instruction used to specify the valid docker image name. So specified Docker Image will be downloaded from docker hub registry if it is not exists locally.
```
FROM docker.io/centos:latest
FROM docker.io/centos:6
```

#### MAINTAINER
* MAINTAINER instruction is used to specify about the author who creates this new docker image for the support.
```
MAINTAINER Administrator
MAINTAINER admin @ learnitguide.net
MAINTAINER Devops Engineer(admin @ learnitguide.net)
```
#### LABEL
* LABEL instruction is used to specify metadata informations to an image. A LABEL is a key-value  pair.
```
LABEL "Application_Environment"="Development"
LABEL "Application_Support"="LearnITGuide.net Group"
```

#### EXPOSE
* EXPOSE instruction is used to inform about the network ports that the container listens on runtime. Docker uses this information to interconnect containers using links and to set up port redirection on docker host system.
```
EXPOSE 80 443
EXPOSE 80/tcp 8080/udp
```
#### ADD
* ADD instruction is used to copy files, directories and remote URL files to the destination (docker container) within the filesystem of the Docker Images. Add instruction also has two forms - Shell Form and Executable Form.

Shell Form - ADD src dest
```
ADD /root/testfile /data/
```
Executable Form - ADD ["src","dest"]
```
ADD /root/testfile /data/
```
* If the "src" argument is a compressed file (tar, gzip, bzip2, etc) then it will extract at the specified "dest" in the container's filesystem.

#### COPY
* COPY instruction is used to copy files, directories and remote URL files to the destination within the filesystem of the Docker Images. COPY instruction also has two forms - Shell Form and Executable Form.
```
COPY src dest
COPY /root/testfile /data/
(or)
COPY ["src","dest"]
COPY /root/testfile /data/
```
* If the "src" argument is a compressed file (tar, gzip, bzip2, etc), then it will copy exactly as a compressed file and will not extract.

#### RUN
* RUN instruction is used to executes any commands on top of the current image and this will create a new layer. RUN instruction has two forms - Shell Form and Executable Form.

```
RUN yum update
RUN systemctl start httpd

RUN ["yum","update"]
RUN ["systemctl","start","httpd"]
```
#### CMD
* CMD instruction is used to set a command to be executed when running a container. There must be only one CMD in a Dockerfile. If more than one CMD is listed, only the last CMD takes effect.
CMD instruction has two forms - Shell Form and Executable Form.

Shell form:
```
CMD ping google.com
CMD python myapplication.py
```

Executable form:
```
CMD ["ping","google.com"]
CMD ["python","myapplication.py"]
```

#### ENTRYPOINT
* ENTRYPOINT instruction is used to configure and run a container as an executable. ENTRYPOINT instruction also has two forms - Shell Form and Executable Form.

Shell form:
```
ENTRYPOINT ping google.com
ENTRYPOINT python myapplication.py
```
Executable form:
```
ENTRYPOINT ["ping","google.com"]
ENTRYPOINT ["python","myapplication.py"]
```

* If user specifies any arguments (commands) at the end of "docker run" command, the specified commands override the default in CMD instruction, But ENTRYPOINT instruction are not overwritten by the docker run command and ENTRYPOINT instruction will run as it is.

* So Docker CMD and ENTRYPOINT commands are used for same purpose, but both has some different functionality, refer this link to understand the differences between Docker CMD and ENTRYPOINT Command with examples.

#### VOLUME
* VOLUME instruction is used to create or mount a volume to the docker container from the docker host filesystem.

```
VOLUME /data
VOLUME /appdata:/appdata
```
#### USER
* USER instruction is used to set the username,group name, UID and GID for running subsequent commands. Else root user will be used.

```
USER webadmin
USER webadmin:webgroup
USER 1008
USER 1008:1200
```
#### WORKDIR
* WORKDIR instruction is used to set the working directory.

```
WORKDIR /app/
WORKDIR /java_dst/
```

#### ENV
* ENV instruction is used to set environment variables with key and value. Lets say, we want to set variables APP_DIR and app_version with the values /data and 2.0 respectively. These variables will be set during the image build also available after the container launched.

```
ENV APP_DIR /data/
ENV app_version 2.0
```

#### ARG
