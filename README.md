## Иерархия файлов и папок:

```
├── .env
├── .gitignore
├── [Папка] bot
│   ├── __init__.py
│   ├── [Папка] core
│   │   ├── __init__.py
│   │   ├── bot.py
│   │   ├── dispatcher.py
│   │   └── scheduler.py
│   ├── [Папка] data
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── [Папка] database
│   │   ├── database.db
│   │   └── sqlite3.py
│   ├── [Папка] filters
│   │   ├── __init__.py
│   │   └── filters.py
│   ├── [Папка] handlers
│   │   ├── __init__.py
│   │   ├── [Папка] admin
│   │   │   ├── __init__.py
│   │   │   └── admin_info.py
│   │   ├── help.py
│   │   ├── start.py
│   │   └── [Папка] user
│   │       └── __init__.py
│   ├── [Папка] keyboards
│   │   ├── inline.py
│   │   └── reply.py
│   ├── [Папка] library
│   │   └── __init__.py
│   ├── [Папка] middlewares
│   │   ├── __init__.py
│   │   └── misc.py
│   └── [Папка] utils
│       ├── __init__.py
│       ├── helpers.py
│       └── logger.py
├── [Папка] logs
│   └── bot.log
└── main.py
```