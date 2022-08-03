from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Search keyword for Youtube
search = '2022'


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.youtube.com/results?search_query={}&sp=CAMSAhAB'.format(search))
driver.implicitly_wait(10)
content = driver.page_source.encode('utf-8').strip()

soup = BeautifulSoup(content, 'lxml')

titles = soup.findAll('a', id='video-title')
views = soup.findAll('span', class_='style-scope ytd-video-meta-block')
video_url = soup.findAll('a', id='video-title')

i = 0
j = 0
for title in titles[:5]:
    print('{}\t{}\t{} \n https://www.youtube.com{}'.format(title.text.strip(),
                                                           views[i].text,
                                                           views[i + 1].text,
                                                           video_url[j].get('href')))
    i += 2
    j += 1
