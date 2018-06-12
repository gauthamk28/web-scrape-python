import requests
from bs4 import BeautifulSoup
url="https://play.google.com/store/apps/details?id=uk.co.o2.android.myo2&hl=en_GB&showAllReviews=true"
r=requests.get(url)
html=r.text
soup = BeautifulSoup(html, "html5lib")
type(soup)

soup.title
soup.title.string
