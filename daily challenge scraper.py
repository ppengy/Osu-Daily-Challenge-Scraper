from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from datetime import datetime
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time


def startDriver():
    profile = FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", True)
    profile.set_preference("browser.cache.memory.enable", True)
    profile.set_preference("browser.cache.offline.enable", True)
    options = FirefoxOptions()
    # options.add_argument("--headless")
    options.set_preference("permissions.default.image", 2)
    driver = webdriver.Firefox(options=options)
    return driver


def getlinksToDate(driver, output):
    date = datetime.now().strftime("%Y-%m-%d")
    driver.get("https://osu.ppy.sh/rankings/daily-challenge/" + date)
    DailyChalLink = driver.find_elements(
        By.XPATH, "//html/body/div[8]/div[2]/div[1]/div/div[2]/a"
    )
    for link in DailyChalLink:
        line = link.get_attribute("href")
        output.write(f"{line}\n")
    return DailyChalLink


def scrape_DailyChal(driver, link):
    driver.get(link)
    DailyChalLink = driver.find_element(
        By.XPATH, "/html/body/div[8]/div[3]/div[1]/div/div/a"
    ).get_attribute("href")
    print("Beatmap Challenge Link: " + DailyChalLink)
    return DailyChalLink

start_time = time.process_time()
driver = startDriver()
outputFile = open(r"beatmap links.txt", "w")
inputFile = open(r"challenge links.txt", "w")
getlinksToDate(driver, inputFile)
inputFile = open(r"challenge links.txt", "r")
L = inputFile.readlines()
for line in L:
    DCLink = line.strip()
    DCDate = DCLink.split("/")[-1]
    print("Current Daily Challenge: " + DCDate)
    time.sleep(1.5)
    beatmapLink = scrape_DailyChal(driver, DCLink)
    data = f"{DCDate} {beatmapLink}\n"
    outputFile.write(data)

print("Finished in " + str(time.process_time() - start_time) + " seconds")
outputFile.close()
inputFile.close()
driver.quit()
