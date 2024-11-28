from process_args import parse_args
from write_json import write_json

from api.users import get_users_info
from api.followers import get_user_followers_info
from api.subscriptions import get_user_subscriptions_info


def run():
    print('Начало работы')

    print('Обработка параметров командной строки')
    try:
        user_id, filepath = parse_args()
    except Exception as ex:
        print(f'Ошибка в чтении аргументов командной строки - {ex.__str__}')
        return 0

    try:
        print('Получение информации о пользователе')
        user_info = get_users_info(user_id)[0]

        print('Получение информации о фолловерах')
        user_followers_info = get_user_followers_info(user_id)

        print('Получение информации о подписках')
        user_subscriptions_users, user_subscriptions_groups = get_user_subscriptions_info(user_id)

    except Exception as ex:
        print(f'Ошибка в получении информации - {ex.__str__}')
        return 0

    print('Формирование общего словаря данных')
    user_info['followers'] = user_followers_info


    user_info['subscriptions'] = {}
    user_info['subscriptions']['users'] = user_subscriptions_users
    user_info['subscriptions']['groups'] = user_subscriptions_groups

    try:
        write_json(user_info, filepath)
    except Exception as ex:
        print(f'Ошибка в записи JSON-файла - {ex.__str__()}')
        return 0

    print('Работа закончена')


if __name__ == '__main__':
    run()
