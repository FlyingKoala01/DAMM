# DAMM project

## Manual installation

Follow these steps to locally host the new Damm Ranking Leaderboard:

### Prerequisites

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

### Install dependencies

Change directory to project base path and run:

```
python3 -m pip install -r requirements.txt
npm install
```

### Set up database

...

```
python3 db_init.py
```

### Compile CSS

Run each time you change something tailwind-related:

```
npm run create-css
```

If you want it to automatically recompile all CSS every time a file changes, run `npm run create-css-forever` instead.

### Run

Simple! Just go to the project folder and type:

```
python3 app.py
```

Run `python3 app.py --listen-all` if you wish to accept TCP
connections from other IP addresses than localhost.

Have the environment variable `export PRODUCTION=True` to run in a production
server (without the debug mode, for example).
