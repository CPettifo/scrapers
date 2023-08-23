try:
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
except ImportError:
    print("You need the requests and beautifulsoup4 pip modules, oh yeah and pandas")

response = requests.get(
    url="https://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government"
)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table',{'class':"wikitable"})

df = pd.read_html(str(table))
df=pd.DataFrame(df[0])

row = str(df.loc[df.index[12]])

split = row.split('\n')

state_split = split[0].split(' ')

state = state_split[len(state_split) - 1]

print(state)

print("Response status code: " + str(response.status_code))