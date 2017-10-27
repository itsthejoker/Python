# Apple's current CVE list from
# circl.lu
# pull all the CVE's

import datetime
import json
import logging

import pandas as pd
import urllib.request


def get_json():
    """
    Pull JSON of OSX vulnerabilities, parse it, and return.

    :return: Dict; all CVE entries returned from API.
    """
    logging.info('Starting JSON retrieval...')
    start = datetime.datetime.now()
    # getting the url
    f = urllib.request.urlopen('https://cve.circl.lu/api/search/apple/mac_os')

    # decoding the text
    logging.info('Starting JSON decode. This may take a few minutes.')
    json_string = f.read().decode('utf-8')
    f.close()

    # parsing the information
    parsed_json = json.loads(json_string)

    end = datetime.datetime.now()
    logging.info(
        'JSON decode finished. Processing time: {} seconds.'.format((end-start).seconds)
    )

    return parsed_json


def format_for_spreadsheet(api_results):
    logging.info('Parsing records...')

    records = list()

    for record in api_results:
        cve = record.get('id', None)
        cwe = record.get('cwe', 'Unknown')
        summary = record.get('summary', 'Unknown')
        published = record.get('Published', 'Unknown')
        last_modified = record.get('last-modified', 'Unknown')
        records.append((cve, cwe, summary, published, last_modified))

    return records


def create_csv(records):
    logging.info('Starting CSV export...')
    df = pd.DataFrame(records, columns=('cve', 'cwe', 'summary', 'published', 'last_modified'))
    df.to_csv('cve_apple.csv', index=False, encoding='utf-8')
    logging.info('CSV export complete.')


def main():
    cve_data = get_json()
    results = format_for_spreadsheet(cve_data)
    create_csv(results)

if __name__ == '__main__':
    FORMAT = '[%(levelname)s] - [%(funcName)s] - %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)

    main()