import logging

logging.basicConfig(format='%(asctime)s %(message)s', filename='myproject.log', filemode='w',  level=logging.INFO)
logger = logging.getLogger(__name__)

def getlogger():
    return logger
