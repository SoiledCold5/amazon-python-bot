from selenium import webdriver
from time import sleep

CARD_TO_BUYS = [
    "https://www.amazon.com/MSI-GeForce-RTX-3060-12G/dp/B08WPJ5P4R/ref=sr_1_2?dchild=1&keywords=3060+rtx&qid=1619637512&refinements=p_85%3A2470955011&rnid=2470954011&rps=1&sr=8-2",
    "https://www.amazon.com/ASUS-Graphics-DisplayPort-Military-Grade-Certification/dp/B08WHJPBFX/ref=sr_1_1?dchild=1&keywords=asus+3060+rtx&qid=1619637575&sr=8-1",
    "https://www.amazon.com/EVGA-GeForce-12G-P5-3657-KR-Dual-Fan-Backplate/dp/B08WM28PVH/ref=sr_1_2?dchild=1&keywords=evga+3060+rtx&qid=1619637588&sr=8-2",
    "https://www.amazon.com/ZOTAC-GeForce-Graphics-IceStorm-ZT-A30600H-10M/dp/B08W8DGK3X/ref=sr_1_5?dchild=1&keywords=RTX+3060&qid=1619754618&sr=8-5",
    "https://www.amazon.com/ZOTAC-GeForce-Graphics-IceStorm-ZT-A30600E-10M/dp/B08ZZW34T3/ref=sr_1_6?dchild=1&keywords=RTX+3060&qid=1619754618&sr=8-6",
    "https://www.amazon.com/GIGABYTE-GeForce-Graphics-WINDFORCE-GV-N3060GAMING/dp/B08X4V8N5Q/ref=sr_1_7?dchild=1&keywords=RTX+3060&qid=1619754618&sr=8-7",
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
