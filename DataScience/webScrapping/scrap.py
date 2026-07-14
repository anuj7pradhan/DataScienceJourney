from bs4 import BeautifulSoup
import requests
 

with open('DataScience/webScrapping/sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    
print(soup.prettify())

match = soup.title
print(match)

match = soup.title.text
print(match)

match = soup.div
print(match)


article1 = soup.find('div', class_='article1')
print(article1)

headline = article1.h2.a.text
print(headline)


article2 = soup.find('div', class_='article2')
print(article2)
headline = article2.h2.a.text

print(headline)
summary = article2.p.text
print(summary)