import logging

import src.db.extract as extract
import src.db.load as load

logger = logging.getLogger(__name__)


def calculate(db_url):

    df = extract.get_data_example_1(db_url)

    df.describe()

    return None
