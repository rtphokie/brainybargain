#!/usr/bin/env python3

from latest_user_agents import get_latest_user_agents, get_random_user_agent
from tqdm import tqdm
import argparse
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Referer": "https://brainybargain.com",
    "User-Agent": get_random_user_agent(),
    "X-Requested-With": "XMLHttpRequest"}
s = requests.Session()


def brainybargain(url='https://www.brainybargain.com', minpercentage=50, daysago=0, skipchecks=False):
    """
    A function that analyzes the deals from a given URL based on certain criteria.

    Args:
        url (str): The URL to fetch the deals from. Defaults to 'https://www.brainybargain.com'.
        minpercentage (int): The minimum percentage discount to consider a deal. Defaults to 50.
        daysago (int): The number of days in the past to begin looking for deals. Defaults to 0, i.e. today. 1 is yesterday, etc.
        supressunavailable (bool): A flag to suppress unavailable deals in the output. Defaults to True.
        summary (bool): A flag to print a summary of the results. Defaults to False.

    Returns:
        nothing
    """
    dealdatestoanalyze = []
    for x in range(0, daysago + 1):
        datetoonsider = (datetime.now() - timedelta(days=x)).date()
        dealdatestoanalyze.append(datetoonsider.strftime('%B %-d Deals'))

    s.headers.update(headers)
    r = s.get(url)
    outputlines = []

    if r.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        for js in soup.find_all('script'):
            if 'pageData' in js.text:
                lines = js.text.split('\n')
                str = lines[2].replace('       window.__doppe_viewer_app_data__.pageData = ', '')
                str = str.strip(';')
                data = json.loads(str)
                actions = data['bymoLinkViewerData']['pageData']['bymoPageProps']['actions']
                for action in actions:
                    if action['name'] in dealdatestoanalyze:
                        # daylines = process_day(action, minpercentage, skipchecks)
                        outputlines += process_day(action, minpercentage, skipchecks)

    if len(outputlines) > 1:
        print(f"{'date':12} disc {'link':32} {'code':12} price description")
        print("\n".join(outputlines), "\n")
    else:
        print('No deals found')


def process_day(action, minpercentage, skipchecks):
    outputlines = []

    if 'tag' in action and action['tag'] == 'CustomCoupons':
        coupons = action['settings']['coupons']
        couponstocheck = []
        for coupon in coupons:
            if type(coupon['ribbon']) is not dict and coupon['ribbon'] != 'Price Drop' and 'click' not in coupon[
                'ribbon'].lower():
                coupon['coupon'] = coupon['coupon'].replace('applied automatically', '').replace('no code needed', '')
                couponstocheck.append(coupon)
        for coupon in tqdm(couponstocheck, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}', desc=action['name']):
            if type(coupon['ribbon']) is not dict and coupon['ribbon'] != 'Price Drop' and 'click' not in coupon[
                'ribbon'].lower():
                coupon['coupon'] = coupon['coupon'].replace('applied automatically', '').replace('no code needed', '')
                if 'FREE' in coupon['ribbon']:
                    perc = 100
                elif 'OFF' in coupon['ribbon']:
                    perc = int(coupon['ribbon'].lower().replace(' 0ff', '').replace(' off', '').replace('%', ''))
                if perc >= minpercentage:
                    price = None
                    if not skipchecks:
                        producturl = coupon['couponPageLink']
                        available, price, already_discounted = check_product(producturl)
                        coupon['already_discounted'] = already_discounted
                        coupon['price'] = price
                        coupon['available'] = available
                        if not already_discounted:
                            coupon['price_discounted'] = round(price * (100 - perc) / 100)
                        else:
                            coupon['price_discounted'] = round(price)
                    if price is None:  # skipping checks or error when checking
                        coupon['price'] = coupon['price_discounted'] = "?"
                        coupon['available'] = None
                    if coupon['price_discounted'] == 0:
                        coupon['price_discounted'] = "?"
                    if perc >= minpercentage:
                        outputline = f"{action['name'].replace(' Deals', ''):12} {coupon['ribbon'].replace(' OFF', ''):4} {coupon['couponPageLink']:32} {coupon['coupon']:11}  ${coupon['price_discounted']:4} "
                        if not coupon['available'] and not skipchecks:
                            struckouttitle = ''.join([u'\u0336{}'.format(c) for c in coupon['title']])
                            outputline += f"{struckouttitle} (unavailable)"
                        else:
                            outputline += f"{coupon['title']}"
                        outputlines.append(outputline)
    return outputlines


def check_product(producturl):
    """
    Given a product URL, this function checks if the product is available and retrieves its price.

    Parameters:
        producturl (str): The URL of the product to be checked.

    Returns:
        tuple: A tuple containing two values:
            - available (bool): True if the product is available, False otherwise. None on error
            - price (float): The price of the product. 0 on error
    """
    rproduct = s.get(producturl, allow_redirects=True)
    already_discounted = None
    if rproduct.ok:
        # class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"
        soup = BeautifulSoup(rproduct.content, 'html.parser')
        pricediv = soup.find('span',
                             class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')
        if pricediv is None:
            price = 0
            available = None
        else:
            already_discounted = ' with ' in pricediv.parent.text
            price = float(pricediv.text.replace('$', '').replace(',', ''))
            available = "we couldn't find that page" not in soup.get_text().lower() and 'currently unavailable' not in soup.get_text().lower()
    else:
        available = None
        price = 0
    return available, price, already_discounted


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--daysago", default=0, type=int, help="days back to look (default: 0, today only)")
    parser.add_argument('-s', '--skipchecks', action='store_true', help="don't check price or availability")
    parser.add_argument('-p', '--percent', default=1, type=int,
                        help='minimum percentage off (default: 1)')  # option that takes a value

    # Read arguments from command line
    args = parser.parse_args()

    brainybargain(minpercentage=args.percent, daysago=args.daysago, skipchecks=args.skipchecks)
