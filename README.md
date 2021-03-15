# Udacity-DevOps-Azure-Project-3 - Ensuring Quality Releases
CI / CD Test Automation Pipeline - Azure DevOps - Terraform - JMeter -Selenium - Postman


## Badges

[![Build Status](https://dev.azure.com/javiercaparo574/udacity-project-3/_apis/build/status/jfcb853.Udacity-DevOps-Azure-Project-3%20(2)?branchName=main)](https://dev.azure.com/javiercaparo574/udacity-project-3/_build/latest?definitionId=17&branchName=main)

## Intro

* To use  a variety of industry leading tools, especially Microsoft Azure, to create disposable test environments and run a variety of automated tests with the click of a button.

![intro.png](./images/intro.png)

## Dependencies
| Dependency | Link |
| ------ | ------ |
| Packer | |
| Terraform | https://www.terraform.io/downloads.html |
| JMeter |  https://jmeter.apache.org/download_jmeter.cgi|
| Postman | https://www.postman.com/downloads/ |
| Python | https://www.python.org/downloads/ |
| Selenium | https://sites.google.com/a/chromium.org/chromedriver/getting-started |
 

## Azure Resources
 - Azure Free account  
 - Azure Storage account (resource)
 - Azure Log Workspace (resource)
 - Terraform Service principle (resource)
 - Azure DevOps Organization ( https://azure.microsoft.com/en-us/services/devops/)
 - Azure CLI (resource)

## Steps

1. Clone this repo:

```sh
git clone https://github.com/jfcb853/Udacity-DevOps-Azure-Project-3
```

2. open a Terminal in VS Code and connect to your Azure Account and get the Subscription ID

```bash
az login 
az account list --output table
```

3. Configure storage account to Store Terraform state

* Execute the script **azure-storage-account.sh** :

```bash
./azure-storage-account.sh
```

* Take notes of **storage_account_name**, **container_name**, **access_key**

> storage_account_name: tstate3994
> container_name: tstate
> access_key: j/bg+StBWOPqf5fQCPF+tCLFeGURmKEnE675v4aVN1RzyUW3+wlFLrq/dTon4XPrCRKMl5/Z79qNRGR7ZHBPQw==

5. Create a Log Analytics workspace

```bash

```

4. To create a  Service Principal with **Contributor** role, perform the following steps:

```bash
az ad sp create-for-rbac --name="UdacityProject3" --role="Contributor" 
```

> Take notes of **appId**, **password**, and **tenant** as will be used later on terraform

5. Create a resourcegroup for your VM image using Packer and build the Image ( Ubuntu 18.04)

```bash
az group create -n RG-myPackerImage -l eastus2
packer --version
cd packer
packer build ubuntu-image.json
cd..
pwd
```

> Here you will get an Ubuntu 18.04 VM Image, which will be used on terraform to create the VM.!!!

```bash
==> azure-arm:  -> Image ResourceGroupName   : 'RG-myPackerImage'
==> azure-arm:  -> Image Name                : 'myPackerImage'
==> azure-arm:  -> Image Location            : 'eastus2'
```

6.  On your terminal create a SSH key

```bash
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
```

```bash
ssh-keyscan github.com
```

8. From the terminal, change into terraform directory

```bash
cd
cd terraform
```

9. Execute terraform performing these commands in order:

```bash
terraform init
terraform fmt
terraform validate

```

10. Execute terraform to create the backend infrastructure

```bash
terraform plan 
terraform apply
```

11. Modify the Azure DevOps Pipeline

* Add the Environment Resource

```bash
mkdir azagent;cd azagent;curl -fkSL -o vstsagent.tar.gz https://vstsagentpackage.azureedge.net/agent/2.183.1/vsts-agent-linux-x64-2.183.1.tar.gz;tar -zxvf vstsagent.tar.gz; if [ -x "$(command -v systemctl)" ]; then ./config.sh --environment --environmentname "TESTING" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/javiercaparo574/ --work _work --projectname 'udacity-project-3' --auth PAT --token ngxxtqxo3viuio3qjt4mex3soe5v4nsxq7ehkskoe4gh6s6ecg7q --runasservice; sudo ./svc.sh install; sudo ./svc.sh start; else ./config.sh --environment --environmentname "TESTING" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/javiercaparo574/ --work _work --projectname 'udacity-project-3' --auth PAT --token ngxxtqxo3viuio3qjt4mex3soe5v4nsxq7ehkskoe4gh6s6ecg7q; ./run.sh; fi
```

```bash
Successfully added the agent
Testing agent connection.
....
   Active: active (running) since Tue 2021-03-09 03:20:16 UTC; 13ms ago
 Main PID: 2330 (runsvc.sh)
    Tasks: 7 (limit: 4680)
   CGroup: /system.slice/vsts.agent.javiercaparo574..ci\x2dcd\x2dtest\x2dautomation.service
           ├─2330 /bin/bash /home/udacity/azagent/runsvc.sh
           └─2333 ./externals/node10/bin/node ./bin/AgentService.js

```

* Create the Service Connection  in Project Settings > Pipelines > Service Connection

> be sure that you are verified and authenticated here!!!
> get the url to have the Service Connection ID:
https://dev.azure.com/<organiztion>/<project>/_apis/serviceendpoint/endpoints?api-version=5.0-preview.2
 
* Add the private secure id_rsa key in Library Secure files


### Links

> Collect custom logs with Log Analytics agent in Azure Monitor (
https://docs.microsoft.com/en-us/azure/azure-monitor/agents/data-sources-custom-logs)

> Collect data from an Azure virtual machine with Azure Monitor (https://docs.microsoft.com/en-us/azure/azure-monitor/vm/quick-collect-azurevm)

> Environment - virtual machine resource (https://docs.microsoft.com/en-us/azure/devops/pipelines/process/environments-virtual-machines?view=azure-devops)

> Build GitHub repositories (https://docs.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops&tabs=yaml)

> Tutorial: Store Terraform state in Azure Storage (https://docs.microsoft.com/en-us/azure/developer/terraform/store-state-in-azure-storage)

> Create your first pipeline (https://docs.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&tabs=azure-cli%2Ctfs-2018-2%2Cbrowser)

> Create a project in Azure DevOps (https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops&tabs=preview-page)

> Create a Linux VM with infrastructure in Azure using Terraform (https://docs.microsoft.com/en-us/azure/developer/terraform/create-linux-virtual-machine-with-infrastructure)

> Create a Log Analytics workspace with Azure CLI 2.0 (https://docs.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace-cli)

> Hashicorp Terraform with Azure (https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet)


> azure-pipelines-jmeter-extension (https://marketplace.visualstudio.com/items?itemName=AlexandreGattiker.jmeter-tasks&ssr=false#qna)
(https://github.com/algattik/azure-pipelines-jmeter-extension/issues?utm_source=vsmp&utm_medium=ms%20web&utm_campaign=mpdetails)