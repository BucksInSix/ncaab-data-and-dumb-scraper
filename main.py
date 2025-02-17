import time
from typing import List

import pandas as pd
import requests
from bs4 import BeautifulSoup


_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
_ROSTER_INDEX = 0
_PER_GAME_INDEX = 5
_TOTALS_INDEX = 7
_PER_40_INDEX = 9
_PER_100_INDEX = 11
_ADVANCED_INDEX = 13


def main():
    all_rosters = pd.DataFrame()
    all_per_game = pd.DataFrame()
    all_total = pd.DataFrame()
    all_per_40 = pd.DataFrame()
    all_per_100 = pd.DataFrame()
    all_advanced = pd.DataFrame()
    school_links = get_school_links()
    year_range = reversed(range(2011, 2023))
    for year in year_range:
        for school in school_links:
            time.sleep(1)
            school_link = school['school_link']
            school_name = school['school_name']
            url = f'https://www.sports-reference.com{school_link}{year}.html'
            response = requests.get(url, headers=_HEADERS)
            if response.status_code == 200:
                print(f'Scraping {year} {school_name}')
                try:
                    soup = BeautifulSoup(response.content, features="lxml")
                    tables = soup.findAll('table')
                    tables = [str(table) for table in tables]
                    roster = pd.read_html(tables[_ROSTER_INDEX])[0]
                    roster = roster.fillna('')
                    roster['Year'] = year
                    roster['School'] = school_name
                    all_rosters = pd.concat([all_rosters, roster], ignore_index=True)
                    per_game = pd.read_html(tables[_PER_GAME_INDEX])[0]
                    per_game = per_game.fillna('')
                    per_game['Year'] = year
                    per_game['School'] = school_name
                    all_per_game = pd.concat([all_per_game, per_game], ignore_index=True)
                    totals = pd.read_html(tables[_TOTALS_INDEX])[0]
                    totals = totals.fillna('')
                    totals['Year'] = year
                    totals['School'] = school_name
                    all_total = pd.concat([all_total, totals], ignore_index=True)
                    per_40 = pd.read_html(tables[_PER_40_INDEX])[0]
                    per_40 = per_40.fillna('')
                    per_40['Year'] = year
                    per_40['School'] = school_name
                    all_per_40 = pd.concat([all_per_40, per_40], ignore_index=True)
                    per_100 = pd.read_html(tables[_PER_100_INDEX])[0]
                    per_100 = per_100.fillna('')
                    per_100['Year'] = year
                    per_100['School'] = school_name
                    all_per_100 = pd.concat([all_per_100, per_100], ignore_index=True)
                    advanced = pd.read_html(tables[_ADVANCED_INDEX])[0]
                    advanced = advanced.fillna('')
                    advanced['Year'] = year
                    advanced['School'] = school_name
                    all_advanced = pd.concat([all_advanced, advanced], ignore_index=True)
                except:
                    print(f'Error scraping {year} {school_name}')
            else:
                print(f'{year} {school_name} cannot be found.')
            all_rosters.to_csv('roster.csv', index=False)
            all_per_game.to_csv('per_game.csv', index=False)
            all_total.to_csv('total.csv', index=False)
            all_per_40.to_csv('per_40_min.csv', index=False)
            all_per_100.to_csv('per_100_poss.csv', index=False)
            all_advanced.to_csv('advanced.csv', index=False)


def get_school_links() -> List[dict]:
    schools_url = 'https://www.sports-reference.com/cbb/schools/'
    response = requests.get(schools_url, headers=_HEADERS)
    soup = BeautifulSoup(response.content, features="lxml")
    links = soup.findAll('a', href=True)
    links = [str(link) for link in links]
    links = [link for link in links if 'cbb/schools/' in link]
    links = sorted(list(set(links)))
    all_links = []
    for link in links:
        all_links.append({
            'school_link': link.split('href="')[1].split('"')[0],
            'school_name': link.split('">')[1].split('</a>')[0],
        })
    return all_links


# Adding new whitespace to test something
if __name__ == '__main__':
    main()
