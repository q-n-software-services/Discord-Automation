import requests
from bs4 import BeautifulSoup

# contents-2MsGLg

url = "https://discord.com/channels/469229972641284097/847938799689269299"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
print(soup)