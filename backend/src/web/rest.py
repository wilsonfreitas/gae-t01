# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch


def index(_json):
	url = 'http://www.cetip.com.br/'
	result = urlfetch.fetch(url)
	if result.status_code == 200:
		soup = BeautifulSoup(result.content)
		# <span id="ctl00_Banner_lblTaxDI">10,80%</span>
		# <span id="ctl00_Banner_lblTaxDateDI">(17/04/2014)</span>
		# soup.find_all(id='ctl00_Banner_lblTaxDI')
		rate = soup.find_all(id='ctl00_Banner_lblTaxDI')[0].string
		rate = float(rate.replace('%', '').replace(',', '.'))
		_json({'CDI': rate})
	else:
		_json({})





