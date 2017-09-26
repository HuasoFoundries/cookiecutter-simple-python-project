#!/usr/bin/env python

import argparse
import logging
import src.helpers as helpers
import time

logger = logging.getLogger(__name__ if __name__ != '__main__' else __package__)


def main(no_flag_1: bool,
         flag_2: str):
    """
    TODO
    """
    logger.info('Starting'
                ' {}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
    start_total_time = time.time()

    logger.info('Finished execution')
    logger.info('Duration: {} seconds'.format(time.time() - start_total_time))

if __name__ == "__main__":

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

    # Init logging
    helpers.init_logging()

    main(args.no_flag_1, args.flag_2)
