## Yaml Basic rules

```
* Space characters is used for intentation 

* Do not use Tab for intentation

* Yaml should be start with three dashes and end with three dots (But it is not mandatory)

* It is key value pair based

* Symbol '-' is used to list the items
```

## Yaml Basic syntax

```
---
# Employee records
- Mahi:
    name: Mahendran
    job: DevOps
    skills:
      - Jenkins
      - Ansible
      - Shell
- Jay:
    name: Jay
    job: Developer
    skills:
      - Java
      - Dotnet
      - Js
...
```

## Ansible Yaml Structure

![image](https://user-images.githubusercontent.com/96326288/210500895-ad2c3c5b-7cad-4183-b20d-42e43bb286a5.png)


## Ansible Yaml Syntax

```
---
- name: Update web servers
  hosts: webservers
  remote_user: root

  tasks:
  - name: Ensure apache is at the latest version
    yum:
      name: httpd
      state: latest

- name: Update db servers
  hosts: databases
  remote_user: root

  tasks:
  - name: Ensure postgresql is at the latest version
    yum:
      name: postgresql
      state: latest
  - name: Ensure that postgresql is started
    service:
      name: postgresql
      state: started
```

## Verify ansible playbook syntax

```
ansible-playbook --syntax-check <yaml file>
```

## Run ansible playbook 

```
ansible-playbook <yaml file>
```
