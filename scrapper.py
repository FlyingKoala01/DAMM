from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

options = Options()
# In headless mode JS is not executed (needed because google does weird things).
#options.headless = True

driver = Firefox(options=options, executable_path='./geckodriver')

driver.get('https://www.google.com/search?q=Crtra+cardona+77+manresa')
grade_span = driver.find_element_by_css_selector('span.yi40Hd.YrbPuc')

try:
    grade_float = float(grade_span.text.replace(',','.'))
    print(grade_float)
except:
    pass

driver.quit()
