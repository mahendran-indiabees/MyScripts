###### Adhoc Syntax
```
ansible <host group name> -m <module name>
```
**For use Custom inventory file**
```
ansible <host group name> -i <custom Inventory> -m <module name>
```
###### Ping web servers only

```
ansible webserver -m ping 
```
![image](https://user-images.githubusercontent.com/96326288/210489066-5143e01e-da1f-44b8-9314-09b6e3af4ba7.png)

###### Ping all servers 
```
ansible -m ping all
```

###### List all servers 
```
ansible all --list-hosts
```

###### List specic group servers 
```
ansible --list-hosts webserver
```

###### Execute linux command in agent nodes 
```
ansible webserver -m command -a 'df -hk'
```

###### Execute shell command in all agent nodes
```
ansible webserver  -m shell -a "tail /var/log/messages | grep ansible-command | wc -l 
```

###### Install apache in agent nodes 
```
ansible webserver -m yum -a "name=httpd state=present"
```


###### Start service in agent anodes
```
ansible webserver -m service -a "name=httpd enabled=yes state=started"
```

###### Remove apache in agent nodes 
```
ansible webserver -m yum -a "name=httpd state=absent"
```

###### Create User in agent nodes
```
ansible webserver -m user -a "name={{username}} password={{ 'password' | password_hash('sha512') }}"
```

###### Create Directory in agent nodes
```
ansible webserver -m file -a "dest=/tmp/test mode=644 state=directory"
```

###### Delete Directory in agent nodes
```
ansible webserver -m file -a "dest=/tmp/test state=absent"
```

###### Copy files to agent nodes
```
ansible webserver -m copy -a "src=/etc/hosts dest=/tmp/hosts"
```

###### Fetch / donwload files from agent nodes
```
ansible webserver -m fetch -a "src=/etc/hosts dest=/root"
```

###### Get agent nodes details and filter specific info
```
ansible webserver -m setup -a "filter=ansible_distribution"
```

###### Get doc for moudules
```
ansible-doc yum
```
