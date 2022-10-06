import httpx
import asyncio
from collections import deque
from scrapy.selector import Selector


async def bcs_parser(httpx_client, posted_q,
                            n_test_chars, send_message_func=None):
    '''Кастомный парсер сайта bcs-express.ru'''

    bcs_link = 'https://bcs-express.ru/category'

    while True:
        try:
            response = await httpx_client.get(bcs_link)
        except:
            await asyncio.sleep(20)
            continue

        selector = Selector(text=response.text)

        for row in selector.xpath('//div[@class="feed__list"]/div/div')[::-1]:

            raw_text = row.xpath('*//text()').extract()

            title = raw_text[3]
            summary = raw_text[5]

            news_text = f'{title}\n{summary}'

            head = news_text[:n_test_chars].strip()

            if head in posted_q:
                continue

            if send_message_func is None:
                print(news_text, '\n')
            else:
                await send_message_func(f'bcs-express.ru\n{news_text}')

            posted_q.appendleft(head)

        await asyncio.sleep(10)


if __name__ == "__main__":

    # Очередь из уже опубликованных постов, чтобы их не дублировать
    posted_q = deque(maxlen=20)

    # 50 первых символов от текста новости - это ключ для проверки повторений
    n_test_chars = 50

    httpx_client = httpx.AsyncClient()

    asyncio.run(bcs_parser(httpx_client, posted_q, n_test_chars))
