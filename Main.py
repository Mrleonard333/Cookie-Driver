from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

Click_on = { # < Dict with all XPATHs
        "Cookie":'/html/body/div/div[2]/div[15]/div[8]/button',
        "Buildings":'/html/body/div/div[2]/div[19]/div[3]/div[6]/div[_]',
        "Upgrades":'/html/body/div/div[2]/div[19]/div[3]/div[5]/div[_]'
           }

Browser = webdriver.Firefox() # < Will open the Firefox
Browser.get("https://orteil.dashnet.org/cookieclicker/") # < Will access the game

sleep(3)            # v Path reader type [XPATH]
Browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]").click() # < Will click on the especific html
sleep(0.5)                                        # ^ path to element

while True:
    for R in range(1,51):
        Browser.find_element(By.XPATH, Click_on["Cookie"]).click()

    for C in range(1, 20):
        C += 1                              # v Will change the character
        Building = Click_on["Buildings"].replace("_", str(C))
        C -= 1
        Upgrade = Click_on["Upgrades"].replace("_", str(C))

        try:
            Element = Browser.find_element(By.XPATH, Upgrade)
            if "enabled" in Element.get_attribute("class"):
                Element.click()         # ^ Will return a string with the class value
        except: pass

        try:
            Element = Browser.find_element(By.XPATH, Building)
            if not "disabled" in Element.get_attribute("class"):
                Element.click()
        except: pass