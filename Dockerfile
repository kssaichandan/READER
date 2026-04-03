FROM python:3.12-slim

WORKDIR /app

COPY . /app

ENV PORT=10000

EXPOSE 10000

CMD ["sh", "-c", "python -m http.server ${PORT:-10000} --bind 0.0.0.0 --directory /app"]
