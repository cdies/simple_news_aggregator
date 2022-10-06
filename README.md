https://habr.com/ru/post/689520/

# Свой аггрегатор новостей на python, телеграмм + RSS + новостные сайты (telethon, fiddler, scrapy)

### Простой аггрегатор новостей.

Для работы неоходимо добавить в файл `telegram_parser.py` параметры из [my.telegram.org](https://my.telegram.org)
- `api_id = <Твой api_id>`
- `api_hash = <Твой api_hash>`

В файл `main.py` свой канал, куда будут сливаться новости из всех парсеров (нужно быть администратором этого канала)
- `channel_habr_agg = <Твой телеграм канал>`



<br/><br/>
---
[![](https://habrastorage.org/webt/gz/gc/i6/gzgci6pivvdnk-gmj-kepml5q9y.gif)](https://yoomoney.ru/to/4100117863420642)
