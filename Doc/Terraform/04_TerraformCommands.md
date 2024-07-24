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

## Terraform state:
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

# Terraform destroy
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

## terraform get
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
