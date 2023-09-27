from selenium import  webdriver


# Replace space from - For example new-york.
city = str(input("Enter the name of the city you want the weather forecast for: ")).replace(" ","-")

try:
    webdriver.Chrome.get('https://www.weather-forecast.com/locations/" + city + "/forecasts/latest')
    print(webdriver.Chrome.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
except:
    print("Something went wrong")