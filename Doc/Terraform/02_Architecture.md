## Architecture of Terraform
* Terraform Core
  
* Providers
  
* State file

![image](https://github.com/user-attachments/assets/5da053a0-0930-41c7-9d7d-2a1297c6a725)

## Terraform Core
Terraform’s core (also known as Terraform CLI) is built on a statically-compiled binary that’s developed using the Go programming language.

###### Responsibilities of terraform Core
* Infrastructure as code: reading and interpolating configuration files and modules
  
* Resource state management
  
* Plan execution
  
* Construction of the Resource Graph
  
* Terraform Core uses remote procedure calls (RPC) to communicate with Terraform Plugins, and offers multiple ways to discover and load plugins to use

#### Providers
Providers are the plugins that Terraform uses to interact with various infrastructure services.
Each provider knows how to communicate with a specific set of APIs (e.g., AWS, Azure, Google Cloud, Docker, etc.).

###### Common examples of providers include:
* AWS Provider: For managing resources on Amazon Web Services
* Azure Provider: For deploying and managing resources in Microsoft Azure
* Google Cloud Provider: For controlling resources on the Google Cloud Platform

#### State file
Terraform state is a critical component of Terraform that records or track all the metadata and configurations of the infrastructure managed by Terraform. The state file is usually named **terraform.tfstate**

#### Provisioner
* Provisioners in Terraform are used to execute scripts or actions on local or remote machines as part of the resource creation or destruction process. 

* Their primary purpose is to allow for the execution of additional steps that Terraform's resource providers cannot handle directly, such as bootstrapping software or performing cleanup tasks.

###### There are two main types of provisioners: 
* **Local provisioners** execute commands on the machine running Terraform, which is typically used for tasks that prepare or modify local files or data.
  
* **Remote provisioners** run commands on the provisioned infrastructure itself. 
