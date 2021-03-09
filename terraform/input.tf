# Azure GUIDS
variable "subscription_id" {}
variable "client_id" {}
variable "client_secret" {}
variable "tenant_id" {}

# Resource Group/Location
variable "location" {}
variable "resource_group" {}
variable "application_type" {}

# Network
variable "virtual_network_name" {}
variable "address_prefix_test" {}
variable "address_space" {}

# VM
variable "admin_username" {
  description = "The admin user name in the VM."
  default     = "udacity"
}

variable "packer_image" {
  description = "The ID of the image created by packer tool."
}

variable "public_key_path" {
  description = "Full path incl. filename to the public key."
}

