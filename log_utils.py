import json
import logging
from logging.handlers import RotatingFileHandler

_kwargs = dict(
    level=logging.DEBUG,
    format=json.dumps(
        {
            "levelname": "%(levelname)s",
            "asctime": "%(asctime)s",
            "filename": "%(filename)s",
            "funcName": "%(funcName)s",
            "name": "%(name)s",
            "lineno": "%(lineno)s",
            "message": "%(message)s",
        }
    ).replace('"%(message)s"', "%(message)s"),
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler(filename="./log.log", maxBytes=1024 * 1024),
    ],
)
logging.basicConfig(**_kwargs)

DEFAULT_LOGGER = logging.getLogger(__name__)


def log4json(
    logger: logging.Logger = DEFAULT_LOGGER,
    level: int = logging.INFO,
    /,
    **log_content,
):
    """记日志，自动完成 json 转换"""
    logger.log(
        level=level,
        msg=json.dumps(log_content, ensure_ascii=False),
        stacklevel=3,
    )
