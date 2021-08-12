import random
import time
from os import remove

from PIL import Image, ImageDraw, ImageFont
from instabot import Bot
import PIL
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import glob
from pathlib import Path
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import PyDictionary
import argparse
import sys
import instaloader

dictionary=PyDictionary.PyDictionary()

instaLoad = instaloader.Instaloader()
#mod.download_profile('cursed.image5')
#mod.download_pic(filename='user_posts/cursed_image5/test1.jpg')

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

def wait_until_clickable(driver, xpath=None, class_name=None, el_id=None, duration=10, frequency=0.01, click=None):
    el = None
    try:
        if xpath:
            el = WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elif class_name:
            el = WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
        elif el_id:
            el = WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.ID, el_id)))
    except Exception as e:
        print(e)

    if(click):
        el.click()


def wait_until_visible(driver, xpath=None, class_name=None, el_id=None, duration=10, frequency=0.01, text=None):
    el = None
    try:
        if xpath:
            el = WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        elif class_name:
            el = WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
        elif el_id:
            el = WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.ID, el_id)))
    except Exception as e:
        print(e)

    if(text):
        el.send_keys(u'\ue009' + u'\ue003')
        el.send_keys(text)


class InstaBot():
    def __init__(self,username,password):
        self.bot = Bot()

        self.username = username
        self.password = password

        self.deleteCookies()

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument("--start-maximized")
        #options.add_argument("headless")
        options.binary_location = ""
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1200, 700)
        self.idealPostTime = '12:00 PM'

    def 

    def login(self,proxy=None):
        self.bot.login(username=self.username, password=self.password,proxy=proxy)

    def getPostCount(self):
        return(len(next(os.walk(os.getcwd()+'\posts'))[1]))

    def deleteCookies(self):
        try:
            #print(os.getcwd()+'/config/'+self.username+'_uuid_and_cookie.json')
            remove(os.getcwd()+'/config/'+self.username+'_uuid_and_cookie.json')
        except:
            pass

    def convertImg(self,img):
        with Image.open(img) as im:
            im = im.convert('RGB')
            im.save(img.split('.')[0]+'.jpg', 'JPEG')

    def uploadPhoto(self,img,caption,request_approval=None,media_id=None,user=None):
        if(request_approval):
            #self.bot.send_message('yeet','vocabexpansion')
            #self.bot.send_photo('vocabexpansion',img)
            #for post in self.bot.
            media_list = self.bot.get_total_user_medias(user)
            #print(str(media_id).split('_')[0])
            #post = media_list[post_num]
            wait_for_reply = False
            for media in media_list:
                #print(str(media).split('_')[0])
                if(str(media).split('_')[0] ==  str(media_id)):
                    self.bot.send_media(media,'vocabexpansion')
                    #self.bot.very_small_delay()
                    #self.bot.send_message('gay bitch','phrankier')
                    wait_for_reply = True
                    break

            approval = False
            while(wait_for_reply):
                messages = self.bot.get_messages()
                dms = messages['inbox']
                threads = dms['threads'][0]
                last_message = threads['last_permanent_item']
                #print(last_message)
                if('text' in last_message.keys()):
                    text = last_message['text']
                    print(text)
                    if(not(approval)):
                        if(text.lower() == 'yes'):
                            approval=True
                        elif(text.lower() == 'no'):
                            approval=True
                            break
                    elif(text.lower() != 'yes'):
                        self.bot.upload_photo(img,caption=text)
                        wait_for_reply = False

                time.sleep(2)

        else:
            self.bot.upload_photo(img,caption=caption)

    def monitorDms(self):
        messages = self.bot.get_messages()
        for message in messages:
            print(message)

    def downloadPhoto(self,usernames,photo=None,video=None,random_post=None,single_post=None):

        # if username[0] != "@":  # if first character isn't "@"
        #     username = "@" + username
        instaLoad.login('vocabexpansion','FaTaLvocab!0212!')

        username = random.choice(usernames)
        dir = '/user_posts/' + username + '/'
        dir1 = os.getcwd() + dir
        #print(os.getcwd() + dir)
        if not os.path.exists(dir1):
            os.makedirs(dir1)
        os.chdir(dir1)
        #sameUserPosts = str(len(next(os.walk(dir1))) + 1)
        sameUserPosts = sum(os.path.isdir(i) for i in os.listdir(dir1)) + 1
        #print(sameUserPosts)
        profile = instaloader.Profile.from_username(instaLoad.context, username)

        if(photo):
            posts = profile.get_posts()
            if(not(random_post)):
                postNum = 0
            else:
                #int(random.randint(0,posts.count-1))
                postNum = int(random.randint(0, 100))
                #postList = list(posts)
                # while postList[postNum].is_video:
                #     postNum = int(random.randint(0, 100))
                #     print(postNum)

            count = 0
            while(count!=-1):
                for post in posts:
                    if(count == postNum):
                        if(post.is_video or (single_post and post.mediacount>1)):
                            count = 0
                            postNum = int(random.randint(0, 100))
                            break
                        else:
                            #print(post.mediacount)
                            instaLoad.download_post(post, sameUserPosts)
                            return [post,sameUserPosts]
                    #print(count)
                    count+=1
        else:
            print(video)


    def generateVocabImg(self,vocabList=''):

        self.driver.get('https://randomword.com/vocabulary')

        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="random_word"]'))
        )
        vocabWord = el.text

        # definition = dictionary.meaning(vocabWord)
        # print(definition)

        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="random_word_definition"]/span'))
        )
        vocabDefinition = el.text

        # partOfSpeech = definition[1]
        # print(partOfSpeech)
        #
        # vocabDefinition = definition.get()

        print(vocabWord+": "+vocabDefinition)

        bgImg = self.generateShinyImgBg()

        with Image.open(bgImg[1]) as img:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('fonts/OpenSans-Bold.ttf',140)
            font1 = ImageFont.truetype('fonts/OpenSans-Regular.ttf', 50)

            w, h = draw.textsize(vocabWord.upper(), font=font)
            draw.text(((1080-w)/2,360),vocabWord.upper(),(255,255,255),font=font)

            definitionList = vocabDefinition.split(" ")
            str1 = ""
            count = 0
            for word in definitionList:
                if(len(str1)<26):
                    str1+=(word+" ")
                else:
                    w, h = draw.textsize(str1, font=font1)
                    draw.text(((1080 - w) / 2, 560+(count*70)), str1, (255, 255, 255), font=font1)
                    count+=1
                    str1=word+" "

                if(word==definitionList[len(definitionList)-1]):
                    w, h = draw.textsize(str1, font=font1)
                    draw.text(((1080 - w) / 2, 560+(count*70)), str1, (255, 255, 255), font=font1)
                    count+=1
                    str1=""

            img.save(bgImg[0]+'/post.jpg')

            img1 = Image.open(bgImg[0]+'/post.jpg')
            img2 = Image.open(os.getcwd() + '/images/logo3.png')
            img1 = img1.convert('RGBA')
            img2 = img2.convert('RGBA')
            newImg = img2.resize((round(img2.size[0]*0.1), round(img2.size[1]*0.1)))
            img1.paste(newImg,(int((1080/2)-(54)),800),newImg)

            img1.save(bgImg[0] + '/post2.png', format="png")

            img3 = Image.open(bgImg[0] + '/post2.png')
            img3 = img3.convert('RGB')
            img3.save(bgImg[0] + '/post2.jpg')

            self.driver.close()

            return([bgImg[0]+'/post2.jpg',vocabWord])

    def generateShinyImgBg(self):
        self.driver.get('https://bgjar.com/simple-shiny')

        colorList = ['#0E2A47',]

        wait_until_visible(driver=self.driver,xpath='//*[@id="width"]',text="1080")

        wait_until_visible(driver=self.driver,xpath='//*[@id="height"]',text="1080")

        wait_until_clickable(driver=self.driver,xpath='//*[@id="workspace"]/div[1]/div[2]/form/div[8]/button',click=True)
        wait_until_clickable(driver=self.driver, xpath='//*[@id="workspace"]/div[1]/div[2]/form/div[8]/button',click=True)
        time.sleep(2)
        wait_until_clickable(driver=self.driver,xpath='//*[@id="workspace"]/div[2]/div[2]/button[1]',click=True)

        files_path = os.path.join(path_to_download_folder, '*')
        files = sorted(
            glob.iglob(files_path), key=os.path.getctime, reverse=True)

        postNum = self.getPostCount()+1
        #print(files[0])
        drawing = svg2rlg(files[0])

        newFolderDir = os.getcwd()+"/posts/"+str(postNum)
        if not os.path.exists(newFolderDir):
            os.makedirs(newFolderDir)

        renderPM.drawToFile(drawing, newFolderDir+"/test"+str(postNum)+".jpg", fmt="JPG")

        return([newFolderDir,newFolderDir+"/test"+str(postNum)+".jpg"])



# deleteCookies()
# #convertImg('test.png')
#
# bot = Bot()
#
# bot.login(username='vocabexpansion', password='FaTaLvOcAb!0212!')
#
# bot.upload_photo('test.jpg',caption='Minchurgin')


