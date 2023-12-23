FROM python:3.12.1-slim

RUN pip install poetry==1.7.1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Set the working directory to /filed_chatgpt
WORKDIR /opt/filed_chatgpt/

COPY pyproject.toml poetry.lock main.py README.md ./
COPY filed_chatgpt ./filed_chatgpt
RUN poetry install --without dev \
 && rm -rf $POETRY_CACHE_DIR

ENTRYPOINT ["poetry", "run", "python", "-m", "main"]
