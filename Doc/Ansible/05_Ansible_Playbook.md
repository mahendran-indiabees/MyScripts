## 1. To check Disk space & free memory
```
---
- name: Check WebServer
  hosts: webservers
 
  tasks:
  - name: Check Disk Space
    command: "df -Th"

  - name: Check free memory
    command: "free -m"
...
```

## 2. To Install apache and start the service
```
---
- name: Install Apache in Web Servers
  hosts: webservers
  tasks:
    - name: httpd installed
      yum:
        name: httpd
        state: latest
    - name: custom index.html
      copy:
        dest: /var/www/html/index.html
        content: "My web page"
    - name: httpd service enabled
      service:
        name: httpd
        enabled: true
        state: started
...
```

## 3. To Use variables

```
---
- name: Install Apache in Web Servers
  hosts: webservers
  vars:
    apacheConfigfile: "/app/test/index.html"
  tasks:
    - name: Display dict values
      debug:
       msg: "{{ apacheConfigfile }}"

...
```

## 3. To Use dict variables

```
---
- name: Install Apache in Web Servers
  hosts: webservers
  vars:
   webhost_java:
    apacheConfigfile: "/app/test/index.html"
  tasks:
    - name: Display dict values
      debug:
       msg: "{{ webhost_java.apacheConfigfile }}"

...
```


## 3. To Use List variables

```
---
- name: Install Apache in Web Servers
  hosts: webservers
  vars:
   Technologies:
    - Java
    - Dotnet
    - Python
    
  tasks:
    - name: Display list values
      debug:
       msg: "{{ Technologies }}"
    - name: Display list first values
      debug:
       msg: "{{ Technologies.0 }}"
    - name: Display list Second values
      debug:
       msg: "{{ Technologies.1 }}"       
...
```

## 3. To Use external varibales files

**External var file structure**
```
---
APP_INSTALL_PATH: "/app/test"
SOURCE_PATH: "/app/test/1"
DEST_PATH: "/app/test/1"
User1:
 id: "100"
...
```
**Use external vars file in playbook**
```
---
- name: Install Apache in Web Servers
  hosts: webservers
  vars_files:
   - external_vars.yaml    
  tasks:
    - name: Display app path
      debug:
       msg: "{{ APP_INSTALL_PATH }}"
    - name: Display destination path
      debug:
       msg: "{{ DEST_PATH }}"
    - name: Display user values
      debug:
       msg: "{{ User1.id }}"       
...
```
