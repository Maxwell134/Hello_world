#!/bin/bash

# Variables
RESOURCE_GROUP_NAME="myResourceGroup"   # Set the name of your resource group
AKS_CLUSTER_NAME="myAKSCluster"         # Set the name of your AKS cluster
LOCATION="southeastasia"                       # Set the region for your cluster (e.g., eastus, westus)
NODE_COUNT=3                         # Number of nodes in the cluster
NODE_SIZE="Standard_DS2_v2"             # VM size for the nodes (e.g., Standard_DS2_v2, Standard_B2ms)

# Create Resource Group (if it doesn't exist)
echo "Creating resource group: $RESOURCE_GROUP_NAME in $LOCATION..."
az group create --name $RESOURCE_GROUP_NAME --location $LOCATION

# Create AKS Cluster
echo "Creating AKS cluster: $AKS_CLUSTER_NAME..."
az aks create \
  --resource-group $RESOURCE_GROUP_NAME \
  --name $AKS_CLUSTER_NAME \
  --node-count $NODE_COUNT \
  --node-vm-size $NODE_SIZE \
  --enable-addons monitoring \
  --generate-ssh-keys

# Get AKS Cluster credentials
echo "Getting AKS cluster credentials..."
az aks get-credentials --resource-group $RESOURCE_GROUP_NAME --name $AKS_CLUSTER_NAME
echo "AKS Cluster $AKS_CLUSTER_NAME created successfully!"
