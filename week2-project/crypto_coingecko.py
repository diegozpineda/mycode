#!/usr/bin/env python3
'''Flask server to pull data from coingecko and display on flask server'''

import requests

def build_url(path: str):
    coingecko = 'https://api.coingecko.com/api/v3/'
    #api_key = 'API KEY GOES HERE' # From testing it looks like API key is not needed for public coingecko api

    #return coingecko + path + '?x_cg_api_key=' +  api_key
    return coingecko + path 

def get_marketchart(coin: str):
    newurl = build_url(f'/coins/{coin}/market_chart?vs_currency=usd&days=7&interval=daily')

    return newurl

def get_marketinfo(price_percentage: str, order: str, per_page: int):
    ''' price_percentage values:
        1h, 24h, 7d, 14d, 30d, 200d, 1y
        order values:
        market_cap_asc, market_cap_desc, volume_asc, volume_desc, id_asc, id_desc
        per_page:
        Any int between 1 and 100 '''
    newurl = build_url(f'/coins/markets?vs_currency=usd&order={order}&per_page={per_page}&page=1&' \
        + f'sparkline=false&price_change_percentage={price_percentage}&local=en')
    
    return newurl

def get_data(url: str):
    api_obj = requests.get(url)
    obj_read = api_obj.json()
    return obj_read

def parse_marketdata(marketdata: list):
    ''' Will return Key stats for top 10 crypto, in the past 7 days,
        by descending market cap'''
    parsed_data = []
    #marketdata = get_data(get_marketinfo('7d', 'market_cap_desc', 10))
    #for i in marketdata:
    #    coin_stats = {}
    #    coin_stats

def get_marketdata():
    ''' Simple function to return market data
        at 7d interval, market_cap_desc, for top 10 coins'''
    
    return get_data(get_marketinfo('7d', 'market_cap_desc', 10))

#def main():
#    bitcoin_chart = get_data(get_marketchart('bitcoin'))    
#    current_market = get_data(get_marketinfo('7d', 'market_cap_desc', 10))
#    print(bitcoin_chart)
#    print(current_market)

#if __name__ == "__main__":
#    main()