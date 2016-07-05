#!/bin/bash

# sensorE16 install script

# Edit manifest file to include location information
print_warning "Editing manifest.yaml to include location-specific information."
print_warning "Input your city and hit enter. Example: San Francisco"
read -p "City: " USER_CITY
sed -i 's|'"{CITY}"'|'"$USER_CITY"'|g' manifest.yaml
echo ""
print_warning "Input your state abbreviation and hit enter. Example: CA"
read -p "State: " USER_STATE
sed -i 's|'"{STATE}"'|'"$USER_STATE"'|g' manifest.yaml
echo ""
print_warning "Input your country abbreviation and hit enter. Example: USA"
read -p "Country: " USER_COUNTRY
sed -i 's|'"{COUNTRY}"'|'"$USER_COUNTRY"'|g' manifest.yaml
echo ""

## Set up 21 account
print_good "Now running 21 status to verify user & wallet creation."
print_warning "If you have not signed up for an account yet, go to https://21.co/signup/"

21 status
