import argparse

from db_settings import init_db as init_database
from blog.app import app


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-idb', '--init_database', action='store_true')
    args = parser.parse_args()

    if not args.init_database:
        app.run()
    else:
        init_database.main()
