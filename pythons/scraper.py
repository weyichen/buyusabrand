from bs4 import BeautifulSoup
import urllib2

# custom package from Python website (ensure .py file is in same folder)
from UnicodeWriter import UnicodeWriter

soup = BeautifulSoup(urllib2.urlopen("http://www.21usdeal.com/zh/"))
#soup = BeautifulSoup(open("21usdeal_test.html"))

titles = soup.findAll(attrs={'class' : "art-postheader"})
descrs = soup.findAll(attrs={'class' : "art-postcontent"})

names = [title.a.get_text(strip=True) for title in titles]
texts = [descr.get_text(strip=True) for descr in descrs]

with open('wordpress2.csv', 'wb') as f:
    writer = UnicodeWriter(f, delimiter=",")
    writer.writerow(["csv_post_title", "csv_post_post", "csv_post_type", "csv_post_excerpt", "csv_post_categories", "csv_post_tags", "csv_post_date", "desc", "link"])
    
    for (name, text) in zip(names, texts):
        writer.writerow([name, "", "post", name, "csvtest", "", "now", text, ""])