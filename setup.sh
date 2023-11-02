#!/bin/bash

# Define the GitHub repository and your username
repo_url="https://github.com/amish0/Python_Setup_Basic.git"

# Set the directory where your local repository is located
local_dir="/user/amish0/Python_Setup_Basic"

# Fetch the latest information about the remote repository
git fetch

# Get the latest release tag from the remote repository
latest_release=$(git ls-remote --tags $repo_url | awk -F/ '{print $3}' | sort -t. -k1,1nr -k2,2nr -k3,3nr | head -n 1)

# Check if the latest release tag is different from the current local tag
if [ "$(git describe --tags)" != "$latest_release" ]; then
    # Pull the latest changes from the remote repository
    git pull
    echo "Repository updated to the latest release: $latest_release"
else
    echo "No updates available."
fi
