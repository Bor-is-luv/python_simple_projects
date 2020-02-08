from selenium import webdriver

keys = {
    "product_url": "https://www.supremenewyork.com/shop/sweatshirts/o5cg0dvs6/ai6lenhg3",
    "name": " ",
    "email": " ",
    "phone_number": " ",
    "address": "aaaa",
    "city": "aaaa",
    "card_number": "1232434354 ",
    "csv": "343 ",
    "zip": "232"
}


def order(k):
    browser = webdriver.Chrome()
    browser.get(k['product_url'])
    browser.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    browser.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    browser.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    browser.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    browser.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone_number"])
    browser.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
    browser.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[3]/div[2]/div[1]/select['
                                  '1]/option[5]').click()
    browser.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
    browser.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])
    browser.find_element_by_xpath('//*[@id="cnb"]').send_keys(k["card_number"])
    browser.find_element_by_xpath('//*[@id="vval"]').send_keys(k["csv"])
    browser.find_element_by_xpath('//*[@id="pay"]/input').click()
    browser.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/[p2]/label/div/ins').click()
    browser.find_element_by_xpath(
        '/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[7]/div[2]/select/option[29]').click()
    browser.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[3]/div[2]/div[1]/select['
                                  '2]/option[3]').click()


if __name__ == '__main__':
    order(keys)
