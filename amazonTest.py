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
            'https://www.amazon.com/ga/p/e7a3c434a838315e?fsrc=glp&nav=amz&ref_=aga_p_vg_lp_p1_g21_nodup_dgv')
        time.sleep(5)
        try:
            box = bot.find_element_by_link_text(
                'Tap the box to see if you win')
        except:
            print('no Tap the box')
            box = None
            pass
        if not box is None:
            try:
                box.click()
                print('Entered')
                # bot.find_element_by_class_name('a-text-center box-click-area').click()
            except:
                print('Error clicking the box')
                # time.sleep(5)
                pass

        else:
            video = bot.find_element_by_class_name('youtube-video')
            try:
                video.click()
            except:
                print('could not click video box')
            time.sleep(20)
            continueButton = bot.find_element_by_xpath(
                '//*[@id="reactApp"]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[6]/div/div/div/button')
            continueButton.click()


daemon = AmazonBot('j.matt.lynch@gmail.com', 'Auseabledistraction$$3')
# daemon.login()
daemon.enterGiveaway()
