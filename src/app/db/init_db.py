import logging

from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

# from src.app.db import base  # noqa: F401
# from src.app.db import base
from src.app.db.session import engine

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))

    with engine.connect() as con:
        with open("src/app/db/init_db.min.sql") as file:
            query = text(file.read())
            con.execute(query)

def main() -> None:
    logger.info("Initializing service")
    init_db()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()