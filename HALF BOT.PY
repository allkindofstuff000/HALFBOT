import requests
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import random
import string
import signal
import os
import time
import winsound
from timezonefinder import TimezoneFinder
from datetime import datetime
from pywinauto import Desktop
from selenium import webdriver
import pyautogui
import pytz

# Rest of the code...

# Generate a random MAC address
def generate_random_mac_address():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

# Generate a random computer name
def generate_random_computer_name(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Prompt for the Chrome profile directories
profile_directories = input("Enter the Chrome profile directories (comma-separated): ").split(",")

# Create the profile directories if they don't exist
for directory in profile_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Read the user agents from the text file
user_agents_file = r"C:\Users\$\Desktop\ALLSET\all user agent.txt"
with open(user_agents_file, "r") as file:
    user_agents = file.read().splitlines()

# Rest of the code...
for profile_directory in profile_directories:
    # Print the generated MAC address, computer name, and user agent
    mac_address = generate_random_mac_address()
    computer_name = generate_random_computer_name()
    user_agent = random.choice(user_agents) if user_agents else "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    print("Generated MAC address:", mac_address)
    print("Generated computer name:", computer_name)
    print("Selected user agent:", user_agent)

 

       # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument(f'--user-data-dir={profile_directory}')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-webrtc')
    chrome_options.add_argument('--disable-features=WebRtcHideLocalIpsWithMdns')
    chrome_options.add_argument('--disable-features=WebRtcLocalIpsWithMdns')
    chrome_options.add_argument('--disable-geolocation')
    chrome_options.add_argument(f'--user-agent={user_agent}')
    chrome_options.add_argument('--window-size=375,812')  # Adjust the width and height as needed
    chrome_options.add_argument('--window-position=0,0')  # Set the window position to top left

            # Additional arguments to enhance undetectability
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])


    
       # Replace this line with your chromedriver path 
    chromedriver_path = r"C:\Users\$\Desktop\ALLSET\chromedriver.exe"  # Provide the correct path

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Maximize the window
    driver.maximize_window()

    # Set the browser window size to a specific width and height (adjust as needed)
    driver.set_window_size(500, 800)

    # Navigate to the login page
login_url = "https://megapersonals.eu/users/auth/login"
driver.get(login_url)

# Wait for 3 seconds for the redirected page to load
time.sleep(8)

# Read the email and password from the file
with open(r"C:\Users\$\Desktop\HANGISH1.txt", "r") as file:
    email, password = file.readline().strip().split(":")
    
# Find the email input field and enter the email
email_input = driver.find_element(By.ID, "person_username_field_login")
email_input.send_keys(email)

# Find the password input field and enter the password
password_input = driver.find_element(By.ID, "person_password_field_login")
password_input.send_keys(password)

# Rest of your code...
api_key = '79763ed453a23ea55a4c16b7acfa9c2a'
captcha_site_key = '6LdDSG4UAAAAANv7vDF_spZrXcSC0JvorM_2N2WQ'
page_url = 'https://megapersonals.eu/users/auth/login'

response = requests.get(f'http://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={captcha_site_key}&pageurl={page_url}')

if 'OK' in response.text:
    captcha_id = response.text.split('|')[1]

    while True:
        time.sleep(5)
        response = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}')
        if 'OK' in response.text:
            captcha_response = response.text.split('|')[1]
            break
        elif 'CAPCHA_NOT_READY' in response.text:
            continue

    driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML='{captcha_response}';")
else:
    print("Captcha solving API request failed.")

time.sleep(2)


# Locate the submit button element by its ID
submit_button = driver.find_element(By.ID, "login_data_submit_button")

# Alternatively, you can locate it by XPath
# submit_button = driver.find_element(By.XPATH, '//*[@id="login_data_submit_button"]')

# Click the submit button
submit_button.click()



driver.get('https://megapersonals.eu/users/posts/create')

# Add a delay before uploading the picture
time.sleep(6)

# Select the category
category_dropdown = driver.find_element(By.ID, 'category')
category_dropdown.click()
category_option = driver.find_element(By.XPATH, "//option[contains(text(), 'I AM A WOMAN seeking Men')]")
category_option.click()

# Function to generate random text with emojis and custom characters
def generate_random_text(words_count):
    words = ['LATINA DREAM GIRL', 'Anal Doggy Style', 'Available Any Style Fuck For You', ' Blowjob ', ' Missionary', 'Photos nudes package deals', ' 𝐈𝐧𝐂𝐚𝐥𝐥 𝐎𝐮𝐭𝐂𝐚𝐥𝐥𝐂𝐚𝐫', 'HornyQueen', 'No Cops', ' No Games ']
    random_words = ' '.join(random.choices(words, k=words_count))
    return random_words

# Rest of the code...

# Fill in the headline with random text
headline_field = driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/div/div[4]/div[1]/div[1]')
headline_text = generate_random_text(10)
headline_field.send_keys(headline_text)

# Fill in the body with random text
body_field = driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/div/div[5]/div/div[1]/div[1]')
body_text = generate_random_text(10)
body_field.send_keys(body_text)

# Select the city
city_field = driver.find_element(By.ID, 'cityName')
city_field.click()

# Select the country
country_label = driver.find_element(By.XPATH, "//label[contains(text(), 'United States')]")
country_label.click()

# Select the state
state_label = driver.find_element(By.XPATH, "//label[contains(text(), 'Alabama')]")
state_label.click()

# Select the city from the dropdown
city_option = driver.find_element(By.XPATH, "//a[contains(text(), 'Mobile')]")
city_option.click()

# Clear the phone number field
phone_number_field = driver.find_element(By.ID, 'phonenumber')
phone_number_field.clear()

# Generate a random phone number with area code 225
random_phone_number = f"225-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

# Enter the generated phone number
phone_number_field.send_keys(random_phone_number)

# Select the age
age_dropdown = driver.find_element(By.ID, 'age')
age_dropdown.click()
age_option = driver.find_element(By.XPATH, "//option[contains(text(), '30')]")
age_option.click()

# Select the "I See" option
i_see_input = driver.find_element(By.ID, 'iseeCategories_input')
i_see_input.clear()
i_see_input.send_keys('Men')

next_button = driver.find_element(By.ID, 'next_button_from_first_form_page')
next_button.click()

# Add a delay before uploading the picture
time.sleep(2)

picture_directory = "C:\\Users\\$\\Desktop\\ALLSET\\pic"

picture_files = os.listdir(picture_directory)
random_picture = random.choice(picture_files)
picture_path = os.path.join(picture_directory, random_picture)

main_photo_button = driver.find_element(By.XPATH, '/html/body/div[3]/form/div[2]/div[1]/div[4]/div[2]/div[1]/img')
main_photo_button.click()

file_input = driver.find_element(By.ID, 'input_image')
file_input.send_keys(picture_path)
time.sleep(1)

windows = Desktop(backend="win32").windows()
print([w.window_text() for w in windows])
file_dialog = list(filter(lambda w: w.window_text() == 'Open', windows))[0]
time.sleep(1)
file_dialog.close()

api_key = '79763ed453a23ea55a4c16b7acfa9c2a'
captcha_site_key = '6LdDSG4UAAAAANv7vDF_spZrXcSC0JvorM_2N2WQ'
page_url = 'https://megapersonals.eu/users/register'

response = requests.get(f'http://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={captcha_site_key}&pageurl={page_url}')

if 'OK' in response.text:
    captcha_id = response.text.split('|')[1]

    while True:
        time.sleep(5)
        response = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}')
        if 'OK' in response.text:
            captcha_response = response.text.split('|')[1]
            break
        elif 'CAPCHA_NOT_READY' in response.text:
            continue

    driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML='{captcha_response}';")
else:
    print("Captcha solving API request failed.")

time.sleep(2)

publish_button = driver.find_element(By.XPATH, "/html/body/div[3]/form/div[2]/div[3]/div[2]/div[2]")
publish_button.click()

# Add a delay before uploading the picture
time.sleep(2)

# Rest of the code...


# Loop until the "OK" button is found on the redirected page
while True:
    current_url = driver.current_url
    if current_url.startswith('https://megapersonals.eu/users/pendingImages/'):
        try:
            # Use find_elements and select by index to locate the OK button by its XPATH
            ok_button = driver.find_elements(By.XPATH, '//img[@alt="OK"]')[0]
            # Use WebDriverWait and expected_conditions to wait for the element to be clickable by its locator
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//img[@alt="OK"]')))
            ok_button.click()
            break  # Exit the loop if successful
        except:
            pass  # Ignore any exceptions and continue looping

# Wait for the redirect to the next URL
WebDriverWait(driver, 60).until(EC.url_changes(current_url))

# Add a delay before uploading the picture
time.sleep(6)

# Find the OK button by its ID
ok_button = driver.find_element("id", "button-ok")

# Execute JavaScript to click on the hidden element
driver.execute_script("arguments[0].click();", ok_button)




# Wait for 3 seconds for the redirected page to load
time.sleep(3)
# Rest of the code...

# Open the text file and read the values for year, month and day
with open("C:\\Users\\$\\Desktop\\ALLSET\\DATEOFBIRTH1.txt", "r") as f:
    date_of_birth = f.read().split(":") # Split by colon to get a list of values
    year = date_of_birth[0]
    month = date_of_birth[1]
    day = date_of_birth[2]

# Locate the input fields by their id attributes
year_input = driver.find_element(By.ID, "birth-year")
month_input = driver.find_element(By.ID, "birth-month")
day_input = driver.find_element(By.ID, "birth-day")

# Send the values to the input fields
year_input.send_keys(year)
month_input.send_keys(month)
day_input.send_keys(day)

# Locate the submit button by its id attribute
submit_button = driver.find_element(By.ID, "btn-go-to-photo-id")

# Click the submit button
submit_button.click()

# Wait for 3 seconds for the redirected page to load
time.sleep(2)

# Locate the I'm ready button by its XPath expression
ready_button = driver.find_element(By.XPATH, '//*[@id="btn-take-photo-id"]/h4')

# Click the I'm ready button
ready_button.click()


# Wait for user action before closing the browser
input("Press Enter to close the browser...")
driver.quit()