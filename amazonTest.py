from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AmazonBot:
    # __init__(self,username,password) if I want to use those
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    def enterGiveaway(self):
        bot = self.bot
        bot.get('https://www.amazon.com/ga/giveaways')
        input('Log into Amazon then press Enter ')
        bot.get(
            'https://www.amazon.com/ga/p/0ebf2a7d24473ac1?fsrc=glp&nav=amz&ref_=aga_p_vg_lp_p26_g14_nodup_dgv')
        time.sleep(5)
        try:
            followButton = bot.find_element_by_class_name(
                "follow-author-continue-button")
        except:
            followButton = None
            print("No follow button")
            pass
        if not followButton is None:
            try:
                followButton.click()
                print('Clicked Follow')
                # bot.find_element_by_class_name('a-text-center box-click-area').click()
            except:
                print('Error clicking follow')
                # time.sleep(5)
                pass


daemon = AmazonBot('j.matt.lynch@gmail.com', 'Auseabledistraction$$3')
# daemon.login()
daemon.enterGiveaway()
