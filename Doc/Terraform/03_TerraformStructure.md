## Terraform Block
A Terraform block specifies the required providers that terraform needs in order to execute the script. This block also contains the source block that specifies from where terraform should download the provider and also the required version.

```
terraform { 
  required_providers { 
    azurerm = { 
      source  = "hashicorp/azurerm" 
      version = "=3.0.0" 
    } 
  } 
}
```


## Provider Block
* A provider block specifies the cloud provider and the API credentials required to connect to the provider’s services. It includes the provider name, version, access key, and secret key.

* For example, if you are using Azure as your service provider, it would look as follows:
  
```
provider "azurerm" {
  features {}
  subscription_id = "00000000-0000-0000-0000-000000000000"
  tenant_id = "11111111-1111-1111-1111-111111111111"
  client_id= "bsdhjdbsj-ddjbdkjb0-ddkb dkhb"
}
```

## Resource Block
* A resource block represents a particular resource in the cloud provider’s services. It includes the resource type, name, and configuration details.
  
* This is the main block that specifies the type of resource we are trying to deploy

```
resource "azurerm_resource_group" "example" { 
  name = "example" 
  location = "West Europe" 
}
```

## Data Block
* A data block is used to fetch data from the provider’s services, which can be used in resource blocks. It includes the data type and configuration details.

* This is used in scenarios where the resource is already deployed, and you would like to fetch the details of that resource.

```
data "azurerm_resource_group" "example" { 
  name = "existing" 
}
```

## Variable Block
A variable block is used to define input variables that are used in the Terraform configuration. It includes the variable name, type, and default value.

```
variable "resource_group_name" {
  default = "myTFResourceGroup"
}
```

## Output Block
An output block is used to define output values that are generated by the Terraform configuration. It includes the output name and value.

```
output "resource_group_id" {
  value = azurerm_resource_group.rg.id
}
```