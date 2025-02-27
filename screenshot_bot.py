import os
import time
import pyautogui
from datetime import datetime
import telegram
import asyncio

# Замените на ваш токен бота
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
# Замените на ваш ID чата
CHAT_ID = "YOUR_CHAT_ID"

async def send_screenshot():
    try:
        # Создаем скриншот
        screenshot = pyautogui.screenshot()
        
        # Генерируем имя файла с текущей датой и временем
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(filename)
        
        # Отправляем файл в Telegram
        bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
        with open(filename, 'rb') as photo:
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=photo,
                caption=f"Скриншот от {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
        
        # Удаляем временный файл
        os.remove(filename)
        print(f"Скриншот успешно отправлен: {filename}")
        
    except Exception as e:
        print(f"Ошибка при отправке скриншота: {str(e)}")

async def main():
    print("Бот запущен. Скриншоты будут отправляться каждый час.")
    while True:
        await send_screenshot()
        # Ждем 1 час
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main()) 