# Stage 1: Build
FROM python:3.6-slim-buster AS build

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --user --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Run
FROM debian:buster-slim AS run

WORKDIR /app

COPY --from=build /root/.local /root/.local
COPY --from=build /app /app

ENV PATH=/root/.local/bin:$PATH \
    FLASK_APP=app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]