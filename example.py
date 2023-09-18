import requests
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
