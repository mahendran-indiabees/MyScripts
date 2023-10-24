#### What is Docker Network?
Docker networking is primarily used to establish communication between Docker containers and the outside world via the host machine where the Docker daemon is running

#### Types of Docker Network
Following are the types of Docker Networks:

* Bridge Networks
* Host Networks
* Overlay Networks
* Macvlan Networks
* None Networks

#### Bridge Networks
* The first type of Docker network is the “bridge” network.
* This is the default network that is made when Docker is installed. If you don't specify network driver, Docker will take default driver as bridge.
* The Bridge network assigns IPs in the range of 172.17.x.x to the containers within it. To access these containers from outside you need to map the ports of these containers to the ports on the host.
* It allows containers on the same host to communicate with each other using IP addresses and is ideal for most use cases.
* Each container on the network gets its unique IP address and can be accessed using this address or the container’s name.
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/7f73efc1-80d0-49e9-9e01-feb986299ff1)

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/c780865d-8cdb-4430-9199-bf891ef9527b)

#### Host Networks
* Unlike bridge networks, “host” networks allow containers direct access to the host network interface.
* Containers using host networks share the same network stack and IP address as the host, eliminating any encapsulation or isolation.
* For instance, if you run a container on port 5000, it will be accessible on the same port on the docker host without any explicit port mapping. The only downside of this approach is that you can not use the same port twice for any container.
* This type is beneficial for scenarios requiring high network performance or services that rely on specific ports being available on the host network.
* **Note:** One limitation with the host driver is that it doesn’t work on Docker desktop: you need a Linux host to use it.
  ![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/abe4cced-3f0c-4ac2-86e7-552566e7c37c)

#### None Networks
* Docker also provides a “none” network type, which essentially isolates a container from the network entirely. 
* Containers using this network type have no access to an external network or other containers. You can use it when you want to disable the networking on a container.
* This network is useful in certain security-sensitive scenarios, such as sandboxing or isolating a container that poses a potential threat.
  ![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/8907eb04-fb6b-4f02-adcf-66f4debcdbcc)

#### Overlay Networks
* The Overlay driver is for multi-host network communication. Overlay networks allow containers across multiple Docker hosts to communicate with each other.
* Overlay networks facilitate the creation of distributed applications and ensure container connectivity even in complex scenarios involving multiple hosts. This type is particularly suitable for distributed applications and scaling scenarios.
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/701dce1c-0d3d-44b1-8ce4-2cbe8e8ff347)

