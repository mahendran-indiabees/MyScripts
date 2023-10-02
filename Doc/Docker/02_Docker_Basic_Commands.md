#### For Check version of Docker host and Docker Client
```
docker version
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/aa6408af-87e1-4ddf-ab00-e3eb793fcbfe)

#### For Check version of Docker (In Short)
```
docker -v
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/d61f8143-ef8e-432c-b9bf-faf537e27319)

#### To get all docker command option 
```
docker
```
#### To get specific docker command applicable options, we can  use help or man command
```
docker <command> help

(or)

man docker <command>
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/5aff9688-a49f-453c-a04c-3f9a0d7c20c6)

#### To get docker information (Like get Running,stopped,passed containers, get networks & drivers, etc...)
```
docker info
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/7679cc2b-0205-462a-8bfd-23e0d9fcc545)
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/9796befc-bba8-4c05-9de1-4e4c42c251eb)

#### To get the disk usage of docker
```
docker system df
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/35bed768-85ed-4eb0-8f6e-fa871424a73c)

#### To get the real time events from docker (If any issues in docker, we can run this command to get real time events)
```
docker system events
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/11f38ed4-67dd-4fc9-8fd7-dac0071a39d3)

#### To remove all stopped container, to remove all dangling / orphanned images and Build cache , to all remove unused networks, we can use below command
```
docker system prune
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/4225fe34-699d-4dcc-a2b8-4bcfee485000)

#### To get resource utilization of docker
```
docker stats
docker stats <container name / id>
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/fa0d5658-1381-4318-a085-57d6e3600630)

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/02702677-5b82-49f3-a2f2-3153d6122f8a)
```
docker top <container Name / id>
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/3ea52ab2-94f8-41c0-88c8-86ad63a4053e)


#### To Search specific image from Docker registry (Docker Hub) in command line
```
docker search <image Name>:<version>
docker search httpd:latest
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/ed47640d-f0d0-4a63-8bc3-dc2aeb8c0014)

#### To Pull image from Docker Registry
###### If you don't specify tag version, Docker will try to check tag name 'latest' in Docker Hub and pull it.
```
docker pull httpd:latest
docker pull httpd
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/ce86a094-eec6-4b9d-b30f-53e405ab9597)

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/865af638-7f02-453a-8c5c-bce8aec864be)

###### Now we have pulled two images, lets check disk usage of docker
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/de2541eb-2960-49ca-82ad-e4a38ef7e033)

#### To get running containers alone
```
docker ps
```

#### To get all running & Stopped containers
```
docker ps -a
```
#### To Create a container in docker.Below command will create containter only. It won't start / run
```
docker create -i -t --name <container Name> <image>
docker container create -i -t --name mywebapp httpd
```

#### To Create & run a container in docker, We can use below command
```
docker run -d --name <container Name>  -p <your VM port>:<docker port> <image>
docker run -d --name DevWebApp  -p 8001:80 httpd
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/a247d4ae-e995-4d78-bb3b-97d4868e721a)

#### To login into a container and execute some commands

###### Below command helps to allow interactive terminal with container.
```
docker exec -it <containter Name> <Command>
docker exec -it DevWebApp /bin/sh
docker exec -it DevWebApp /bin/bash
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/7be5fa29-ee67-4eea-945d-4e10bb8db6a9)

###### Below command helps to execute command in container without login into terminal.
```
docker exec <containter Name> <Command>
docker exec DevWebApp uname -a
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/a732c5fb-66b1-4b52-af46-3e11accda2fd)

#### To Copy a file from local machine to container
```
docker cp <your local file> <docker container id or name>:/<path>
docker cp test.txt 31233847488:/opt/mydest/
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/14d2c535-b909-454b-80d6-dbcd116f7641)

#### To Copy a file from container to local machine
```
docker cp  <docker container id or name>:/<path> <your local dest path>
docker cp mywebapp:/opt/mydest/ test.txt
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/acc6d06a-3ca3-4bc2-90ad-147dd0f19b7f)

#### To Start a stopped container
```
docker start <container id or name>
docker start mywebapp
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/b0086593-95be-4572-96ce-d4f4718c9a0e)

#### To remove a container, use below command
###### Before remove the container, we have to stop the container and we can remove it. This is safest way to remove container
```
docker stop <container id or name>
docker stop mywebapp
docker rm mywebapp
```
###### Use force option to remove running container
```
docker  rm -f  -<container id or name>
docker rm -f mywebapp
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/2238677e-acb3-48c4-81c5-722754f15fed)

#### To remove a image, use below command
```
docker  rmi <image Id>
```
#### To check specific container log
```
docker logs <container name or id>
docker logs mywebapp
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/e15063fb-18aa-48e7-bea4-db8d493330f3)

#### To start /run OS related images (alpine, ubuntu, etc...), we need to mention some additional shell command. Because, this is not application image like httpd.
```
docker run -d -it --name <container Name>  <image id> <shell command>
docker run -d -it --name lightweightOS alpine /bin/sh
docker run -d -it --name lightweightOS alpine ping google.com
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/c19b061c-e27e-45dc-b998-c3f8e46b4d8d)


