#### Defining Variables
Variables can  be defined into three scopes
* **Global Scope:** This varables are defining in command line option or ansible configuration file
* **Host Scope:** This variables are defining in inventory file or hosts_var / groups_var directory
* **Play Scope:** This variables are defining in play area in playbook
**Note:** If variables are defined in multiple scopes, Global scope will take priority. [ Global > Host > Play ]
