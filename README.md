# Welcome to the Nepali-news-Web-Scraper!

### with this scraper you can scrape every news article from onlinekhabar.com and save it locally on your computer in different formats such as csv, json
## Here is the link to scraped to data
          https://drive.google.com/file/d/1E8u6_pJbsWPhg61hfPi5Up4l730SUKRb/view?usp=sharing

## Notes:
     Operating System: Linux
     Language:         python3
     libraries:        Scrapy

     This scraper was purely  built for research purpose. 


#### you may need to edit the code at nepalinews/spiders/onlinekhabr.py


Please note that you might need to make some changes to the scraper 
if in future the interface of the onlinekhabar.com is 
changed.( the scraping is totally based on CSS)

### Guides to use the scrapper
 1. clone this repository to your computer
 2. Launch terminal
 3. Navigate to the folder with file scrapy.cfg
 4. Enter this code
 `scrapy crawl onlineScraper -o data.csv`

 This is the sample code

 `scrapy crawl onlinekhabr -a category="blog" -a address="https://www.onlinekhabar.com/content/opinion" -o blogdata.csv`


