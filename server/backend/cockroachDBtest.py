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


def main():
    conn = psycopg2.connect(
        host="localhost",
        database="DBname",
        user="userName",
        password="userPassword")

    createQuestions(conn)

    printQuestion(conn)

    conn.close()

if __name__ == "__main__":
    main()