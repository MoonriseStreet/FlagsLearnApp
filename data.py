import sqlite3 as sql
import urllib.error
from urllib.request import urlopen, Request
import re

con = sql.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `test` (id INTEGER)")
    con.commit()

data = []

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    list_of_countries = urllib.request.urlopen(
        'https://en.wikipedia.org/wiki/List_of_sovereign_states').read()
    req = Request(
        url='https://www.countries-ofthe-world.com/capitals-of-the-world.html',
        headers=headers)
    list_of_capitals = urllib.request.urlopen(req).read()
    countries_list = re.findall(r'<span id="\w+">', str(list_of_countries))
    capitals_list = re.findall(
        r'<td>[a-zA-Z,.\'()\-\s]+</td><td>[a-zA-Zó\',.()\-\s]+</td>',
        str(list_of_capitals))
    f = open('data.txt', 'w')
    if countries_list:
        counter = -1
        flags_counter = 0
        for country in countries_list:
            counter += 1
            country = re.search('\"\w+\"', country)
            country = country.group()[1:-1:]
            try:
                country_page = urllib.request.urlopen(
                    'https://en.wikipedia.org/wiki/' + country)
            except urllib.error.HTTPError:
                print(country + " not found")
                continue
            try:
                flag_url = re.search(
                    r'//upload.wikimedia.org/wikipedia(/commons)??(/en)??/thumb/[a-z0-9]/[a-z0-9][a-z0-9]/Flag_of_(the_)??(The_)??' + country + '[.]*.svg',
                    str(list_of_countries))
                flag = 'None'
                if flag_url:
                    flags_counter += 1
                    flag = 'https:' + flag_url.group()
                    flag = flag.replace('thumb', '')
                    flag_of_country = urllib.request.urlopen(flag)
            except urllib.error.HTTPError:
                flags_counter -= 1
                flag = 'None'
            country = country.replace("_", " ")
            capital = 'None'
            for pair in capitals_list:
                a = pair.find(country + '<')
                if not a == -1:
                    capital = pair[a + len(country) + 9:-5:]
            country_data = [str(counter), country, flag, capital]
            print(country_data)
            f.write('\t'.join(country_data) + '\n')
        print(str(flags_counter) + ' flags was found')
        f.close()
    else:
        print('did not find')
