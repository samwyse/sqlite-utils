# sqlite-utils
<!---
[![PyPI](https://img.shields.io/pypi/v/sqlite-utils.svg)](https://pypi.org/project/sqlite-utils/)
[![Changelog](https://img.shields.io/github/v/release/simonw/sqlite-utils?include_prereleases&label=changelog)](https://sqlite-utils.datasette.io/en/stable/changelog.html)
[![Python 2.7](https://img.shields.io/pypi/pyversions/sqlite-utils.svg?logo=python&logoColor=white)](https://pypi.org/project/sqlite-utils/)
[![Tests](https://github.com/simonw/sqlite-utils/workflows/Test/badge.svg)](https://github.com/simonw/sqlite-utils/actions?query=workflow%3ATest)
[![Documentation Status](https://readthedocs.org/projects/sqlite-utils/badge/?version=stable)](http://sqlite-utils.datasette.io/en/stable/?badge=stable)
[![codecov](https://codecov.io/gh/simonw/sqlite-utils/branch/main/graph/badge.svg)](https://codecov.io/gh/simonw/sqlite-utils)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/sqlite-utils/blob/main/LICENSE)
[![discord](https://img.shields.io/discord/823971286308356157?label=discord)](https://discord.gg/Ass7bCAMDw)
--->
Python CLI utility and library for manipulating SQLite databases, back-ported to Jython/Python 2.7.

## Some feature highlights

- [Pipe JSON](https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-json-data) (or [CSV or TSV](https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-csv-or-tsv-data)) directly into a new SQLite database file, automatically creating a table with the appropriate schema
- [Run in-memory SQL queries](https://sqlite-utils.datasette.io/en/stable/cli.html#querying-data-directly-using-an-in-memory-database), including joins, directly against data in CSV, TSV or JSON files and view the results
- [Configure SQLite full-text search](https://sqlite-utils.datasette.io/en/stable/cli.html#configuring-full-text-search) against your database tables and run search queries against them, ordered by relevance
- Run [transformations against your tables](https://sqlite-utils.datasette.io/en/stable/cli.html#transforming-tables) to make schema changes that SQLite `ALTER TABLE` does not directly support, such as changing the type of a column
- [Extract columns](https://sqlite-utils.datasette.io/en/stable/cli.html#extracting-columns-into-a-separate-table) into separate tables to better normalize your existing data

Read more on my blog, in this series of posts on [New features in sqlite-utils](https://simonwillison.net/series/sqlite-utils-features/) and other [entries tagged sqliteutils](https://simonwillison.net/tags/sqliteutils/).

## Installation

    pip install sqlite-utils

Or if you use [Homebrew](https://brew.sh/) for macOS:

    brew install sqlite-utils

## Using as a CLI tool

Now you can do things with the CLI utility like this:

    $ sqlite-utils memory dogs.csv "select * from t"
    [{"id": 1, "age": 4, "name": "Cleo"},
     {"id": 2, "age": 2, "name": "Pancakes"}]

    $ sqlite-utils insert dogs.db dogs dogs.csv --csv
    [####################################]  100%

    $ sqlite-utils tables dogs.db --counts
    [{"table": "dogs", "count": 2}]

    $ sqlite-utils dogs.db "select id, name from dogs"
    [{"id": 1, "name": "Cleo"},
     {"id": 2, "name": "Pancakes"}]

    $ sqlite-utils dogs.db "select * from dogs" --csv
    id,age,name
    1,4,Cleo
    2,2,Pancakes

    $ sqlite-utils dogs.db "select * from dogs" --table
      id    age  name
    ----  -----  --------
       1      4  Cleo
       2      2  Pancakes

You can import JSON data into a new database table like this:

    $ curl https://api.github.com/repos/simonw/sqlite-utils/releases \
        | sqlite-utils insert releases.db releases - --pk id

Or for data in a CSV file:

    $ sqlite-utils insert dogs.db dogs dogs.csv --csv

`sqlite-utils memory` lets you import CSV or JSON data into an in-memory database and run SQL queries against it in a single command:

    $ cat dogs.csv | sqlite-utils memory - "select name, age from stdin"

See the [full CLI documentation](https://sqlite-utils.datasette.io/en/stable/cli.html) for comprehensive coverage of many more commands.

## Using as a library

You can also `import sqlite_utils` and use it as a Python library like this:

```python
import sqlite_utils
db = sqlite_utils.Database("demo_database.db")
# This line creates a "dogs" table if one does not already exist:
db["dogs"].insert_all([
    {"id": 1, "age": 4, "name": "Cleo"},
    {"id": 2, "age": 2, "name": "Pancakes"}
], pk="id")
```

Check out the [full library documentation](https://sqlite-utils.datasette.io/en/stable/python-api.html) for everything else you can do with the Python library.

## Related projects

* [Datasette](https://datasette.io/): A tool for exploring and publishing data
* [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite): Convert CSV files into a SQLite database
* [db-to-sqlite](https://github.com/simonw/db-to-sqlite): CLI tool for exporting a MySQL or PostgreSQL database as a SQLite file
* [dogsheep](https://dogsheep.github.io/): A family of tools for personal analytics, built on top of `sqlite-utils`
