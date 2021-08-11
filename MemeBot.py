from InstaBot import InstaBot
import os

bot = InstaBot('derbgang','FaTaLgAnG!0212!')
bot.login()

#bot.monitorDms()

post = bot.downloadPhoto(['savagerealms.jemima','cursed.image5'],photo=True,random_post=True,single_post=True)

files = os.listdir(os.getcwd()+'/'+str(post[1])+'/')
img_files = list(filter(lambda x: '.jpg' in x, files))

bot.uploadPhoto(os.getcwd()+'/'+str(post[1])+'/'+img_files[0],'Follow @derbgang',request_approval=True,media_id=post[0].mediaid,user=post[0].owner_username)