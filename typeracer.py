import pyautogui
import time
from selenium import webdriver


driver = webdriver.Chrome('C:/chromedriver')
driver.get('https://play.typeracer.com')

time.sleep(1)

# If playing with friends
driver.find_element_by_class_name("raceAgainLink").click()

# If playing with randoms
# driver.find_element_by_class_name('prompt-button').click()

time.sleep(1)
# If playing with friends
firstLetter = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]')
secondLetters = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]')
mainText = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]')

# If playing with randoms
# span1 = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]')
# span2 = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]')
# span3 = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]')

elements = span1 + span2 + span3

text = ''

for i in range(len(elements)):
    text += elements[i].text

print(text)
# for p in range(len(span1)):
#     text += span1[p].text
# for p in range(len(span2)):
#     text += ' ' + span2[p].text
# for p in range(len(span3)):
#     text += ' ' +  span3[p].text

play = False

while play == False:
    try:
        driver.find_element_by_class_name('countdownPopup')
    except:
        play = True

textArr = text.split(' ')

for i in textArr:
    # print(i)
    pyautogui.write(i + ' ')

print('Finished')