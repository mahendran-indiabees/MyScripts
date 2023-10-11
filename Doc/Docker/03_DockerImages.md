#### What is Docker Images?

* A Docker image is an immutable (unchangeable) file that contains the source code, libraries, dependencies, tools, and other files needed for an application to run.

* Docker image informs how a container should instantiate, determining which software components will run and how. Docker images are platform-independent.


![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/cee9edc9-4bf4-4053-a7d1-3b95a51a9f72)

#### To check Docker Images
```
docker images
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/5daaa29d-4e58-4cb1-a214-e2ca67566b82)

#### To check Docker Image commands
```
docker image
```

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/2751d9ae-74d9-4e02-a8dc-5a8da33533a0)


#### To Run Docker Images in container with Port

```
docker run -it --name <myapp> -p <Docker Host port>:<container port> <Image Name>

docker run -it --name myApp -p 8080:80 httpd
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/2c821e9d-482e-4868-b203-c41f51a1f6da)

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/72dee180-be31-4f6e-a761-1e18183d8ab8)
#### To Check Port forwarding

```
docker ps -a
```

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/00e39839-41ef-408f-b529-2d6532405053)

#### How to find exposed port in docker image

```
docker inpsect <imageName>
docker inpsect httpd
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/0117edb9-b5af-45ce-9ee5-5ec4118d1594)

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/4bfbef3d-6b86-4b2e-b351-675e2455a34d)

#### How to export / save image in tar file
```
docker save <image id> > myname.tar
docker save 87t3evveu8e3 > myname_v.0.0.1.tar
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/b40b15a5-37b7-4c73-9d9f-27dd98ca33e9)

#### How to Import image using tar file
```
docker load -i <tar file>
docker load -i myname_v.0.0.1.tar
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/e87e6c7e-fc1e-401f-adcb-ddbf9429387d)

#### How to remove docker images
```
docker rmi <image id>
docker rmi 997bgb87t22
```
```
Note: Before remove docker image, we need to do below steps
a) First, we have to check whether any container is using our docker image or not.
b) If any container is using docker image means, we need to stop the container first. Then we need to remove in docker
docker stop <container name>
docker rm <container name>
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/c7923153-6460-4e81-b9c3-4a22eea35690)

#### To get all docker images id and remove
```
docker rmi $(docker images -a -q)
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/509d854e-5e68-4f4e-ab0e-d7620290706d)

#### To Stop and pause the conatiner
```
docker stop <conatiner name>
docker pause <conatiner name>
```

* The main difference between the paused and stopped states is that the memory portion of the state is cleared when a container is stopped, whereas, in the paused state, its memory portion stays intact.

```
docker stop <container-id or container-name>
```

* When the above command is executed, the main container process receives a SIGTERM signal (by default), and after a grace period (default 10s as of writing), it receives a SIGKILLsignal.

* SIGTERM is the signal of termination. The intention is to kill the process, gracefully or not, but to first allow it a chance to clean up.
* SIGKILL is the kill signal. The only behaviour is to kill the process, immediately.
* SIGSTOP is the pause signal. The only behaviour is to pause the process


