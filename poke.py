#!/usr/bin/env python

import mechanize

class FacebookBrowser(object):

	def __init__(self, email, pw):
		self.br = mechanize.Browser()
		self.br.set_handle_robos(False)
		self.br.open("http://www.facebook.com/login.php")
		self.br.select_form(predicate=lambda f: 'id' in f.attrs and f.attrs['id'] == 'login_form')
		br['email'] = email
		br['pass'] = pw
		r = br.submit()

	def poke_all_back(self):
		html = self.br.open('https://www.facebook.com/pokes').get_data()
		split_html = re.split(r'id=(\d*)\W{2}(\w*\s\w*)\<\/a\> has poked', html)
		# group(1) per group of 3 + surrounding before & after is a[2+3i] zero-idx
		names = [x[1] for x in filter(lambda t: (t[0] + 1) % 3 == 0, enumerate(split_html))] 
		# group(2) per group of 3 + surrounding before & after is a[1+3i] zero-idx
		ids = [x[1] for x in filter(lambda t: (t[0] + 2) % 3 == 0, enumerate(split_html))]
		