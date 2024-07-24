## Terraform init
* The terraform init command is used to initialize a working directory containing Terraform configuration files

* It downloads the necessary provider plugins and sets up the backend configuration.

```
terraform init
```

## Terraform fmt
The terraform fmt command is used to align or restructure Terraform configuration files to a canonical format and style. 

```
terraform fmt
```

## Terraform validate
* The terraform validate command is used to validate the configuration in a directory and checks whether a configuration is syntactically valid.
  
* It is used for general verification of correctness of attribute names and value types.
  
```
terraform validate
```

## Terraform plan
* The terraform plan command is used to create an execution plan.
  
* It will not modify things in infrastructure
  
* This command is a convenient way to check whether the execution plan for a set of changes matches your expectations without making any changes to real resources or to the state.

```
terraform plan
```

## Terraform apply
* The terraform apply command is used to apply the changes required to reach the desired state of the configuration. 

* This Terraform apply will also write data to the terraform.tfstate file.

```
terraform apply
```

## Terraform graph
* The terraform graph command is used to generate a visual representation of either a configuration or execution plan. The output is in the DOT format, which can be used by GraphViz to generate charts.

```
terraform graph | dot -Tsvg > graph.svg
```

## Terraform output
* The terraform output command displays the outputs defined in your Terraform configuration.

```
terraform output
```


## Terraform show
* The terraform show command is used to provide human-readable output from a state or plan file

```
terraform show
```

## Terraform state
The terraform state command allows you to manage and inspect the Terraform state. It provides insights into the current state of your infrastructure.

```
terraform state list
terraform state show <ResourceType>.<ResourceName>
```

## Terraform taint
The terraform taint command marks a resource as tainted, forcing it to be destroyed and recreated on the next `terraform apply`.

```
terraform taint <ResourceType>.<ResourceName>
```

## Terraform untaint
The terraform taint command will unmarked a resource which we tainted

```
terraform untaint <ResourceType>.<ResourceName>
```

## Terraform destroy
The terraform destroy command destroys the infrastructure managed by your Terraform configuration. It removes all the resources that were created.

```
terraform destroy
```

## Terraform refresh
* The terraform refresh command updates Terraform's state file to match the actual state of the resources in the real world.
    
* This command ensures that Terraform's state file is accurate and up-to-date.
    
* When changes have been made to resources outside of Terraform and you need to update the Terraform state file to reflect these changes.

```
terraform refresh
```

## Terraform get
The `terraform get` command retrieves and updates any modules referenced in your Terraform configuration.

```
terraform get
```


## Terraform import
The `terraform import` command imports existing infrastructure into your Terraform state. It helps you manage resources that were not created using Terraform.

```
terraform import <ResourceType>.<ResourceName> <ResourceID>
```

## Terraform providers:
The `terraform providers` command lists the providers used in the current configuration and their version information.

```
terraform providers
```

## Terraform command with useful Arguments:

| **Commands**             | **Description** |
| :---------------- | :------ | 
| **terraform init -get-plugins=false** | Initialize the working directory, do not download plugins |
| **terraform init -migrate-state** | Reconfigure a backend, and attempt to migrate any existing state. This command is typically used when you have reconfigured your backend settings in your terraform configuration. |
| **terraform init -verify-plugins=false** | Initialize the working directory, do not verify plugins for Hashicorp signature |
| **terraform init -get-plugins=false** | Initialize the working directory, do not download plugins |
| **terraform plan -out=myplan.tfplan**  | Write the plan to *.tfplan file. This can be used for review the changes| 
| **terraform plan -target resourceName**  | Create a plan for a specific module or resource | 
| **terraform plan -replace resourceName**  | Force the plan to replace a specific resource | 
| **terraform plan -var keyName=value**  | Pass in a variable value in command line when run plan command | 
| **terraform plan -refresh-only** |  This command refreshes the state file by querying the provider to get the latest information about the existing infrastructure but does not perform any other actions such as creating, updating, or destroying resources. | 
| **terraform apply myplan.tfplan** | Create or update infrastructure using a specific plan file | 
| **terraform apply -target resourceName**  | Create or update a specific resource | 
| **terraform apply -replace resourceName**  | Force the replacement of a specific resource | 
| **terraform apply -auto-approve**  | Apply changes without having to interactively type ‘yes’ to the plan | 
| **terraform apply -var "keyName=value"**  | Pass in a variable value in command line when run apply command |
| **terraform apply -parallelism=int** | Specify the number of operations run in parallel |
| **terraform output -json**  | Show all output values in JSON format
| **terraform output (Name)** | Show a specific output value
| **terraform output -raw (name)** | Show a specific output value without quotes
