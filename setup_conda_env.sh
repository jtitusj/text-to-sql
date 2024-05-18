#!/bin/bash

# Define the environment name
env_name="llm_dev"

# if env exist skip installation...
if conda info --envs | grep -q ${env_name}; then 
  echo "$env_name already exists"; 
else 
  echo "installing env"
  conda create --name ${env_name} python
fi