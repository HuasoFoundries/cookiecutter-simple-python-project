#!/usr/bin/env python

import argparse
import configparser
import logging
import time
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

logger = logging.getLogger(__name__ if __name__ != '__main__' else __package__)


def main(no_flag_1: bool,
         flag_2: str,
         db_url: str):
    """
    TODO
    """
    logger.info('Starting'
                ' {}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
    start_total_time = time.time()

    cfg = configparser.ConfigParser()
    cfg.read('config.cfg')
    value1_section = cfg['section']['key1']

    logger.info('Finished execution')
    logger.info('Duration: {} seconds'.format(time.time() - start_total_time))

if __name__ == "__main__":

    log_level = os.environ['LOG_LEVEL']
    db_url = os.environ['DB_URL']

    logging.basicConfig(
        level=log_level,
        format='%(asctime)-15s %(name)-20s %(levelname)-8s %(message)s')

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-no-f1', '--no-flag-1',
                        help='',
                        action='store_false',
                        required=False)
    parser.add_argument('-f2', '--flag-2',
                        type=str,
                        help='',
                        required=False)

    args = parser.parse_args()

    main(args.no_flag_1, args.flag_2, db_url)
