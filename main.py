import logging

from gui.mainWindow import App
from logger import setup_logger
if __name__ == "__main__":
    setup_logger()
    logging.getLogger(__name__).info("程序开始运行")
    app = App()
    app.run()

