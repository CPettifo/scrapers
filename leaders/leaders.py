try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("You need the requests and beautifulsoup4 pip modules")

response = requests.get(
    url="https://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government"
)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('table',{'class':"wikitable"})

print(title)

print("Response status code: " + str(response.status_code))