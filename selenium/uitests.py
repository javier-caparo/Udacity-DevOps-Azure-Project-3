# #!/usr/bin/env python
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

#datetime.now().strftime("%m-%d-%y %H:%M:%S")

login_url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'

def create_driver():
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless") 
    return webdriver.Chrome(options=options)
    

# Start the browser and login with standard_user
def test_login (driver, user, password):
    print ('Test: login. Navigating to the demo page to login {}'.format(login_url))
    driver.get(login_url)
    print ('Login attempt, user: {},  password: {}'.format(user, password))
    driver.find_element_by_id('user-name').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    #print ('Assert in inventory page. ')
    assert inventory_url in driver.current_url
    #print ('User successfully logged in.')
    print ('Test Login Success.')
    

def test_add_items_to_cart(driver):
    items_in_cart = []
    print ('Test: adding items to cart')
    elements = driver.find_elements_by_class_name('inventory_item')
    #print('Total items to add: {}'.format(len(elements)))
    for item in elements:
        item_name = item.find_element_by_class_name('inventory_item_name').text
        items_in_cart.append(item_name)
        item.find_element_by_class_name('btn_inventory').click()
        print('Added {} to cart'.format(item_name))
    #print ('Assert in cart icon to reflect {} items added.'.format(len(elements)))
    cart_element = driver.find_element_by_class_name('shopping_cart_badge')
    assert int(cart_element.text) == len(elements)
    #print ('Navigate to cart and assert items in cart.')
    driver.find_element_by_class_name('shopping_cart_link').click()
    #print ('Assert in cart page. ')
    assert cart_url in driver.current_url
    #print ('Assert items in cart. ')
    for item in driver.find_elements_by_class_name('inventory_item_name'):
        assert item.text in items_in_cart
    #print ('Asserted items in cart ') 
    print ('Test Add Items in cart Success.')


def test_remove_items_from_cart(driver):
    print ('Test: removing items from cart')
    #print ('Navigate to cart and assert items in cart.')
    driver.find_element_by_class_name('shopping_cart_link').click()
    #print ('Assert in cart page.')
    assert cart_url in driver.current_url

    print("Items in Cart: {}".format(len(driver.find_elements_by_class_name('cart_item'))))
    
    #print('Remove all items from cart.')
    for item in driver.find_elements_by_class_name('cart_item'):
        item_name = item.find_element_by_class_name('inventory_item_name').text
        item.find_element_by_class_name('cart_button').click()
        print('Removed {} from cart'.format(item_name))

    #print('Assert cart is empy')
    #print("Items in Cart: {}".format(len(driver.find_elements_by_class_name('cart_item'))))
    assert len(driver.find_elements_by_class_name('cart_item')) == 0
    #print('Cart empty.')
    print ('Test Remove Items from cart Success.')


def run_ui_tests():
    driver = create_driver()
    #print("Browser started successfully.")
    print("UI Tests started")
    
    print("####################################### - test login user")
    test_login(driver, 'standard_user', 'secret_sauce')
    print("####################################### - test add items to cart")
    test_add_items_to_cart(driver)
    print("####################################### - test remove items from cart")
    test_remove_items_from_cart(driver)

    print("UI Tests completed.")
    driver.quit()

if __name__ == "__main__":
    run_ui_tests()