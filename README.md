# Fetcher
Fetch multiple URLs concurrently using Python threads

## About Fetcher
Fetcher is a Python script designed to fetch multiple URLs concurrently using Python threads. It allows you to retrieve data from multiple web resources simultaneously, which can be useful for various tasks such as web scraping, API requests, and more.

## Installation
```
git clone https://github.com/hesamz3090/Fetcher.git
```
- Installation on Windows:
```
c:\python3\python.exe -m pip install .
```
- Installation on Linux
```
sudo pip install .
```

## Dependencies:
Fetcher depends on the `requests` python modules.
These dependencies can be installed using the requirements file:


## Usage
| Short Form | Long Form | Description                            |
|------------|-----------|----------------------------------------|
| -i         | --input   | Path to the file containing URLs       |
| -o         | --output  | Path to the output file                |
| -j         | --json    | Output results in JSON format          |
| -c         | --csv     | Output results in CSV format           |
| -w         | --workers | Maximum number of workers (threads)    |
| -v         | --version | Show program's version number and exit |
| -h         | --help    | Show this help message and exit        |

### Examples

* Fetch URLs from urls.txt file and save the results in output.json file in JSON format::

```python fetch_urls.py urls.txt -o output.json -j```

* Fetch URLs from urls.txt file and output the results in CSV format:

``python fetch_urls.py urls.txt -c``

## Using Fetcher as a module in your python scripts

**Example**

```python
import fetcher 
response_list = fetcher.main(urls, max_workers, output_file, output_json, output_csv, return_list)
```
The main function will return a list of unique responses

**Function Usage:**
* **urls**: Path to the file containing URLs.
* **max_workers**: The maximum number of worker threads to use for fetching URLs concurrently.
* **output_file**: Path to the output file.
* **output_json**: Output results in JSON format.
* **output_csv**: Output results in CSV format.
* **return_list**: A flag indicating whether to return the results as a list.


## License
Fetcher is licensed under the MIT license.take a look at the [LICENSE](https://github.com/hesamz3090/Fetcher/blob/main/LICENSE) for more information.

## Version
**Current version is 1.0**