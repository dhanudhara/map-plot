# Sri Lanka Test Map
- This is a map of Sri Lanka with custom values ploted to the map

## Installation
- Clone the github repo 
```bash
git clone $repo
cd $repo
```
- Setup the python venv to avoid breaking your system
```bash
python -m venv .venv
source .venv/bin/activate
```
- Install the python dependencies needed
```bash
pip install -r requirements.txt
```

- Run the app
```bash
python main.py
```
The app will display an map on your browser.

- You can add more information to the database and display them on the map
```bash
sqlite3 data.db
```
```sqlite3
INSERT INTO locations (location, latitude, longitude, value) VALUES (...)
```

> [!NOTE]
> This repo is a test repo build to test out mapping for the main weather app at https://github.com/arcn-one/weather-app-python-backend