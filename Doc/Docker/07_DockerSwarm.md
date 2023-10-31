#### What is Container Orchestration?
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/50da9a1a-3185-4279-9a08-bccad705653e)

#### Container Orchestration tools in Market place
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/219b5c70-0c9a-44c1-930b-929c55bd1a0a)

#### What is Docker Swarm?
* Docker swarm is a container orchestration tool, meaning that it allows the user to manage multiple containers deployed across multiple host machines.
  
* A Docker Swarm is a group of either physical or virtual machines that are running the Docker application and that have been configured to join together in a cluster.
  
* The activities of the cluster are controlled by a swarm manager, and machines that have joined the cluster are referred to as nodes.
  
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/ea586120-a50d-4fae-a3b8-8842892c67c3)

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/7d551158-dea7-434c-a71d-8d3d3b76e99a)

#### Benefits
* Availability and scaling
* Easy installation and setup
* Auto Load Balancing
* Rollback faatures
* Scaling
  
#### Initialize Docker Swarm
Run below command in master node. It will generate token for add worker node into manager node. We need to copy this token and run in worker nodes.
```
docker swarm init --advertise-addr <host ip>
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/9fe77193-13e6-4e7e-8e20-63203a495b0f)

**Note:** If you want to add another manager (For availability), You need to run below comamnd. Below command will generate token for add new manager node into our primary node.

```
docker swarm join-token manager
```
#### How to Join worker node into Manager node
Get the token from manager node and run "docker swarm join" command in worker
```
docker swarm join --token <token values and ip> 
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/30c7ac86-6b03-4ead-a73f-e8ea57c780bc)

#### List all docker swarm nodes
```
docker node ls
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/f1d1266d-d1bd-4ee4-9431-6360130fad42)

**Note**
Swarm related commands only execute in manger node. If we execute in worker node, you will get below error
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/67e01168-2c49-4fc0-a5cf-18718acc4fdf)

#### Docker service command Options
```
docker service --help
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/7fdbb794-b065-4c9f-97d6-2bb037e9f3de)

#### How to run image into container using docker service
```
docker service create --replicas <int> -p <manager host port>: <container port> --name <service name> <image name>
docker service create --replicas 5 -p 9001:80 --name mywebappservice httpd
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/2b5a1c5c-9353-4f3f-830b-7ea718e41163)

#### List docker services
```
docker service ls
```
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/3143930a-d30e-4764-b8f3-b0705321eb52)

#### How to find the nodes which my containers are running
```
docker service ps <service name>
```

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/0e06327d-6cd7-4f33-8cfe-273fb36ca04c)

