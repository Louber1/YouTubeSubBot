# Free YouTubeSubBot
A 100% free to use YouTube Subscriber Bot for Windows

# How to use:

1. Install Selenium with: pip install selenium==3.141.0
2. Be sure, that Firefox is installed on your System
3. Grab your YouTube Channel ID (The ID is the end of your Channel URL. If https://www.youtube.com/channel/UdfgGIMU3tfdZ6ec-jT8ledfr is your Channel URL, then       UdfgGIMU3tfdZ6ec-jT8ledfr is your ID)
4. Go to https://sonuker.com | https://ytpals.com | https://subpals.com and create an account with the SAME Email/YoutubeID/Password at all of them
5. Edit the configuration.py file and put in your data
6. Excecute the main.py file (Tested with Python 3.8)

# Error Solving:

If Python says "geckodriver excecutable has do be in path" or something like that, edit the main.py file
with Python IDLE and click on RUN + Run module and it should work fine.

If the file closes immediatlely after double click it, try to run it from the Terminal or from IDLE.

The script auto-solves the Google Recaptcha, if the script breaks due to that, just restart it.
Also make shure to NOT go over the Firefox Window with the cursor during the whole login process, otherwise it might not work!

If there's a login error the whole time, please check the configuration.py file again and check if you created an account at all of the sites
with the SAME login data! (https://sonuker.com | https://ytpals.com | https://subpals.com)

# How the script works:

1. First it will login to YouTube with your  account
2. After the it will login to one of the sites (https://sonuker.com | https://ytpals.com | https://subpals.com)
3. There the bot will activate the free Subscriber Plan, but in order to get 10 free subscribers, you have to subscribe to 20 other People, and this is what the Bot
   does for you!
4. After subscribing to all of them, it will open a new window and go to the other sites to repeat the whole procces!
5. So you will get 30 completly free Subscribers, without doing anything. You can start this script every 12 Hours, so you can get up to 60 subscribers per day!
6. Be sure that you can activate the free Plan again, before you start the Script again (Just go to the website and you will see a 12 hour countdown, after you    activated the free Plan)

Please tell me if there are issus, i will try to fix them as soon as possible. I also want to create an .EXE Programm with GUI, to make it evem easier to use, without
having Python istalled ;)
