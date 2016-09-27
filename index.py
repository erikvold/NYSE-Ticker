#     _   ____  _______ ______   _______      __            
#    / | / /\ \/ / ___// ____/  /_  __(_)____/ /_____  _____
#   /  |/ /  \  /\__ \/ __/      / / / / ___/ //_/ _ \/ ___/
#  / /|  /   / /___/ / /___     / / / / /__/ ,< /  __/ /    
# /_/ |_/   /_//____/_____/    /_/ /_/\___/_/|_|\___/_/     

# Author: Will Binns (Threema ID: UFKZ739A | https://threema.ch)
# Description: Look up the latest prices for stocks on the NYSE.
# GitHub Repository: NYSE Ticker (github.com/wbinns/NYSE-Ticker)
# License: Unlicense (unlicense.org)

# Load libraries
import requests
import urllib
import json
import yaml
from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Init Flask, Wallet and Payment
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# Add 402
@app.route('/price')
@payment.required(720)
def lookup_string():
    symbol = request.args.get('symbol')
    link = requests.get('http://www.google.com/finance/info?q=NSE:'+symbol)
    return link.text

# Add Manifest
@app.route('/manifest')
def docs():
    '''
    Serves the app manifest to the 21 crawler.
    '''
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)

# Init Host
if __name__=='__main__':
    app.run(host='::', port='10115')
