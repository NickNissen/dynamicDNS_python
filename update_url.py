import boto3
from dotenv import load_dotenv
from os import getenv
from requests import get


load_dotenv()
getenv('HOSTED_ZONE_ID')

def main():
    ip = get_ip()
    oldIp = get_old_ip()
    if ip != oldIp:
        update_dns(ip)
        update_ip(ip)

def get_ip():
    ip = get('https://ident.me').text
    return ip.strip()

def get_old_ip():
    try:
        with open('ip.log','r') as logfile:
            ip = logfile.read().strip()
            return ip
    except FileNotFoundError:
        with open('ip.log','w') as logfile:
            return None

def update_ip(ip):
    with open('ip.log','w') as logfile:
        logfile.write(ip)

def update_dns(ip):
    client = boto3.client('route53',aws_access_key_id=getenv('AWS_ACCESS_KEY'),aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'))
    response = client.change_resource_record_sets(
        HostedZoneId= getenv('HOSTED_ZONE_ID'),
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': getenv('DOMAIN'),
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords':[
                            {
                                'Value': ip
                            }
                        ]
                    }
                }
            ]
        }
    )


if __name__ == '__main__':
    main()
