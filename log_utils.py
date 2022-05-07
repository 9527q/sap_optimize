import json
import logging
from logging.handlers import RotatingFileHandler

DEFAULT_LOGGER = logging.getLogger(__name__)


def set_base_config():
    logging.basicConfig(
        **dict(  # fool pycharm inspection
            level=logging.DEBUG,
            format=json.dumps(  # json，方便解析
                dict(
                    levelname="%(levelname)s",
                    asctime="%(asctime)s",
                    filename="%(filename)s",
                    funcName="%(funcName)s",
                    name="%(name)s",
                    lineno="%(lineno)s",
                    message="%(message)s",
                )
            ).replace('"%(message)s"', "%(message)s"),
            handlers=[
                logging.StreamHandler(),
                RotatingFileHandler(
                    filename="./log.log", maxBytes=1024 * 1024
                ),
            ],
        )
    )


def log4json(
    logger: logging.Logger = None,
    level: int = logging.INFO,
    /,
    **log_content,
):
    """记日志，自动完成 json 转换"""
    if logger is None:
        logger = DEFAULT_LOGGER

    logger.log(
        level=level,
        msg=json.dumps(log_content, ensure_ascii=False),
        stacklevel=3,
    )


def log_error4json(logger: logging.Logger = None, /, **log_content):
    log4json(logger, logging.ERROR, **log_content)
