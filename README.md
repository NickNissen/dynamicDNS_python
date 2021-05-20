# Dynamic DNS using AWS Route53

Written By Nick Nissen 

MIT License


This script looks up the public IP address of the machine, checks if it has changed since the last lookup, and if the IP address has changed will update Route53 DNS records to reflect the change.

This can be useful for hosting a website or other service on a residential internet connection, or for providing a ssh or vpn address that is always available.

## Requirements

- Python3
- boto3
- dotenv
- os
- requests

- crontab

## Setup

Edit the 'env' file to include the relevant values and rename the file '.env'

run the script by calling 

'''
python3 update_url.py
'''

Confirm that Route53 has been updated.

Setup crontab with:

'''
* * * * * cd PATH_TO_DIR/ && python3 update_url.py >/dev/null 2>&1 
'''

This will run the script every minute
