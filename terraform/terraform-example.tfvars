# Azure subscription vars
subscription_id = "to fill"
client_id       = "to fill"
client_secret   = "to fill"
tenant_id       = "to fill"

# Resource Group/Location
location         = "eastus2"
resource_group   = "RG-udacity_project3"
application_type = "to fill"

# Network
virtual_network_name = "to fill"
address_space        = ["10.5.0.0/16"]
address_prefix_test  = "10.5.1.0/24"

# VM
packer_image   = "to fill"
admin_username = "udacity"

# public key in azure pipelines
#public_key_path = "/home/vsts/work/_temp/myKey.pub"

# public key on Windows local machine
public_key_path = "~/.ssh/id_rsa.pub"