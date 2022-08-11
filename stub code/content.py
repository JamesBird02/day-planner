import csv
import random


def get_quote(quotes_file = 'quotes.csv'):
    try:
        with open(quotes_file) as csvfile:
            quotes = [{'author': line[0],
                       'quote': line[1]} for line in csv.reader(csvfile, delimiter='|')]

    except Exception as e:
        quotes = [{'author': 'Eric Idle',
                   'quote': 'Always Look on the Bright Side of Life.'}]

    return random.choice(quotes)



def get_weather():
    pass


def get_article():
    pass


if __name__ == '__main__':
    pass

