#!/bin/bash

install_programs() {
    while IFS= read -r program; do
        if ! dpkg -l | grep -q "$program"; then
            sudo apt-get install -y "$program"
        else
            echo "$program is already installed"
        fi
    done < "$1"
}

# Update package list and upgrade all packages
sudo apt-get update
sudo apt-get upgrade -y

install_programs()

# Install necessary packages
sudo apt-get install -y git vim zsh curl fzf

# Install Oh My Zsh (if using zsh)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

echo "Setup complete!"

