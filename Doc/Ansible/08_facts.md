#### What is facts
* Variables related to remote systems are called facts.
* In Ansible, facts are the data collected from remote hosts that can be used by Ansible playbooks to make decisions. 
* These facts can be related to hardware, network, software, or any other information that can be queried from a remote host.

#### List all facts in remote system
In Adhoc Command Line
```
ansible myhostgroup -m setup
```
In Playbook
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
#### Get Specific facts from remote host
In Adhoc Command Line
```
ansible myhostgroup -m setup -a "filter=ansible_distribution"
ansible myhostgroup -m setup -a "filter=ansible_local"
ansible myhostgroup -m setup -a "filter=network"
```
In Playbook
```
---
- name: Print all available facts
  host: webserver
  gather_facts: true
  tasks:
   - name: Display Remote host facts OS
     debug:
     var: ansible_facts['distribution']
   - name: Display Remote host facts System info
     debug:
     var: ansible_facts['System']
   - name: Display Remote host facts IP
     debug:
     var: ansible_default_ipv4.address
...
```

#### How to know the data type of variable (or) fact
```
{{ <the variable name> | type_debug }}
{{ ansible_all_ipv4_addresses | type_debug }}
{{ ansible_architecture | type_debug }}
```
#### Magic Variables:
* Ansible provides a set of magic variables that allow you to access specific information about the remote systems and the Ansible environment.
* These variables are automatically set by Ansible and can be used in playbooks, templates, and scripts.

* **Note:** The most commonly used magic variables are hostvars, groups, group_names, and inventory_hostname.

hostvars is a magic variable that allows accessing all the variables defined for a particular host or group of hosts. The hostvars variable is a dictionary that contains all the variables defined for a specific host.
```
- name: Display a variable for a specific host
  debug:
    msg: "The IP address of {{ inventory_hostname }} is {{ hostvars[inventory_hostname]['ansible_host'] }}"
```

#### Disabling facts
```
- hosts: whatever
  gather_facts: false
```
#### Custom facts
* There are two types of custom facts: **data** and **code**. Data (Static content) is just read from a file, and code (small snippet) is executed and its output is accepted as data.
* Both facts are usually located in /etc/ansible/facts.d/ directory on the remote machine and both have extension of .fact (example: /etc/ansible/facts.d/date.fact).
```
- hosts: whatever
  gather_facts: false
```

#### Static custom facts:
Create a fact file in /etc/ansible/facts.d/mycustom.fact

mycustom.fact
```
{
"JAVA_JDK" : "REDHAT"
}
```
In Playbook
```
---
- name: Print all available facts
  host: webserver
  gather_facts: true
  tasks:
   - name: Display Remote host custom facts
     debug:
     msg: hostvars[InventoryHostname]['ansible_local']['JAVA_JDK']
...
```
#### Dynamic custom facts:
Create a fact file in /etc/ansible/facts.d/mycustom.fact

mycustom.fact
```
#!/bin/bash
DATE=`date`
echo "{\"date\" : \"${DATE}\"}"
```
In Playbook
```
---
- name: Print all available facts
  host: webserver
  gather_facts: true
  tasks:
   - name: Display Remote host custom facts
     debug:
     msg: hostvars[InventoryHostname]['ansible_local']['date']
...
```
