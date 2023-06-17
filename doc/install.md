# Installation

How to run the server locally?

## Disclaimer

This tutorial isn't meant for everyone. If you wish to try the website, you
can simply go to damm.ericroy.net . The server is a Raspberry Pi, so the
response time will be VERY slow (10 seconds). Apologies for that.

## Prerequisites

- Python 3.6 or higher installed:

```
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3
```

- Node 14 or higher with npm 6.14 or higher:

```
sudo apt install nodejs npm
```

- Sqlite3
```
sudo apt install sqlite3
```

## Install dependencies

Change directory to project base path and run:

```
python3 -m pip install -r requirements.txt
npm install
```

## Set up database

This command will take the data input from the db folder (the data MUST have
the format that you provided to us) and create a database. It will also process
the grades and get reviews from google (when possible).

**WARNING:** This command will take AGES if you're on a big database. If you
received a copy of the project that already has the file `app/damm.db` on it,
you can skip time by not starting the database again.

```
python3 db_init.py
```

## Compile CSS

Run each time you change something tailwind-related (or the first time):

```
npm run create-css
```

If you want it to automatically recompile all CSS every time a file changes,
run `npm run create-css-forever` instead.

## Run

Simple! Just go to the project folder and type:

```
python3 app.py
```

It will open the server on port 5003.

Run `python3 app.py --listen-all` if you wish to accept TCP
connections from other IP addresses than localhost.

Have the environment variable `export PRODUCTION=True` to run in a production
server (without the debug mode, for example).
