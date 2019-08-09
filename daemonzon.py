from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AmazonBot:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def login(self):
        # ----------------User Logs In -------------------
        # make sure cookies are allowed for amazon in the remote controled Firefox
        bot = self.bot
        bot.get('https://www.amazon.com/ga/giveaways')
        input('Log in on the Firefox browser. Once complete, press Enter here ')

    def result(self, link):
        bot = self.bot
        try:
            r = bot.find_element_by_xpath(
                '//*[@id="reactApp"]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/span')
        except:
            print('Could not get result.')
            return
        if "you didn't win" in r.text:
            print("You didn't win")
        elif "You're a Winner" in r.text:
            print("You won!")
            print(link)
        else:
            print("Could not find result")

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
                alreadyEntered = bot.find_element_by_xpath(
                    '//*[@id="reactApp"]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/span')
            except:
                print("Error on alreadyEntered.")
                pass
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
                print('No YouTube video to watch')
                video = None
                pass
            if video is None:
                try:
                    video = bot.find_element_by_class_name('amazon-video')
                except:
                    print('No Amazon video to watch.')
                    pass
            # start of main if

            if not box is None:  # reads if box is not NULL
                try:
                    box.click()
                    print('Entered Giveaway')
                except:
                    print('Error clicking the box')
                    pass
                time.sleep(5)
                self.result(link)
            elif not video is None:
                try:
                    video.click()
                    print('Watching video.')
                    time.sleep(20)
                except:
                    print('Could not click video box')
                    pass
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
                self.result(link)
            elif not "Enter for a chance" in alreadyEntered.text:
                print("Aleady entered.")
                time.sleep(5)
            else:
                print('Error entering giveaway')
                print(link)
                time.sleep(5)
            # end of main if chain
            print('-----End of entry-----')
            print(count)
        return count


entryCount = 0
print('Welcome Daemonzon will enter giveaways on your behalf')
daemon = AmazonBot()
daemon.login()
# i serves as the URL page start index
# j serves as the URL stop page - in case you don't want to do 194 pages
i = int(input('Start page: '))
j = int(input('Stop page: '))
while i < j:
    print('Giveaway Page ' + str(i))
    entryCount = daemon.enterGiveaway(i, entryCount)
    i += 1
