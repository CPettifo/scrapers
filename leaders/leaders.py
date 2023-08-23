try:
    from googlesearch import search
except ImportError:
    print("You need the google and beautifulsoup4 pip modules")

# Take a parameter of country
# country = "whatever country"

# Perform a google search for "leader of <country>"
query = "Who is the leader of australia?"

for j in search(query, tld = "co.in", num = 1, stop = 10, pause = 2):
    print(j)