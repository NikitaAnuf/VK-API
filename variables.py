import os
import datetime

from dotenv import load_dotenv


# Мой ID пользователя
BASE_VK_USER_ID = '240664024'

# Абсолютный путь к папке results, где по умолчанию будут храниться результаты
BASE_RESULT_FILE = os.path.join(
    os.path.dirname(__file__), 'results', datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.json')

# Записываем варианты адресов API, если не сработает один, будет обращение по второму
SERVER_ADDRESS_OPTIONS = ['api.vk.com', 'api.vk.ru']

# Протестированная версия VK API
TESTED_VK_API_VERSION = '5.199'

# Получаем токен API из файла .env
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
