from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver=webdriver.Chrome(ChromeDriverManager().install())



# ------- Enter Your Channel ID and Password --------


CID='Your Channel ID'
password='Your Password'


# ----------------------------------------------------


link1='https://www.subpals.com/login/final/'+CID+'/'
link2='https://www.ytpals.com/login/final/'+CID+'/'
link3='https://www.sonuker.com/login/final/'+CID+'/'




# ------------- subpals activation -------------

driver.get(link1)
sleep(2)
driver.find_element_by_name("password").send_keys(password)
sleep(2)
driver.find_element_by_name("password").send_keys("\ue007")
sleep(2)
driver.find_element_by_name("starter").submit()
sleep(2)
for x in range(21):
    driver.get("https://www.subpals.com/members-area/sub-completed-v4.php")
    sleep(2)
driver.get("https://www.subpals.com/members-area/activate/")
sleep(2)


# ------------- ytpals activation -------------

driver.get(link2)
sleep(2)
driver.find_element_by_name("password").send_keys(password)
sleep(2)
driver.find_element_by_name("password").send_keys("\ue007")
sleep(2)
driver.find_element_by_name("starter").submit()
sleep(2)
for x in range(21):
    driver.get("https://www.ytpals.com/members-area/sub-completed-v4.php")
    sleep(2)
driver.get("https://www.ytpals.com/members-area/activate/")
sleep(2)


# ------------- sonuker activation -------------

driver.get(link3)
sleep(2)
driver.find_element_by_name("password").send_keys(password)
sleep(2)
driver.find_element_by_name("password").send_keys("\ue007")
sleep(2)
driver.find_element_by_name("starter").submit()
sleep(2)
for x in range(21):
    driver.get("https://www.sonuker.com/members-area/sub-completed-v4.php")
    sleep(2)
driver.get("https://www.sonuker.com/members-area/activate/")
sleep(2)
