# NULL BOT API wrapper [В РАЗРАБОТКЕ]



![PyPI](https://img.shields.io/pypi/v/null-bot-api)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/null-bot-api)
![GitHub](https://img.shields.io/github/license/lordralinc/null_bot_api)

## Установка 
```shell
pip install -U https://github.com/lordralinc/null_bot_api/archive/master.zip
```

или 

```shell
pip install null_bot_api
```

## Использование

```python
from null_bot_api import NullBotApi

api = NullBotApi()


custom = api.make_request(
    "section.method", 
    data=dict(param1="foo", param2="bar"), 
    dataclass=dict
)
```

```python
# Асинхронное использование
from null_bot_api import NullBotApi

api = NullBotApi()


custom = api.make_request_async(
    "section.method", 
    data=dict(param1="foo", param2="bar"), 
    dataclass=dict
)
```

## Методы

| Секция  | Метод               | Параметры                                            | Описание                                              |
|---------|---------------------|------------------------------------------------------|-------------------------------------------------------|
