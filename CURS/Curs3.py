#Selenium Google
from selenium import webdriver

driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.cel.ro/index.php?main_page=login")

#Nume
get_element1 = driver.find_element_by_id('firstname')
get_element1.send_keys('Tudor')

#Prenume
get_element2 = driver.find_element_by_id('lastname')
get_element2.send_keys('Mihai')

#email
get_element3 = driver.find_element_by_name('email_address')
get_element3.send_keys('tudormihaieugen@gmail.com')

#sex
get_element4 = driver.find_element_by_id('customers_gender')
get_element4.send_keys('Domnul')

#telefon
get_element5 = driver.find_element_by_id('telephone')
get_element5.send_keys('0771759112')

#scroll  -->  1080 rezolutie
driver.execute_script("window.scrollTo(0, 1080)")

#Adresa
get_element6 = driver.find_element_by_id('street_address')
get_element6.send_keys('Pitesti, Arges')

#Judet/Sector
get_element7 = driver.find_element_by_id('entry_suburb')
get_element7.send_keys('Arges')

#Oras
get_element8 = driver.find_element_by_id('city')
get_element8.send_keys('Pitesti')

#termeni
get_element9 = driver.find_element_by_name('termeni')
get_element9.click()

#submit
get_element1.submit()
