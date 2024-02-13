# pyodbc-example

1. Clone this repo.
2. Make virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` or `source venv/Scripts/activate`
4. Upgrade `pip`: `python -m pip install -U pip`
5. Install dependencies: `pip install -U -r requirements.txt`
6. Make directory `instance`
7. Copy an example config to instance and fill out details.
8. Issue a query:

```sh
python query.py instance/your_config.ini 'SELECT * FROM table;'
```
