# Daemonzon
Enter giveaways automatically.

This program was written as a way for me to learn Python.  It's far from perfect and I take no responsibility for any damages caused by the use of this program.  That being said it in no way collects information from you.  The logon is handled strickly by the browser.

# Requirements:
- Python 3.x
- Firefox browser - https://www.mozilla.org/en-US/firefox/new/
- Selenium for Python
  - with the Gecko Driver for Windows - https://github.com/mozilla/geckodriver/

# Requirements for the release(exe):
- Windows
- Firefox

# What does it do?
Daemonzon will open a Firefox browser as remote controlled and navigate to https://www.amazon.com/ga/giveaways/.  It will prompt you to log in, do this in the open Firefox window, then press enter in the console.  Next you will be asked for the starting page and the page you want to stop on.  Finally it will run through all the giveaways on the starting page and then transition to the next page and so on until it reaches your stopping page.


