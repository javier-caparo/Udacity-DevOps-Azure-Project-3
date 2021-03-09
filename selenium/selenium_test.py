from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Ititialize settings
URL = "https://www.saucedemo.com/"
SEARCH_TERM = "T SHIRT"
LOG_FILE = "/var/logs/selenium/selenium_log.txt"
log_arr = []
chrome_options = Options()
chrome_options.add_argument("--headless")


def log(text):
    time = datetime.now().strftime("%Y-%m-%dT%H:%M:%SK")
    entry = time + " " + text
    print(entry)
    log_arr.append(entry)


def write_log():
    with open(LOG_FILE, "a+") as txt_file:
        for line in log_arr:
            txt_file.write("".join(line) + "\n")


def login(username, password, driver):
    log(f"Loggin {username} with password {password}")

    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    # Enter password
    username_field.send_keys(username)
    password_field.send_keys(password + Keys.RETURN)


def add_to_cart(item_title, button):
    log(f"Adding {item_title} to the cart")
    button.click()


def remove_from_cart(item_title, button):
    log(f"Removing {item_title} from cart the cart")
    button.click()


# This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome(options=chrome_options) as driver:
    # Set maximum time to wait for element to load
    wait = WebDriverWait(driver, 10)

    # Get URL
    driver.get(URL)
    log(f"At home page - {URL}")

    login("standard_user", "secret_sauce", driver)

    log("User successfully logged in")

    # Find all inventory items
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    log("Adding all items to the cart ...")

    # Add all items to the cart
    for item in inventory_items:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        button = item.find_element(
            By.CSS_SELECTOR, "button[class='btn_primary btn_inventory']"
        )
        add_to_cart(title, button)

    # Navigate to cart
    log("Navigating to cart page")
    cart_button = driver.find_element(
        By.CSS_SELECTOR, "a[class='shopping_cart_link fa-layers fa-fw']"
    )
    cart_button.click()
    log("Now on cart page")

    # Remove all items from cart
    log("Removing all items from the cart")

    # Find cart items
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")

    for item in cart_items:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        button = item.find_element(
            By.CSS_SELECTOR, "button[class='btn_secondary cart_button']"
        )
        remove_from_cart(title, button)

    log("Successfully logged in, added all items to cart and removed all items.")
    write_log()
