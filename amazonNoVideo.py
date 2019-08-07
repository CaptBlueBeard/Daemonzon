from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AmazonBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        # not using this, too many problems staying logged in.
        # Better if user just logs in
        bot = self.bot
        bot.get('https://www.amazon.com/ap/signin?clientContext=134-3094089-8040603&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fga%2Fp%2F35b14230629c5fae&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_giveaway_exp_na&openid.mode=checkid_setup&marketPlaceId=ATVPDKIKX0DER&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=loginCheckout-amzn_giveaway_exp_na_amazon&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=2147483647&siteState=clientContext%3D132-3593858-4404428%2CsourceUrl%3Dhttps%253A%252F%252Fwww.amazon.com%252Fga%252Fp%252F35b14230629c5fae%2Csignature%3Dnull')
        time.sleep(7)
        email = bot.find_element_by_id('ap_email')
        password = bot.find_element_by_id('ap_password')
        email.clear
        password.clear
        email.send_keys(self.email)
        time.sleep(5)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        # password.submit()

    def enterGiveaway(self):
        bot = self.bot
        bot.get('https://www.amazon.com/ga/giveaways')
        input('Log into Amazon then press Enter ')
        bot.get('https://www.amazon.com/ga/giveaways')
        time.sleep(5)
        giveaways = bot.find_elements_by_class_name('standard-card')
        links = [elem.find_element_by_css_selector(
            'a').get_attribute('href') for elem in giveaways]
        for link in links:
            bot.get(link)
            time.sleep(5)
            try:
                box = bot.find_element_by_link_text(
                    'Tap the box to see if you win')
                box.click()
                print("Entered")
                time.sleep(5)
            except Exception as ex:
                print('error clicking the box')
                time.sleep(5)

        #giveaways = bot.find_elements_by_class_name('a-link-normal item-link')
        #links = [elem.get_attribute('href') for elem in giveaways]


daemon = AmazonBot('notanemail@nope.com', 'youWish')
# daemon.login()
daemon.enterGiveaway()
