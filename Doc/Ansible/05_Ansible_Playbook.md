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
