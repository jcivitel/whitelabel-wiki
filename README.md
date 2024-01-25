[![](https://img.shields.io/maintenance/yes/2024)](https://github.com/jcivitel/)
[![GitHub issues](https://img.shields.io/github/issues/jcivitel/whitelable-wiki)](https://github.com/jcivitel/whitelable-wiki)
[![GitHub Repo stars](https://img.shields.io/github/stars/jcivitel/whitelable-wiki)](https://github.com/jcivitel/whitelable-wiki)
[![GitHub License](https://img.shields.io/github/license/jcivitel/whitelable-wiki)](https://github.com/jcivitel/whitelable-wiki)

# What is the goal of the project?
The general goal of this project is to provide a wiki in which several service providers can be mapped without having to rewrite each topic for each one.

The integration of corporate logos is also planned.


## How to install the project?
1. Begin by cloning the repository to a designated local directory on your machine.
```console
git clone https://github.com/jcivitel/whitelable-wiki.git
```
2. Launch a Command Prompt (CMD) and navigate to the specified directory. Once in the directory, execute the following command:
```python
python -m venv venv
```

3. Once the virtual Python environment has been successfully created, it is now possible to execute the script by the following steps:
```python
. venv/bin/activate
pip install -r reqirements.txt
```

4. To run the server, execute the following command:
```
python manage.py runserver
```

> [!NOTE]
> By default, the runserver command starts the development server on the internal IP at port 8000.
>
> If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:
> ```console
>python manage.py runserver 8080
>```
>
> If you want to change the server’s IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:
> ```console
>python manage.py runserver 0.0.0.0:8080
>```


## Installation by compose-yaml
```yaml
version: "3.3"
services:
  wiki:
    container_name: wiki
    image: jcivitell/whitelable_wiki:latest
    ports:
      - "80:8000/tcp"
    environment:
      SECRET_KEY: '${SECRET_KEY}'
      DEBUG: '${DEBUG}'
      LANGUAGE_CODE: '${LANGUAGE_CODE}'
      TIME_ZONE: '${TIME_ZONE}'
      MAIN_DATABASE_ENGINE: '${MAIN_DATABASE_ENGINE}'
      MAIN_DATABASE_NAME: '${MAIN_DATABASE_NAME}'
      MAIN_DATABASE_USER: '${MAIN_DATABASE_USER}'
      MAIN_DATABASE_PASSWD: '${MAIN_DATABASE_PASSWD}'
      MAIN_DATABASE_HOST: '${MAIN_DATABASE_HOST}'
      MAIN_DATABASE_PORT: '${MAIN_DATABASE_PORT}'
    networks:
      - wiki

  mariadb:
    container_name: db
    image: mariadb:latest
    environment:
      MARIADB_ROOT_PASSWORD: '${MARIADB_ROOT_PASSWORD}'
      MYSQL_DATABASE: '${MAIN_DATABASE_NAME}'
      MYSQL_USER: '${MAIN_DATABASE_USER}'
      MYSQL_PASSWORD: '${MAIN_DATABASE_PASSWD}'
    volumes:
      - 'data:/var/lib/mysql'
    networks:
      - wiki

networks:
  wiki:

volumes:
  data:
```
---

## Contributors
[![Contributors Display](https://badges.pufler.dev/contributors/jcivitel/garrysmod?size=50&padding=5&bots=false)](https://github.com/jcivitel/py_itu_change/graphs/contributors)
