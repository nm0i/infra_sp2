import os
import sqlite3
from typing import Dict, List

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from api_yamdb.settings import BASE_DIR, DATABASES
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = URL.create(
            drivername="postgresql",
            username=DATABASES["default"]["USER"],
            host=DATABASES["default"]["HOST"],
            port=DATABASES["default"]["PORT"],
            password=DATABASES["default"]["PASSWORD"],
            database=DATABASES["default"]["NAME"],
        )
        engine = create_engine(url)
        connection = engine.connect()
        FILE_TABLE_PAIRS: List = map(
            lambda x: (os.path.join(BASE_DIR, x[0]), x[1]),
            (
                ("data/titles.csv", "reviews_title"),
                ("data/users.csv", "users_user"),
                ("data/review.csv", "reviews_review"),
                ("data/category.csv", "reviews_category"),
                ("data/comments.csv", "reviews_comment"),
                ("data/genre_title.csv", "reviews_genretitle"),
                ("data/genre.csv", "reviews_genre"),
            ),
        )
        COLUMN_RENAME_MAP: Dict[str, str] = {
            "category": "category_id",
            "author": "author_id",
        }

        USERS_DEF_RECORD: Dict = {
            "password": "---",
            "is_superuser": False,
            "is_staff": False,
            "is_active": True,
            "confirmation_code": 0,
            "date_joined": pd.to_datetime(0, unit='s'),
            "first_name": "null",
            "last_name": "null",
            "bio": "null",
        }

        for csv_file, table in FILE_TABLE_PAIRS:
            try:
                frame = pd.read_csv(
                    csv_file,
                    sep=",",
                    header=0,
                )
                frame.rename(
                    columns=COLUMN_RENAME_MAP,
                    inplace=True,
                )
                frame.columns
                if table == "users_user":
                    frame_new = frame.assign(**USERS_DEF_RECORD)
                else:
                    frame_new = frame
                frame_new.to_sql(table,
                                 connection,
                                 if_exists="append",
                                 index=False)
                print(f"OK: {csv_file}")
            except Exception as error:
                print(f"ERROR: {error}")
        connection.close()


if __name__ == "__main__":
    Command.handle()
