FROM python:3.12-alpine AS builder

WORKDIR /opt/whitelable-wiki
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /opt/whitelable-wiki/
COPY manage.py /opt/whitelable-wiki/
COPY whitelable_wiki /opt/whitelable-wiki/whitelable_wiki/
COPY wikibackend /opt/whitelable-wiki/wikibackend/

COPY entry.sh /opt/whitelable-wiki/entry.sh

FROM builder AS install
WORKDIR /opt/whitelable-wiki
ENV VIRTUAL_ENV=/opt/whitelable-wiki/venv

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r /opt/whitelable-wiki/requirements.txt

FROM install as run

EXPOSE 8000
CMD ["bash", "entry.sh"]
