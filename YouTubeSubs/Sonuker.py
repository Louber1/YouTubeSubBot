from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from selenium import webdriver
import pydub
import urllib
from urllib import request
import speech_recognition
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from configuration import YouTubeId, data_path, Firefox_Headless, loginemail, gmailpass, subpass


def Sonuker():

    options = Options()

    driver = webdriver.Firefox(options=options)

    options.headless = Firefox_Headless

    suburl = "https://sonuker.com"

    def youtubelogin():
        servicelogin = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dde%26next%3D%252F&hl=de&service=youtube&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        driver.get(servicelogin)

        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))).click()
        loginbutton = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        loginbutton.send_keys(loginemail)
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"))).click()
        time.sleep(2)
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))).click()
        passbutton = driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        passbutton.send_keys(gmailpass)
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"))).click()

    def recaptcha():
        time.sleep(random.randint(2, 4))
        frames = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(frames)
        time.sleep(random.randint(2, 4))
        driver.find_element_by_class_name(
            "recaptcha-checkbox-border"
        ).click()
        time.sleep(4)
        driver.switch_to.default_content()
        try:
            frames = driver.find_element_by_xpath(
                "/html/body/div[4]/div[4]"
            ).find_elements_by_tag_name("iframe")
        except:
            frames = driver.find_element_by_xpath(
                "/html/body/div[7]/div[4]"
            ).find_elements_by_tag_name("iframe")
        finally:
            driver.switch_to.frame(frames[0])
            time.sleep(random.randint(2, 4))
            try:
                driver.find_element_by_id(
                    "recaptcha-audio-button"
                ).click()
            except:
                pass

        while True:
            try:
                driver.switch_to.default_content()
                driver.find_elements_by_tag_name("iframe")
                driver.switch_to.frame(frames[-1])
                time.sleep(random.randint(2, 4))

                src = driver.find_element_by_id(
                    "audio-source"
                ).get_attribute("src")
                urllib.request.urlretrieve(src,
                                           data_path + "\\audio.mp3"
                                           )
                pydub.AudioSegment.from_mp3(
                    data_path + "\\audio.mp3"
                ).export(data_path + "\\audio.wav", format="wav")
                recognizer = speech_recognition.Recognizer()
                google_audio = speech_recognition.AudioFile(
                    data_path + "\\audio.wav"
                )
                with google_audio as source:
                    audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language='de-DE')
                inputfield = driver.find_element_by_id("audio-response")
                inputfield.send_keys(text.lower())
                time.sleep(random.randint(2, 4))
                inputfield.send_keys(Keys.ENTER)

            except:
                print("Error, getting a new captcha")
                driver.switch_to.frame(frames[0])
                driver.find_element_by_id("recaptcha-reload-button").click()
                continue
            break

    def vpncaptcha():
        try:
            time.sleep(random.randint(2, 4))
            src = driver.find_element_by_id(
                "audio-source"
            ).get_attribute("src")
            urllib.request.urlretrieve(src,
                                       data_path + "\\audio.mp3"
                                       )
            pydub.AudioSegment.from_mp3(
                data_path + "\\audio.mp3"
            ).export(data_path + "\\audio.wav", format="wav")
            recognizer = speech_recognition.Recognizer()
            google_audio = speech_recognition.AudioFile(
                data_path + "\\audio.wav"
            )
            with google_audio as source:
                audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language='de-DE')
            inputfield = driver.find_element_by_id("audio-response")
            inputfield.click()
            inputfield.send_keys(text.lower())
            inputfield.send_keys(Keys.ENTER)
        except:
            try:
             print("Error, getting new captcha")
             driver.find_element_by_xpath("/html/body/div/div/div[7]/div[2]/div[1]/div[1]/div[1]/button").click()
            except:
                driver.find_element_by_id("recaptcha-audio-button").click()
                time.sleep(1)

    def likeandsubscribe():
        sonuker = driver.window_handles[0]
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR,
                                        'div.step:nth-child(1) > a:nth-child(1)'))).click()
        time.sleep(10)
        youtube = driver.window_handles[1]
        driver.switch_to.window(youtube)
        youtube_url = driver.current_url
        driver.close()
        driver.switch_to.window(sonuker)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(youtube_url)
        time.sleep(3)
        try:
            button = driver.find_element_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]/a")
            ActionChains(driver).move_to_element(button).click(button).perform()
            time.sleep(2)
            button = driver.find_element_by_xpath(
                "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[3]/ytd-video-secondary-info-renderer/div/div[2]/div/ytd-subscribe-button-renderer/paper-button")
            ActionChains(driver).move_to_element(button).click(button).perform()
            time.sleep(4)
            driver.close()
            time.sleep(1)
            driver.switch_to.window(sonuker)
            time.sleep(7)
            confirm = driver.find_element_by_css_selector(
                '#likeSub3 > a:nth-child(1)')
            confirm.click()
        except:
            driver.close()
            time.sleep(1)
            driver.switch_to.window(sonuker)
            skip = driver.find_element_by_xpath(
                "/html/body/div[1]/section/div/div/div/div/div/div[3]/div[2]/div/div[2]/div[4]/a")
            skip.click()
        finally:
            time.sleep(60)

    youtubelogin()
    print("Youtube Login Successfull")
    driver.get(suburl)
    driver.switch_to.default_content()
    WebDriverWait(driver, 5).until(
        ec.element_to_be_clickable((By.XPATH,
                                    '/html/body/main/section[1]/div/div/div[1]/div/a'))).click()
    WebDriverWait(driver, 5).until(
        ec.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/section/div/div/div/div/div/form/div/input'))).click()
    inputElement = driver.find_element_by_xpath("/html/body/div[1]/section/div/div/div/div/div/form/div/input")
    inputElement.send_keys(YouTubeId)
    recaptcha()

    for i in range(5):
        vpncaptcha()

    driver.switch_to.default_content()
    time.sleep(2)
    inputElement = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/div/form/button')

    inputElement.send_keys("\n")
    action = ActionChains(driver)
    WebDriverWait(driver, 5).until(
        ec.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/section/div/div/div/div/div/form/button'))).click()

    WebDriverWait(driver, 5).until(
        ec.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/section/div/div/div/div/div/form/div[2]/input'))).click()
    inputElement = driver.find_element_by_xpath("/html/body/div[1]/section/div/div/div/div/div/form/div[2]/input")
    inputElement.send_keys(subpass)
    WebDriverWait(driver, 5).until(
        ec.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/section/div/div/div/div/div/form/button'))).click()
    try:
        time.sleep(3)
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/a').click()
        print("login Successsfull")
        time.sleep(3)
    except:
        print("login Successsfull")
        pass

    finally:
        while True:
            try:
                likeandsubscribe()
            except:
                driver.quit()
                print("Alle Kanäle Abonniert und geliked, bis zu, Sonuker abgeschlossen")
                break
