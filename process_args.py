import argparse
import datetime
import os

from variables import BASE_VK_USER_ID, BASE_RESULT_FILE

def create_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--userid', '-u', type=str, default=BASE_VK_USER_ID)
    parser.add_argument('--filepath', '-f', type=str, default=BASE_RESULT_FILE)

    return parser

def parse_args() -> tuple[str, str]:
    parser = create_argparser()
    args = parser.parse_args()

    vk_user_id = args.userid

    if args.filepath.endswith('.json'):
        result_file = args.filepath
    else:
        result_file = os.path.join(args.filepath, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.json')

    return vk_user_id, result_file
