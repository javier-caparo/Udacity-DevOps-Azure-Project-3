#!/bin/bash

az group create --name RG-LogAnalytics --location eastus2
az deployment group create --resource-group RG-LogAnalytics --name test-log --template-file deploy_log_analytics_workspace.json