FROM python:3

WORKDIR /usr/src/app

#fastapi deps
RUN pip install "fastapi[all]"
RUN pip install "python-jose[cryptography]"
RUN pip install "passlib[bcrypt]"
RUN pip install sqlalchemy
RUN pip install alembic
RUN pip install python-dotenv

# COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]