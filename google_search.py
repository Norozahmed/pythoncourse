from googlesearch import search

query = input("ہرچیزے جست کن")

for url in search(query):
    print(url)

