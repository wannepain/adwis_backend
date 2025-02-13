# # syntax=docker/dockerfile:1

# ARG PYTHON_VERSION=3.11.9
# FROM python:${PYTHON_VERSION}-slim as base

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# COPY requirements.txt requirements.txt  
# RUN python -m pip install -r requirements.txt

# # ✅ Add this to download and link the spaCy model
# RUN python -m spacy download en_core_web_sm && \
#     python -m spacy link en_core_web_sm en

# # Switch to non-privileged user
# USER appuser

# COPY . .

# ENV PORT=8080

# EXPOSE 8080

# CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "src.app:app"]

# syntax=docker/dockerfile:1

# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

COPY requirements.txt requirements.txt  
RUN python -m pip install -r requirements.txt

# ✅ Add this to download the spaCy model
RUN python -m spacy download en_core_web_sm

# Switch to non-privileged user
USER appuser

COPY . .

ENV PORT=8080

EXPOSE 8080

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "src.app:app"]