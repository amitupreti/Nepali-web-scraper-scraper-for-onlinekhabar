# Welcome to the Nepali-news-Web-Scraper!

### with this scraper you can scrape every news article from onlinekhabar.com and save it locally on your computer in different formats such as csv, json
## Here is the link to scraped to data
     `https://drive.google.com/file/d/1E8u6_pJbsWPhg61hfPi5Up4l730SUKRb/view?usp=sharing`

## Notes:
     Operating System: Linux
     Language:         python3
     libraries:        Scrapy, system, chdir   

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
 `scrapy crawl onlinekhabr -a category="blog" -a address="https://www.onlinekhabar.com/content/opinion" -o blogdata.csv`

 This is the sample code

 `scrapy crawl onlinekhabr -a category="blog" -a address="https://www.onlinekhabar.com/content/opinion" -o blogdata.csv`

 ### Explanation of code :  
   *  It will create a folder name blog(category="blog").If you want another folder for your news change the category value
    * It will create a csv file name blogdata.csv and the scraped news articles will be inside the csv file(if you want news in json  format put (-o blogdata.json)
   *  You can also change the address to scrape other news such as entertainment, business. Get the link from onlinekhabar for a category that you want. dont forget to change category='yourcategory' in the code


<a href="https://ibb.co/kMd7HG"><img src="https://preview.ibb.co/eJzsjw/git.png" alt="git" border="0" /></a>



[If you have problems please refer to the video on the link](https://www.youtube.com/watch?v=cBASLM-VOFg)
