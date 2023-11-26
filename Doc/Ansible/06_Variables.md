#### Defining Variables
Variables can  be defined into three scopes
* **Global Scope:** This varables are defining in command line option or ansible configuration file
* **Host Scope:** This variables are defining in inventory file or hosts_var / groups_var directory
* **Play Scope:** This variables are defining in play area in playbook
  
**Note:** If variables are defined in multiple scopes, Global scope will take priority. [ Global > Host > Play ]

#### Global Scope variables
###### a) Pass variables from Ansible command
```
ansible-playbook myfile.yaml -e "BUILD_ID=12"
```
###### a) Sample Playbook to get variable value
```
---
- name: This is for get value from variables
  host: webservers
  tasks:
   - name: This is test
     debug:
      msg: "{{ BUILD_ID}}"
 ...
```
###### b) Pass JSON or Yaml file variables from Ansible command
```
ansible-playbook myfile.yaml -e @envs_var.json
ansible-playbook myfile.yaml -e @envs_var.yaml
```
###### b) Sample JSON file
```
{
"BUILD_ID":"12"
}
```
###### b) Sample Playbook to get variable value
```
---
- name: This is for get value from variables
  host: webservers
  tasks:
   - name: This is test
     debug:
      msg: "{{ BUILD_ID}}"
 ...
```


#### Play Scope variables
###### a) Sample Playbook for define variables using vars keyword
```
---
- name: This is for get value from variables
  host: webservers
  vars:
   BUILD_ID=12
  tasks:
   - name: This is test
     debug:
      msg: "{{ BUILD_ID}}"
 ...
```
###### b) Sample Playbook for define variables using dict
```
---
- name: This is for get value from variables
  host: webservers
  vars:
   Platform:
    Linux: "/app/workspace"
    windows: "c:\"
  tasks:
   - name: This is test
     debug:
      msg: "{{ Platform.Linux }}"
   - name: This is test1
     debug:
      msg: "{{ Platform['windows'] }}"
 ...
```
###### C) Sample Playbook for define variables using list
```
---
- name: This is for get value from variables
  host: webservers
  vars:
   Platform:
    - Linux
    - Windows
  tasks:
   - name: This is test
     debug:
      msg: "{{ Platform.0 }}"
   - name: This is test1
     debug:
      msg: "{{ Platform[1] }}"
 ...
```
###### d) Sample Playbook for define variables using inline list
```
---
- name: This is for get value from variables
  host: webservers
  vars:
   Platform:
    [ linux,windows ]
  tasks:
   - name: This is test
     debug:
      msg: "{{ Platform.0 }}"
   - name: This is test1
     debug:
      msg: "{{ Platform[1] }}"
 ...
```
###### d) Pass variables in external file json / yaml
external_vars.yaml
```
---
BUILD_ID=12
CUSTOM_DIR=/app/directoty
CUSTOM_PLATFORM
 Linux: bash
 windows: powsershell
...
```
```
---
- name: This is for get value from variables
  host: webservers
  vars_files:
   - external_vars.yaml
  tasks:
   - name: This is test
     debug:
      msg: "{{ BUILD_ID }}"
   - name: This is test1
     debug:
      msg: "{{ CUSTOM_PLATFORM['Linux'] }}"
 ...
```
#### Host Scope variables
###### a) define variables in Inventory file (hosts file)

a) Sample inventory file for individual host
```
LINUX01 ansible_ssh_host=10.100.1.2 ansible_port=22 http_port=80 https_port=443
LINUX02 ansible_ssh_host=10.100.1.3
```
```
- name: This is for get value from variables
  host: LINUX01
  tasks:
   - name: This is test
     debug:
      msg: "{{ hostvars[ansible_hostname]['https_port'] }}"
 ...
```
a) For avoid error if your host does not contains variable, please add default keyword
```
- name: This is for get value from variables
  host: LINUX02
  tasks:
   - name: This is test
     debug:
      msg: "{{ hostvars[ansible_hostname]['https_port'] | default('') }}"
 ...
```
b) Sample inventory file for groups
```
[webservers]
LINUX01 ansible_ssh_host=10.100.1.2
LINUX02 ansible_ssh_host=10.100.1.3

[webservers:vars]
https_port=9001
```

```
- name: This is for get value from variables
  host: webservers
  tasks:
   - name: This is test
     debug:
      msg: "{{ hostvars[ansible_hostname]['https_port'] }}"
 ...
```

c) Best pratcies : create group_vars/<group name> and host_vars/<hostname> in inventory file dirctory

Sample structure for group_vars and host_vars

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/ece9d305-a3a7-4b5b-9048-1d4fb6f5ed7e)

```
- name: This is for get value from variables
  host: webservers
  tasks:
   - name: This is test
     debug:
      msg: "{{ ['https_port'] }}"
 ...
```
