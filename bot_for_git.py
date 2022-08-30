import os
import time
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

PEOPLE = {
   "<emploee name>": "<notice text>",
   "John-Snow": "John Snow, bastard of Eddard Stark"
}

API_TOKEN = "<YOUR_BOT_API_TOKEN>"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

path_to_watch = "checked_camera_photos" # <path to load checked images>

class View_to_TG:
   @dp.message_handler(commands=['start'])
   async def start(message: types.Message):
      before = dict([(f, None) for f in os.listdir(path_to_watch)])
      while 1:
         time.sleep(1)
         after = dict([(f, None) for f in os.listdir(path_to_watch)])
         added = [f for f in after if f not in before]
         if added:
            print("Added: ", ", ".join(added))
            before = dict([(f, None) for f in os.listdir(path_to_watch)])
            full_filename = added

            for f_fn in full_filename:
               fn = path_to_watch + "/" + f_fn
               photo = open(fn, 'rb')
               await message.answer_document
               await message.answer_photo(photo)
               messa = PEOPLE.get(f_fn.split("[")[0])
               await message.answer(messa)
               await message.answer(datetime.today().strftime('%Y-%m-%d | %H:%M:%S'))

            added = []

   executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
   View_to_TG
