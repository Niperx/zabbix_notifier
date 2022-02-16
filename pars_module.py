import time
import requests
import numpy as np

from bs4 import BeautifulSoup

from config import USERNAME, PASSWORD, url_login, url, user_agent

                     
session = requests.Session()
r = session.get(url_login, headers = user_agent)

session.headers.update({'Referer': url_login})
session.headers.update({'User-Agent': user_agent})
_xsrf = session.cookies.get('_xsrf', domain="monitor.st65.ru/")
  # 
post_request = session.post(url_login, {
      'name': USERNAME,
      'password': PASSWORD,
      'autologin' : '1',
      'enter': 'Sign in'
 })

def main(url = url, session = session):
  adress = [0]
  vremm = [0]

  response = session.get(url)

  start_time = time.time()

  soup = BeautifulSoup(response.text, 'lxml')
  quotes = soup.find_all('span', class_='link-action')




  # vrem = soup.find_all('td',class_='timeline-date')

  start_time = time.time()
  for item in quotes: 
    item_attr = item.get('data-menu-popup')
    if str(item_attr)[1:14] == '"type":"host"':
      adress.append(item.text)
  adress = np.array(adress)

  print("--- %s seconds SORT---" % (time.time() - start_time))
  
#  for item in vrem:  
#    if str(item)[0:37] == '<td class="timeline-date"><a href="tr':
#      a1 = (str(item).find('</a></td>'))
#      a2 = (str(item).rfind('">')) + 2
#      vremm.append(str(item)[a2:a1])

   
#  for i in range (1,len(adress)): 
#    adress[i] = str(adress[i]) + '|' + str(vremm [i]) + '|' 

  adress = adress[:14]
  print("--- %s seconds ---" % (time.time() - start_time))
  return adress


