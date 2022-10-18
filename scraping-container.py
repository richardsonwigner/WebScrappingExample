from bs4 import BeautifulSoup
import requests
from requests.models import CaseInsensitiveDict
import json

def getInfoSite(endpoint):
    headers = CaseInsensitiveDict()
    headers["Cookie"] = "_august_app_session=cWFhSnNhamtUZHRLbWh6S0JJeTNvbG5YQzRKbTk5TTYvdTRRaHZxTzhUbWUrZytqblpGVjdCdDJsQy9lZ1ZkNFdHYzVXQ2lCd1ZWVVJXTTkvMzBzSDVwR0ltd2xXL0FNWTlQUFZsU241MVRiTnNpUXZLRk9EZ0lIanYwZTBFdjF5WFVEVEcwVzA1WVV5dks2OWxZRERBbkRMU0lONVlkWTQxbE83QU0wQVFPSVNmVkxXWFBXSDFZeStMTzJaVHJKZ2ZoRGdJRStyVlVpTnBPdWw4a3BQQ1Z3cG5QZEFZVUFHTksva0NsazBSRHdXSVlkT0xUa0ZtU21GWHBpcnpjcnZHOE9FQy9Gek8wNTJjS1U5Y3NjUXV1THpEU1VsUGpwNndJY0VLNE92Zlk9LS01ZnBCRW8vSmdKV0IrL3NNSjNFM1dRPT0%3D--611aee198353c82cbc40e7d08847e6af048224d4"
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.34 Safari/537.36"
    response = requests.get(endpoint, headers=headers)
    return response.text


def scraping_card(jogo):
    game_link = site + jogo.find('a')['href']
    data_game = jogo.find('div', attrs={ 'class': 'card mx-auto game-cover quick-access' })
    game_name = data_game.find('div', attrs = { 'class' : 'game-text-centered' })
    game_name = removeCaracters(game_name)
    print(game_name)
    game_img  = data_game.find('div', attrs = { 'class' : 'overflow-wrapper' }).find('img', attrs = { 'class' : 'card-img height' })['src']
    game_id   = data_game.find('div', attrs = { 'class' : 'quick-access-bar' })['game_id']
    return { "game_link": game_link, "game_name": game_name, "game_img" : game_img, "game_id": game_id }

def removeCaracters(game_name):
    return game_name.text.strip().lower().replace("'s", "s") .replace(":", "").replace(" ", "-").replace("&", "and").replace(".", "").replace("+", "plus")\
    .replace("é", "e")


site = "https://www.backloggd.com"
siteBusca = "https://www.backloggd.com/games/lib/popular?page={page}"
paginaJogo = "https://www.backloggd.com/games/{jogo}/"

nomeJogos = []

for page in range(1, 6):
    print(f"Iniciando Pagina {page}")
    
    dados = getInfoSite( siteBusca.replace("{page}", str(page) ) )
    soup = BeautifulSoup(dados, "html.parser")
    container_jogos = soup.find('div', attrs={ 'class': 'row show-release toggle-fade' })
    divs_jogos = container_jogos.findAll('div', attrs= { 'class' : 'col-2 my-2 px-1 px-md-2' })
    
    for jogo in divs_jogos:
        busca = scraping_card(jogo)['game_name']
        nomeJogos.append(busca)


with open("dados.json", 'w') as fs:
    json.dump(nomeJogos, fs, indent=4)

for jogos in nomeJogos:
    DadosDoJogo = getInfoSite(paginaJogo.replace("{jogo}", str(jogos) ) )
    print(paginaJogo.replace("{jogo}", str(jogos)))
    soupJogo = BeautifulSoup(DadosDoJogo, "html.parser")
