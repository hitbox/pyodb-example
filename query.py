import argparse
import configparser

import pyodbc

def main(argv=None):
    """
    Query with pyodbc.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('config')
    parser.add_argument('sql')
    args = parser.parse_args(argv)

    cp = configparser.ConfigParser()
    cp.read(args.config)

    connection = pyodbc.connect(**cp['odbc'])
    cursor = connection.cursor()
    for row in cursor.execute(args.sql):
        print(row)

if __name__ == '__main__':
    main()
