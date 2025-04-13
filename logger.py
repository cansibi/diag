# logger.py
import logging

def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,  # 设置日志级别，可选：DEBUG, INFO, WARNING, ERROR, CRITICAL
        format='[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
