#### What is facts
* Variables related to remote systems are called facts.
* In Ansible, facts are the data collected from remote hosts that can be used by Ansible playbooks to make decisions. 
* These facts can be related to hardware, network, software, or any other information that can be queried from a remote host.

#### List all facts in remote system
```
---
- name: Print all available facts
  host: webserver
  tasks:
   - name: Display Remote host facts
     debug:
     var: ansible_facts
...
```
