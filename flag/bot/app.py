from aiogram import Bot,Dispatcher,types,executor
import requests

token = "7274526995:AAFM1-_B8URpoc-rZLLjdRJgfUbWIgiohNA"

bot = Bot(token=token)

dp = Dispatcher(bot)



flags = requests.get('http://127.0.0.1:8000/api/').json()


# @dp.message_handler()
# async def echo(message: types.Message):
#     davlat = message.text
#     bayroq_url = ""
#     from flag in flags:
#         if davlat == flag["conntry_name"]:
#             bayroq_url = flag['image']
#             bayroq_url = bayroq_url[21:]
#             print(bayroq_url)
#     try:
#         bayroq = types.InputFile(f"...{bayroq_url}")

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Это простой бот")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Чтобы получить помощь, используйте /start")




if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)