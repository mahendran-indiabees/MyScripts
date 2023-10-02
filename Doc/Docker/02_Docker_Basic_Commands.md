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
#### To get specific docker command applicable options 
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

#### To get the real time events from docker (If any issues docker, we can run this command to get real time events)
```
docker system events
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/11f38ed4-67dd-4fc9-8fd7-dac0071a39d3)

#### To remove all stopped container, to remove all dangling / orphanned images and Build cache , to all unused networks, we can use below command
```
docker system prune
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/4225fe34-699d-4dcc-a2b8-4bcfee485000)

#### To get resource utilization of docker
```
docker stats
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/fa0d5658-1381-4318-a085-57d6e3600630)

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
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/ce86a094-eec6-4b9d-b30f-53e405ab9597)

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/865af638-7f02-453a-8c5c-bce8aec864be)

###### Now we have downloaded two images, lets check disk usage of docker
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/de2541eb-2960-49ca-82ad-e4a38ef7e033)

#### To get running container alone
```
docker ps
```

#### To get all running & Stopped container
```
docker ps -a
```
