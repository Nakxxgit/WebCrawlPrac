from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('/Users/nakxx/Desktop/WebCrawlPrac/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')
# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('username')
driver.find_element_by_name('pw').send_keys('password')

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

driver.implicitly_wait(5)

driver.get('https://section.blog.naver.com/main/BuddyPostList.nhn')

driver.implicitly_wait(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('#buddyNewPostListInSection > li > h5 > a')

for n in titles:
    print(n.text.strip())