import requests

site_id = '0a6f0cb8-7d7e-478b-b808-d975d939ab21'
url = f'https://api.netlify.com/api/v1/sites/{site_id}/service-instances'
headers = {
    "User-Agent": "resonant-druid-c3f299",
    "Authorization": "Bearer z3TWgCM-msRrjFokXQFDyd2YmxGPPIPDopPQyhOaPG8"
}
response = requests.get(url, headers=headers)

print(response.content)