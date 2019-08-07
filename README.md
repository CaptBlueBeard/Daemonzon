# Daemonzon
Enter giveaways automatically.

This program was written as a way for me to learn Python.  It's far from perfect and I take no responsibility for any damages caused by the use of this program.  That being said it in no way collects information from you.  The logon is handled strickly by the browser.

# Requirements:
- Firefox browser - https://www.mozilla.org/en-US/firefox/new/
  - Set Firefox Cookies and Site Data for amazon.com to allow
    - You will probably need to do this in the Remote Controlled browser once it opens the first time.
- Selenium for Python
  - with the Gecko Driver for Windows - https://github.com/mozilla/geckodriver/

# What does it do?
Daemonzon will open a Firefox browser as remote controled and navagate to https://www.amazon.com/ga/giveaways/.  It will promote you to log in, do this in the open Firefox window, then press enter in the console.  Next you will be asked for the starting page and the page you want to stop on.  Finally it will run through all the giveaways on the starting page and then transition to the next page and so on until it reaches your stopping page.


