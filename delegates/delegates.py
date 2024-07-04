# This python script (which isn't finished of course) aims to extract current heads of state from the wikipedia table containing current heads of state and government
# Using Beautiful soup and pandas for easier extraction.

try:
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
except ImportError:
    print("You need the requests and beautifulsoup4 pip modules, oh yeah and pandas\nTo install these requirements execute the command below in a terminal.\n" 
          +"pip install -r requirements.txt")

response = requests.get(
    url="https://pax.unesco.org/PermanentDelegations/PermanentDelegationsAll.html"
)

soup = BeautifulSoup(response.content, 'html.parser')

# First create a list of all countries at Unesco

# Loop through this list

    # For each item in the list, match the first h3 element to the name.

    # The next <b> element is the name of the delegation

    # The next <i><p> element is the name in French, 

    # The next <p> element is the address

    # Next <p> element is general phone number

    # Next <p> element is Fax

    # Next <p> is general email

    # Next <p> is correspondence language in the format Correspondence Language(s): EN;AR 

    # The next <p><i> element is for Notes

    # Finally divs with class "card-body" contain the memebers of the delegation

    


section = soup.find('table',{'class':"wikitable"})

df = pd.read_html(str(table))
df=pd.DataFrame(df[0])

row = str(df.loc[df.index[8]])
