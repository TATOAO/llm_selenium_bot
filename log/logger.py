import logging
from logging.handlers import RotatingFileHandler

# Create logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages
fh = RotatingFileHandler('log/app.log', maxBytes=3 * 1024 *1024, backupCount=1)
fh.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
fh.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(fh)



