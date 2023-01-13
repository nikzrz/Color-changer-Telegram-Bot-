import os
import subprocess
from PIL import Image
from telegram.ext import Updater, MessageHandler, Filters

def black_and_white(image_path):
    image = Image.open(image_path)
    image = image.convert('L')
    return image

def handle_image(bot, update):
    file_id = update.message.photo[-1].file_id
    newFile = bot.get_file(file_id)
    newFile.download('temp.jpg')
    image = black_and_white('temp.jpg')
    image.save('temp.jpg')
    bot.send_photo(chat_id=update.message.chat_id, photo=open('temp.jpg', 'rb'))
    os.remove('temp.jpg')

def main():
    updater = Updater(YOUR_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.photo, handle_image))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
