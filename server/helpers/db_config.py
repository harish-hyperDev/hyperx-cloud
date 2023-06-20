from .loaders import MonogDBClient
from . import config as Config

db = MonogDBClient[Config.MONGO_DB_NAME]
