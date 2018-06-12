# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 06:14:36 2018

@author: ASUS
"""

import requests
import re
from optparse import OptionParser
import json
import csv

def getGooglePlayReviews(id,page):
    data = {
        "reviewType": 0,
        "pageNum" :page,
        "id":id,
        "reviewSortOrder":4,
        "xhr": 1,        
        "hl":"en"
    }
    r = requests.post("https://play.google.com/store/getreviews?authuser=0", data=data)
    revs = re.findall("(review-title)(.*?)(review-link)",r.text)
    stars = re.findall("Rated (.*?) stars out of five stars" ,r.text)
    x = []
    tmp = []
    [x.append(y) for (a,y,b) in revs]
    for i,rev in enumerate(x):
        tmp.append({"rating":int(stars[i]),"review":rev[25:-24].replace("span","")})
    print ("[*] Retrieved " + str(len(tmp)) + " reviews")
    return tmp

def getNPages(id,n):
    s = []
    [[s.append(x) for x in getGooglePlayReviews(id,i)] for i in range(n)]
    return s

def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-p", "--pages",
                      action="store", 
                      dest="pages",
                      default=5,
                      help="The number of pages you want to scrape",)
    parser.add_option("-i", "--id",
                      action="store", 
                      dest="app_id",
                      default="com.facebook.katana",
                      help="The id of the app you want to scrape comments",)
    parser.add_option("-o", "--output",
                      action="store", 
                      dest="output",
                      default="output.json",
                      help="The output file where you want to dump results",)
    parser.add_option("-v", "--verbose",
                  action="store_false", dest="verbose", default=False,
                  help="Visualize the wordcloud associated with your results")
    (options, args) = parser.parse_args()
    print ("[*] Downloading the first " + str(options.pages) + " pages from: " + options.app_id)
    s = getNPages(options.app_id,int(options.pages))
    with open(options.output,"w+") as output_file:
        json.dump({"results": s},output_file)

if __name__ == '__main__':
    main()

#Converting json data to csv
    
json_data=open("output.json").read()

data = json.loads(json_data)
#print(data)

json_parsed=json.loads(json_data)
review_data = json_parsed['results']

# open a file for writing
res_data = open('reviews.csv', 'w',encoding='utf-8')

# create the csv writer object
csvwriter = csv.writer(res_data)
count = 0
for i in review_data:
      if count == 0:
             header = i.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(i.values())
res_data.close()