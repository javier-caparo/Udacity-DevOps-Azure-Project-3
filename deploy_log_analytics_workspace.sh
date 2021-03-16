#!/bin/bash

az deployment group create --resource-group RG-LogAnalytics --name test-log --template-file deploy_log_analytics_workspace.json