from InstaBot import InstaBot

bot = InstaBot('vocabexpansion','FaTaLvocab!0212!')
bot.login()

vocabImg = bot.generateVocabImg()
bot.uploadPhoto(vocabImg[0],vocabImg[1]+'\n'+'\n'+'Follow us to learn a new word everyday!\n'+'#vocabulary #vocab #grammar #english #vocabexpansion #expandvocab #learning #education #teaching #language')

#bot.bot.unfollow_everyone()

#bot.bot.very_small_delay()

#bot.bot.comment_hashtag('vocab',amount=3)

##### MAKE SURE BOT IS PUT IN A TRY EXCEPT STATEMENT THAT LOOPS ON AN ERROR FOR COMPLETE AUTOMATION ######