# Stage 1: Build
FROM python:3.6-slim-buster AS build

WORKDIR /app

COPY . /app

RUN python3 -m pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Run
FROM python:3.6-slim-buster AS run

COPY --from=build /root/.local /root/.local
COPY --from=build /app /app

WORKDIR /app

ENV PATH=/root/.local/bin:$PATH \
    FLASK_APP=app.py \
    FLASK_ENV=production \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

