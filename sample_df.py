import pandas as pd
import random
from datetime import datetime, timedelta


def create_test_df(num_rows):
    # create random string of 10 characters
    def random_string():
        letters = 'abcdefghijklmnopqrstuvwxyz'
        return ''.join(random.choice(letters) for i in range(10))

    # random date between 2010 and 202
    def random_date():
        time_delta = datetime(2020, 1, 1) - datetime(2000, 1, 1)
        random_days = random.randint(0, time_delta.days)
        return datetime(2000, 1, 1) + timedelta(days=random_days)

    # set columns and data
    data = {
        'string': [random_string() for s in range(num_rows)],
        'integer_num': [random.randint(1000, 9999) for i in range(num_rows)],
        'float_num': [round(random.uniform(10, 100), 2) for f in range(num_rows)],
        'boolean': [random.randint(0, 1) for b in range(num_rows)],
        'dates': [random_date().strftime('%Y-%m-%d') for d in range(num_rows)]
    }

    sample_df = pd.DataFrame(data)
    return sample_df


