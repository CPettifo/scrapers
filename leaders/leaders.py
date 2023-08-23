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

print(str(df.loc[df.index[12]]))

print("Response status code: " + str(response.status_code))