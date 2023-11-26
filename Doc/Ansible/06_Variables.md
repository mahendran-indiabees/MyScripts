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
###### a) b) Sample Playbook to get variable value
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
