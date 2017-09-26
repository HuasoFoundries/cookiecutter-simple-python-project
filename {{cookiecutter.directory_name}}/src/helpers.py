import logging

import src.constants as __CONST


def init_logging():
    """
    TODO
    """
    logging.basicConfig(
        level=__CONST.LOG_LEVEL,
        format='%(asctime)-15s %(name)-20s %(levelname)-8s %(message)s')
