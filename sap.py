import datetime
import json
import os
import traceback
from pathlib import Path

import click

from log_utils import log4json

# import requests


DOMAIN = "http://39.96.36.73:9999/"
BASE_FILE_PATH = "./data/sap"

if not os.path.exists(BASE_FILE_PATH):
    log4json(BASE_FILE_PATH=BASE_FILE_PATH)
    Path(BASE_FILE_PATH).mkdir(parents=True)


@click.command
@click.option("--username", prompt="用户")
@click.password_option(prompt="密码", confirmation_prompt=False)
def login_and_get_session_id(username: str, password: str) -> str:
    print(username)
    print(password)
    return username + password


def get_login_cookie_header(refresh=False) -> dict[str, str]:
    """获取登录使用的 cookie 请求头"""
    file_path = f"{BASE_FILE_PATH}/cookie_header.json"
    header = None

    if not refresh:
        print(1)
        with open(file_path, "w+") as f:
            try:
                header = json.load(f)
                print(1, header)
            except Exception:
                print(1, "exc")
                log4json(
                    file_name=file_path,
                    exc_info=traceback.format_exc(),
                )

    if refresh or not header:
        print(2)
        session_id = login_and_get_session_id()
        header = {"Cookie": f"sessionid={session_id}"}
        print(2, header)
        with open(file_path, "w+") as f:
            json.dump(header, f, ensure_ascii=False)

    return header


def get_city_date_task_info(
    city_name: str, delivery_date: datetime.date
) -> dict:
    """查某城市某日的任务信息
    :param task_name: 城市名，如 西安市
    :param delivery_date: 配送日期（一般是规划任务创建日期的第二天）
    """
    res = get_login_cookie_header()
    print(res)

    # r = requests.post(DOMAIN + "admin/login/", data={
    #     "username": "ike",
    #     "password": "Ding987&",
    # })
    # print(r.text)
    # print(r.headers)
