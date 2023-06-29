# import requests

# def get_country_name(ip_address):
#     api_key = 'your_ipstack_api_key_here'
#     url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
#     response = requests.get(url)
#     data = response.json()
#     return data['country_name']

# # Sample data for testing
# sample_ips = ['8.8.8.8', '157.240.221.35', '216.58.194.174']
# for ip in sample_ips:
#     print(f'IP address {ip} is going to {get_country_name(ip)}')


import requests


def get_country_name(ip_address):
    url = f'https://ipinfo.io/{ip_address}/country'
    response = requests.get(url)
    data = response.text.strip()
    return data


# Sample data for testing
sample_ips = ['8.8.8.8', '157.240.221.35', '216.58.194.174', "3.232.249.89", "3.228.175.144",
              "107.20.125.9", "18.214.219.120", "35.175.40.32", "35.168.85.18", "44.198.110.26", "3.85.67.177", "151.101.0.81", "151.101.128.81", "151.101.192.81", "151.101.64.81", "13.48.53.182", "16.16.40.161", "13.48.40.225"]

for ip in sample_ips:
    print(f'IP address {ip} is going to {get_country_name(ip)}')
 

# test change