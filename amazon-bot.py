from selenium import webdriver
from time import sleep

CARD_TO_BUYS = [
    "https://www.amazon.com/GeForce-RTX-3060-12G-P5-3657-KR-Backplate/dp/B092L2KTHD/ref=sr_1_21?crid=QHGK99E7NQLU&dchild=1&keywords=rtx+3060&qid=1621808207&sprefix=rtx%2Caps%2C165&sr=8-21",
]
SLEEP_IN_BETWEEN = 5


class PS5Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.amazon.com')
        sleep(30)

    def checkAndBuyPS5(self):
        succ = False
        while not succ:
            for card in CARD_TO_BUYS:
                self.driver.get(card)
                sleep(1)
                try:
                    add_to_cart = self.driver.find_element_by_id("add-to-cart-button")
                    add_to_cart.click()
                    sleep(1.5)
                    checkout = self.driver.find_element_by_id("hlb-ptc-btn-native") or self.driver.find_element_by_id("hlb-ptc-btn")
                    checkout.click()
                    sleep(1.5)
                    place_order = self.driver.find_element_by_name("placeYourOrder1")
                    place_order.click()
                    sleep(1.5)
                    print(f"succssfully bought {card}")
                except Exception as e:
                    print(e)
                    sleep(1.5)

            sleep(SLEEP_IN_BETWEEN)

bot = PS5Bot()
bot.login()
bot.checkAndBuyPS5()
