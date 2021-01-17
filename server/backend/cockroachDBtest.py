import random
from math import floor
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cockroachdb.sqlalchemy import run_transaction
from flask import jsonify

import time
import random
import logging
from argparse import ArgumentParser, RawTextHelpFormatter

import psycopg2
from psycopg2.errors import SerializationFailure


def createQuestions(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS interviewQs (id integer primary key, question VARCHAR not null)"
        )
        # cur.execute("INSERT INTO interviewQs (id, question) VALUES (1, 'Tell me about yourself')")
        logging.debug("createQuestions(): status message: %s", cur.statusmessage)
    conn.commit()

def printQuestion(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM interviewQs")
        logging.debug("printQuestion(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        for row in rows:
            print(row)


def parse_cmdline():
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "dsn",
        help="database connection string\n\n"
             "For cockroach demo, use postgres://user@trusty-lemur-8c3.gcp-northamerica-northeast1.cockroachlabs.cloud:26257/danielye?sslmode=verify-full&sslrootcert=/Users/michaelchang/Desktop/certs/trusty-lemur-ca.crt,\n"
             "with the username and password created in the demo cluster, and the hostname and port listed in the\n"
             "(sql/tcp) connection parameters of the demo cluster welcome message."
    )

    parser.add_argument("-v", "--verbose",
                        action="store_true", help="print debug info")

    opt = parser.parse_args()
    return opt

def main():
    # opt = parse_cmdline()
    # conn = psycopg2.connect(opt.dsn)

    # conn.close()

    conn = psycopg2.connect(
    host="localhost",
    database="michaelchang",
    user="michaelchang",
    password="domics2017")

    createQuestions(conn)

    printQuestion(conn)

    conn.close()

if __name__ == "__main__":
    main()