from bs4 import BeautifulSoup
import urllib2

# custom package from Python website (ensure .py file is in same folder)
from UnicodeWriter import UnicodeWriter

# substrings to construct our Amazon affiliate links and image URLs
link0 = "http://www.amazon.com/gp/product/"
link1 = "/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN="
link2 = "&linkCode=as2&tag=buyusabrand-20"
pict0 = "http://ws.assoc-amazon.com/widgets/q?_encoding=UTF8&ASIN="
pict1 = "&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=buyusabrand-20"

soup = BeautifulSoup(urllib2.urlopen("http://www.21usdeal.com/zh/"))
#soup = BeautifulSoup(open("21usdeal_test.html"))

titles = soup.findAll(attrs={'class' : "art-postheader"})
descrs = soup.findAll(attrs={'class' : "art-postcontent"})
links = soup.findAll(attrs={'class' : "morelink"})

with open('wordpress.csv', 'wb') as f:
    writer = UnicodeWriter(f, delimiter=",")
    writer.writerow(["csv_post_title", "csv_post_post", "csv_post_type", "csv_post_excerpt", "csv_post_categories", "csv_post_tags", "csv_post_date", "desc", "link", "picture"])
    
    for (title, descr, link) in zip(titles, descrs, links):
        link = link.a.next_sibling.get('href')
        
        # only run if this is an Amazon link
        if link0 in link :
            title = title.a.get_text(strip=True)
            descr = descr.get_text(strip=True)
            
            # extract the Amazon product ID
            asin = link.split('/')[5]

            link = ""+link0+asin+link1+asin+link2
            pict = ""+pict0+asin+pict1

            writer.writerow([title, "", "post", title, "csvtest", "", "now", descr, link, pict])
