###### To get Ansible for CentOS 7, first ensure that the CentOS 7 EPEL repository is installed:

```
sudo yum install epel-release
```

######  Once the repository is installed, install Ansible with yum:

```
sudo yum install ansible
```
######  Check Ansible version:

```
ansible --version
```

![image](https://user-images.githubusercontent.com/96326288/210485342-51aa4906-d490-491e-a631-0a8530415532.png)


######  For our Understanding, Let assume we have below nodes


**master node**
ansmaster

**Agent nodes**
ansnode1
ansnode2
ansnode3
ansnode4

######  Edit `/etc/hosts` file in ansible master node and add all agent nodes entries

```
vi /etc/hosts
```

![image](https://user-images.githubusercontent.com/96326288/210486231-0b486b19-316b-48bd-bb5a-cf10faaaeafd.png)

######  Generate ssh key and copy public key to all agent nodes

```
ssh-keygen

cd ~/.ssh/

ssh-copy-id -i <user>@<agent host>
```

![image](https://user-images.githubusercontent.com/96326288/210486610-dffe7761-5e54-4a0d-925d-32a88dd9d7f6.png)



