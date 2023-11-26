#### Inclusion examples
installation.yaml
```
---
- name: Install {{ PackageName}} 
   yum:
    name: "{{ PackageName}}"
    state: present
    
- name: Service is {{ ServiceName }}
   service:
    name: "{{ ServiceName }}"
    state: "{{ ServiceState }}"
 ...
```
mainExecution.yaml
```
---
- name: Install Software
  hosts: webservers 
  tasks:
    - name: Install software
      Include: installation.yaml
       vars:
        PackageName: httpd
        ServiceName: httpd
        ServiceState: started
       register: captureOutput
    - name: Display Installation output
      debug:
       msg: "{{ captureOutput }}"  
...
```
