FROM python:3.11.3
WORKDIR /opt/whitelable-wiki
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY requirements.txt /opt/whitelable-wiki
RUN pip install -r requirements.txt
COPY manage.py /opt/whitelable-wiki/
COPY whitelable_wiki /opt/whitelable-wiki/whitelable_wiki/
COPY wikibackend /opt/whitelable-wiki/wikibackend/

COPY env_template /opt/whitelable-wiki/env_template
COPY entry.sh /opt/whitelable-wiki/entry.sh

EXPOSE 8000
CMD ["bash", "entry.sh"]
