#start db
export $(grep -v '^#' .env | xargs -d '\n')

mariadb -u c8gd2s -p < src/app/db/init_db.min.sql

# Run migrations
cd src/alembic && alembic upgrade head