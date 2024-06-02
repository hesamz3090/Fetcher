import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import json
import csv

# Author and banner information
__author__ = "Hesam Aghajani"
__version__ = "1.0"
__description__ = "Fetch multiple URLs concurrently using Python threads"


def fetch_url(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"


def main(urls, max_workers=5, output_file=None, output_json=False, output_csv=False, return_list=False):
    '''
    Fetch multiple URLs concurrently using Python threads.

    Parameters:
    urls (list of str): A list of URLs to be fetched.
    max_workers (int, optional): The maximum number of worker threads to use for fetching URLs concurrently. Default is 5.
    output_file (str, optional): The path to the file where the results will be saved. If not specified, results will not be saved to a file.
    output_json (bool, optional): If True, output the results in JSON format. Default is False.
    output_csv (bool, optional): If True, output the results in CSV format. Default is False.
    return_list (bool, optional): If True, return the results as a list. Default is False.

    Returns:
    list of tuples: If return_list is True, returns a list of tuples where each tuple contains a URL and its fetched content or an error message.
                    Example: [("http://example.com", "<html>...</html>"), ("http://example.org", "Error: ...")]

    Example Usage:
    1. Fetch URLs with default settings:
       main(["http://example.com", "http://example.org"])

    2. Fetch URLs with custom number of workers and save results to JSON file:
       main(["http://example.com", "http://example.org"], max_workers=10, output_file="results.json", output_json=True)

    3. Fetch URLs and save results to CSV file:
       main(["http://example.com", "http://example.org"], output_file="results.csv", output_csv=True)

    4. Fetch URLs and return results as a list:
       results = main(["http://example.com", "http://example.org"], return_list=True)
       print(results)
    '''
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(fetch_url, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                results.append((url, data))
            except Exception as exc:
                results.append((url, f"Generated an exception: {exc}"))

    if output_json:
        output = json.dumps({url: result for url, result in results}, indent=2)
        if output_file:
            with open(output_file, 'w') as f:
                f.write(output)
        else:
            print(output)

    if output_csv:
        if output_file:
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['URL', 'Result'])
                csv_writer.writerows(results)
        else:
            print("Cannot output CSV to stdout. Please specify an output file.")

    if return_list:
        return results
    else:
        return None


if __name__ == "__main__":
    banner = f"""
███████╗███████╗████████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
█████╗  █████╗     ██║   ██║     ███████║█████╗  ██████╔╝
██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
██║     ███████╗   ██║   ╚██████╗██║  ██║███████╗██║  ██║
╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                   
Fetch URLs Concurrently
Version: {__version__}
Author: {__author__}
Description: {__description__}
    """

    print(banner)

    parser = argparse.ArgumentParser(
        description=__description__,
        epilog=f"Author: {__author__} | Version: {__version__}",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input", help="Path to the file containing URLs")
    parser.add_argument("-o", "--output", help="Path to the output file")
    parser.add_argument("-j", "--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("-c", "--csv", action="store_true", help="Output results in CSV format")
    parser.add_argument("-w", "--workers", type=int, default=5, help="Maximum number of workers (threads)")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    main(urls, max_workers=args.max_workers, output_file=args.output_file, output_json=args.json, output_csv=args.csv)
