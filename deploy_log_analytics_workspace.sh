#!/bin/bash

az group create --name RG-LogAnalytics --location eastus2
az deployment group create --resource-group RG-LogAnalytics --name la-jc-wsp --template-file deploylaworkspacetemplate.json