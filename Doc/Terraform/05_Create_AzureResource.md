## Create a Resource Group in Azure
```
terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "~>2.0"
    }
  }
  backend "azurerm" {
        resource_group_name  = "tfstate"
        storage_account_name = "tfstate-storage-account"
        container_name       = "tfstate"
        key                  = "terraform.tfstate"
    }
}

provider "azurerm" {
  subscription_id   = "<azure_subscription_id>"
  tenant_id         = "<azure_subscription_tenant_id>"
  client_id         = "<service_principal_appid>"
  client_secret     = "<service_principal_password>"
  
  features {}
}


resource "azurerm_resource_group" "state-demo-secure" {
  name     = "state-demo"
  location = "eastus"
}
```
