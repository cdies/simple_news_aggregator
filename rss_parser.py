import httpx
import asyncio
from collections import deque
import feedparser


async def rss_parser(httpx_client, posted_q,
                     n_test_chars, send_message_func=None):
    '''Парсер rss ленты'''

    rss_link = 'https://rssexport.rbc.ru/rbcnews/news/20/full.rss'

    while True:
        try:
            response = await httpx_client.get(rss_link)
        except:
            await asyncio.sleep(10)
            continue

        feed = feedparser.parse(response.text)

        for entry in feed.entries[::-1]:
            summary = entry['summary']
            title = entry['title']

            news_text = f'{title}\n{summary}'

            head = news_text[:n_test_chars].strip()

            if head in posted_q:
                continue

            if send_message_func is None:
                print(news_text, '\n')
            else:
                await send_message_func(f'rbc.ru\n{news_text}')

            posted_q.appendleft(head)

        await asyncio.sleep(5)


if __name__ == "__main__":

    # Очередь из уже опубликованных постов, чтобы их не дублировать
    posted_q = deque(maxlen=20)

    # 50 первых символов от текста новости - это ключ для проверки повторений
    n_test_chars = 50

    httpx_client = httpx.AsyncClient()

    asyncio.run(rss_parser(httpx_client, posted_q, n_test_chars))
