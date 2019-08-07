from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from distutils.core import setup
import time
#import py2exe


class AmazonBot:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def login(self):
        # ----------------User Logs In -------------------
        # make sure cookies are allowed in the remote controled Firefox
        bot = self.bot
        bot.get('https://www.amazon.com/ga/giveaways')
        input('Log in on the Firefox browser. Once complete, press Enter here ')

    def enterGiveaway(self, urlIndex, count):
        bot = self.bot
        bot.get('https://www.amazon.com/ga/giveaways/?pageId=' + str(urlIndex))
        time.sleep(5)
        giveaways = bot.find_elements_by_class_name('standard-card')
        links = [elem.find_element_by_css_selector(
            'a').get_attribute('href') for elem in giveaways]
        for link in links:
            print('-----Start of Entry------')
            count += 1
            bot.get(link)
            time.sleep(5)
            try:
                box = bot.find_element_by_link_text(
                    'Tap the box to see if you win')
            except:
                print('No box to click')
                box = None
                pass
            try:
                video = bot.find_element_by_class_name('youtube-video')
            except:
                print('No Video to watch')
                video = None
                pass
            if not box is None:  # reads if box is not NULL
                try:
                    box.click()
                    print('Entered Giveaway')
                    time.sleep(5)
                    # bot.find_element_by_class_name('a-text-center box-click-area').click()
                except:
                    print('Error clicking the box')
                    # time.sleep(5)
                    pass

            elif not video is None:
                # video = bot.find_element_by_class_name('youtube-video')
                try:
                    video.click()
                except:
                    print('Could not click video box')
                time.sleep(20)
                try:
                    continueButton = bot.find_element_by_xpath(
                        '//*[@id="reactApp"]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[6]/div/div/div/button')
                    continueButton.click()
                    print('Entered giveaway')
                except:
                    print('Unable to locate continueButton')
                    print('Giveaway page: ' + str(urlIndex))
                    print(link)
                    pass
                time.sleep(5)
            else:
                print('Already entered')
                time.sleep(5)
            print('-----End of entry-----')
            print(count)
        return count


entryCount = 0
print('Welcome Damonzon will enter giveaways on your behalf')
daemon = AmazonBot()
daemon.login()
# i servers as the URL index
# To skip pages set i to higher number
i = input('Start page: ')
j = input('Stop page: ')
while i < j:
    print('Giveaway Page ' + str(i))
    entryCount = daemon.enterGiveaway(i, entryCount)
    i += 1
