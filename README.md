<h1 align="center">Иерархия файлов и папок:</a>

<h3 style="font-family: 'JetBrains Mono'">
├── .env<br>
├── .gitignore<br>
├── [Папка] bot<br>
│   ├── __init__.py<br>
│   ├── [Папка] core<br>
│   │   ├── __init__.py<br>
│   │   ├── bot.py<br>
│   │   ├── dispatcher.py<br>
│   │   └── scheduler.py<br>
│   ├── [Папка] data<br>
│   │   ├── __init__.py<br>
│   │   └── settings.py<br>
│   ├── [Папка] database<br>
│   │   ├── database.db<br>
│   │   └── sqlite3.py<br>
│   ├── [Папка] filters<br>
│   │   ├── __init__.py<br>
│   │   └── filters.py<br>
│   ├── [Папка] handlers<br>
│   │   ├── __init__.py<br>
│   │   ├── [Папка] admin<br>
│   │   │   ├── __init__.py<br>
│   │   │   └── admin_info.py<br>
│   │   ├── help.py<br>
│   │   ├── start.py<br>
│   │   └── [Папка] user<br>
│   │       └── __init__.py<br>
│   ├── [Папка] keyboards<br>
│   │   ├── inline.py<br>
│   │   └── reply.py<br>
│   ├── [Папка] library<br>
│   │   └── __init__.py<br>
│   ├── [Папка] middlewares<br>
│   │   ├── __init__.py<br>
│   │   └── misc.py<br>
│   └── [Папка] utils<br>
│       ├── __init__.py<br>
│       ├── helpers.py<br>
│       └── logger.py<br>
├── [Папка] logs<br>
│   └── bot.log<br>
└── main.py<br>
