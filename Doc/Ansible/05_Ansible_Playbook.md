## 1. How to check Disk space & free memory
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
