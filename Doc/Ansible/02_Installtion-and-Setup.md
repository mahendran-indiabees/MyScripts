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

```
**master node**
ansmaster

**Agent nodes**
ansnode1
ansnode2
ansnode3
ansnode4
```


