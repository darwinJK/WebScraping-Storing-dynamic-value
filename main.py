
from selenium import webdriver
import time
from datetime import datetime

#connecting driver
def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("diable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver

#auto file creation
def filecreation(temperature):
    currentdate = datetime.now()
    formatted_date = currentdate.strftime("%Y-%m-%d %H:%M:%S")
    print("Time: " + str(formatted_date))
    with open(formatted_date + ".txt","w") as file:
     file.write("Average world temperature : " + temperature)

#cleaning the webscraped data
def clean_text(text):
  temperature = text.split(": ")  
  output = temperature[1]
  filecreation(output)
  return str(output)
  
def main():
  driver = get_driver()
  time.sleep(2)
  temp = ""
  
  #Collecting values 
  for i in range(5):
    time.sleep(2)
    element = (driver.find_element(by="xpath",value = "/html/body/div[1]/div/h1[2]")).text
    print("String : " + element)
    temp = clean_text(element)
  return temp

value = main()
print("Temperature : " + value)

