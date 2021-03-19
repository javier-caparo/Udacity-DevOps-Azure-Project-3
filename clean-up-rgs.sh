#!/bin/bash

# Deleting the RGs for Package and Storage Account
az group delete -n RG-myPackerImage
az group delete -n tstate