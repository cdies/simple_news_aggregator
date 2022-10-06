import httpx
import asyncio
from collections import deque

from telegram_parser import telegram_parser
from rss_parser import rss_parser
from bcs_parser import bcs_parser


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Канал куда скидываем новости, например @habr_agg, сюда введи свой канал
channel_habr_agg = 'https://t.me/habr_agg'

# Очередь из уже опубликованных постов, чтобы их не дублировать
posted_q = deque(maxlen=40)

# 50 первых символов от текста новости - это ключ для проверки повторений
n_test_chars = 50


async def send_message_func(message):
    '''Отправляет посты в канал'''
    await client.send_message(entity=channel_habr_agg, message=message)


# Телеграм парсер
client = telegram_parser(send_message_func, loop)

httpx_client = httpx.AsyncClient()

# Добавляет в текущий event_loop rss парсер
loop.create_task(rss_parser(httpx_client, posted_q,
                 n_test_chars, send_message_func))

# Добавляет в текущий event_loop парсер сайта bcs-express.ru
loop.create_task(bcs_parser(httpx_client, posted_q,
                                   n_test_chars, send_message_func))


# Запускает все парсеры
client.run_until_disconnected()
