import requests
from requests.api import head
from requests.structures import CaseInsensitiveDict

url = "https://www.backloggd.com/games/lib/popular"

headers = CaseInsensitiveDict()
headers["Cookie"] = "_august_app_session=cWFhSnNhamtUZHRLbWh6S0JJeTNvbG5YQzRKbTk5TTYvdTRRaHZxTzhUbWUrZytqblpGVjdCdDJsQy9lZ1ZkNFdHYzVXQ2lCd1ZWVVJXTTkvMzBzSDVwR0ltd2xXL0FNWTlQUFZsU241MVRiTnNpUXZLRk9EZ0lIanYwZTBFdjF5WFVEVEcwVzA1WVV5dks2OWxZRERBbkRMU0lONVlkWTQxbE83QU0wQVFPSVNmVkxXWFBXSDFZeStMTzJaVHJKZ2ZoRGdJRStyVlVpTnBPdWw4a3BQQ1Z3cG5QZEFZVUFHTksva0NsazBSRHdXSVlkT0xUa0ZtU21GWHBpcnpjcnZHOE9FQy9Gek8wNTJjS1U5Y3NjUXV1THpEU1VsUGpwNndJY0VLNE92Zlk9LS01ZnBCRW8vSmdKV0IrL3NNSjNFM1dRPT0%3D--611aee198353c82cbc40e7d08847e6af048224d4"
headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.34 Safari/537.36"


response = requests.get(url, headers=headers)

print(response.status_code)

with open("site-games.html", "w") as fs:
    fs.write(response.text)


def getInfoSite(endpoint):
    headers = CaseInsensitiveDict()
    headers["Cookie"] = "_august_app_session=cWFhSnNhamtUZHRLbWh6S0JJeTNvbG5YQzRKbTk5TTYvdTRRaHZxTzhUbWUrZytqblpGVjdCdDJsQy9lZ1ZkNFdHYzVXQ2lCd1ZWVVJXTTkvMzBzSDVwR0ltd2xXL0FNWTlQUFZsU241MVRiTnNpUXZLRk9EZ0lIanYwZTBFdjF5WFVEVEcwVzA1WVV5dks2OWxZRERBbkRMU0lONVlkWTQxbE83QU0wQVFPSVNmVkxXWFBXSDFZeStMTzJaVHJKZ2ZoRGdJRStyVlVpTnBPdWw4a3BQQ1Z3cG5QZEFZVUFHTksva0NsazBSRHdXSVlkT0xUa0ZtU21GWHBpcnpjcnZHOE9FQy9Gek8wNTJjS1U5Y3NjUXV1THpEU1VsUGpwNndJY0VLNE92Zlk9LS01ZnBCRW8vSmdKV0IrL3NNSjNFM1dRPT0%3D--611aee198353c82cbc40e7d08847e6af048224d4"
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.34 Safari/537.36"
    response = requests.get(endpoint, headers=headers)
    return response.text
