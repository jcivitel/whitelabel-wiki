FROM python:3.12-alpine AS builder

RUN apk add --no-cache libgcc mariadb-connector-c pkgconf mariadb-dev postgresql-dev linux-headers

WORKDIR /opt/whitelabel-wiki
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /opt/whitelabel-wiki/
COPY manage.py /opt/whitelabel-wiki/
COPY whitelabel_wiki /opt/whitelabel-wiki/whitelabel_wiki/
COPY wikibackend /opt/whitelabel-wiki/wikibackend/

FROM builder AS install
WORKDIR /opt/whitelabel-wiki
ENV VIRTUAL_ENV=/opt/whitelabel-wiki/venv

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r /opt/whitelabel-wiki/requirements.txt

FROM install as run

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "--noreload", "0.0.0.0:8000"]
