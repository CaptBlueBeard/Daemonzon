from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging


class AmazonBot:
    def __init__(self, logger=None):
        self.bot = webdriver.Firefox()
        # self.logger = logging.getLogger(__name__)

    def login(self):
        # ----------------User Logs In -------------------
        logger.info("User logs in.")
        bot = self.bot
        bot.get('https://www.amazon.com/ga/giveaways')
        input('Log in on the Firefox browser. Once complete, press Enter here ')

    def result(self, link):
        bot = self.bot
        r = None
        try:
            r = bot.find_element_by_xpath(
                '//*[@id="reactApp"]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/span')
        except:
            print('Could not get result.')
            return
        if "you didn't win" in r.text or "You didn't win" in r.text:
            print("You didn't win")
            # print(r.text)
            logger.info("You didn't win")
        elif "You're a Winner" in r.text:
            print("!!!!!!!You won!!!!!!!!!")
            logger.info("!!!!!!!You won!!!!!!!!!:  %s", link)
        else:
            print("Could not determine result")
            print(r.text)
            logger.info("Could not determine result")

    def enterGiveaway(self, urlIndex, count):
        bot = self.bot
        bot.get('https://www.amazon.com/ga/giveaways/?pageId=' + str(urlIndex))
        time.sleep(5)
        giveaways = bot.find_elements_by_class_name('standard-card')
        links = [elem.find_element_by_css_selector(
            'a').get_attribute('href') for elem in giveaways]
        for link in links:
            print('-----Start of Entry------')
            logger.info('Start of Entry: %s', link)
            count += 1
            bot.get(link)
            time.sleep(5)
            try:
                alreadyEntered = bot.find_element_by_xpath(
                    '//*[@id="reactApp"]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/span')
            except:
                print("Error on alreadyEntered.")
                logger.info("Error on alreadyEntered")
                alreadyEntered = None
                pass
            try:
                box = bot.find_element_by_link_text(
                    'Tap the box to see if you win')
                print("There is a box to click")
                logger.info("There is a box to click")
            except:
                print('No box to click')
                logger.info("No box to click")
                box = None
                pass
            try:
                video = bot.find_element_by_class_name('youtube-video')
            except:
                print('No YouTube video to watch')
                logger.info("No youtube video to watch")
                video = None
                pass
            if video is None:
                try:
                    video = bot.find_element_by_class_name('amazon-video')
                except:
                    print('No Amazon video to watch.')
                    logger.info('No Amazon video to watch.')
                    pass
            # start of main if

            if not box is None:  # reads if box is not NULL
                try:
                    box.click()
                    print('Clicked box')
                    logger.info('Clicked box')
                except:
                    print('Error clicking the box')
                    logger.info("Error clicking the box")
                    pass
                time.sleep(5)
                self.result(link)
            elif not video is None:
                try:
                    video.click()
                    print('Watching video.')
                    logger.info('Watching video.')
                    time.sleep(20)
                except:
                    print('Could not click video box')
                    logger.info('Could not click video box')
                    pass
                try:
                    continueButton = bot.find_element_by_xpath(
                        '//*[@id="reactApp"]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[6]/div/div/div/button')
                    continueButton.click()
                    print('Clicked continue to entry')
                    logger.info('Clicked continue to entry')
                except:
                    print(f"Unable to locate continueButton.  URL: {link}")
                    logger.info(
                        "Unable to locate continueButton.  URL: %s", link)
                    pass
                time.sleep(5)
                self.result(link)
            elif not alreadyEntered is None:
                if not "Enter for a chance" in alreadyEntered.text:
                    print("Already entered.")
                    logger.info("Already entered.")
                    time.sleep(5)
            else:
                print(f"Error entering giveaway: {link}")
                logger.info('Error entering giveaway: %s', link)
                time.sleep(5)
            # end of main if chain
            print('-----End of entry-----')
            logger.info("---End of entry---")
            print(count)
            logger.info("Entry count: %s", str(count))
        return count


logFormat = "%(levelname)s %(asctime)s - %(message)s"  # adds date and time
logging.basicConfig(filename=".\\daemonzon.log",
                    level=logging.INFO,
                    format=logFormat,
                    filemode='w')  # rewrite the file so it doesn't get to big.
logger = logging.getLogger()
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
    logger.info("Giveaway Page %s", i)
    entryCount = daemon.enterGiveaway(i, entryCount)
    i += 1
