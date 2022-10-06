# simple_news_aggregator
Простой аггрегатор новостей.

Для работы неоходимо добавить в файл `telegram_parser.py` параметры из [my.telegram.org](https://my.telegram.org)
- `api_id = <Твой api_id>`
- `api_hash = <Твой api_hash>`

В файл `main.py` свой канал, куда будут сливаться новости из всех парсеров (нужно быть администратором этого канала)
- `channel_habr_agg = <Твой телеграм канал>`
