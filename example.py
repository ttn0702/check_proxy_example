import requests
'''
{
    'status': 'success',
    'country': 'Vietnam',
    'countryCode': 'VN',
    'region': 'DN',
    'regionName': 'Da Nang',
    'city': 'Cam Le',
    'zip': '',
    'lat': 16.0292,
    'lon': 108.223,
    'timezone': 'Asia/Ho_Chi_Minh',
    'isp': 'HUNASOFT',
    'org': 'Hunasoft Technology Solution Consulting Co.,
    Ltd',
    'as': 'AS135967 Bach Kim Network solutions Join stock company',
    'query': '103.179.174.201'
}
'''
proxy = {
    'username':'PVN86079',
    'password':'d06mlKxg',
    'ip':'103.179.174.204',
    'port':'56789',
}
proxies = {
    'http': f'''http://{proxy['username']}:{proxy['password']}@{proxy['ip']}:{proxy['port']}''',
    'https': f'''http://{proxy['username']}:{proxy['password']}@{proxy['ip']}:{proxy['port']}''' 
}
ip_api = requests.get('http://ip-api.com/json/', proxies=proxies, timeout=10)
