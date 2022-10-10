https://habr.com/ru/post/689520/

# Свой агрегатор новостей на python. Телеграм + RSS + новостные сайты (telethon, feedparser, scrapy)

### Простой аггрегатор новостей.

Для работы неоходимо добавить в файл `telegram_parser.py` параметры из [my.telegram.org](https://my.telegram.org)
- `api_id = <Твой api_id int>`
- `api_hash = <Твой api_hash str>`

В файл `main.py` свой канал, куда будут сливаться новости из всех парсеров (нужно быть администратором этого канала)
- `channel_habr_agg = <Твой телеграм канал str>`



<br/><br/>
---
[![](https://habrastorage.org/webt/gz/gc/i6/gzgci6pivvdnk-gmj-kepml5q9y.gif)](https://yoomoney.ru/to/4100117863420642)
