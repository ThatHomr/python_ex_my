from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.naver.com')
# driver.implicitly_wait(15)
time.sleep(5)
driver.get('https://google.co.kr')
time.sleep(5)
driver.get('https://youtube.com/c/반원')
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.forward()

# 창 크기 조절
# driver.fullscreen_window()
# time.sleep(5)
# driver.set_window_rect(100, 100, 800, 800)
# time.sleep(5)
# driver.maximize_window()
# time.sleep(5)

driver.quit()