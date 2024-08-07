import pyshorteners

import pyshorteners

link = 'https://www.google.com'

s = pyshorteners.Shortener()
link_domain_list = ['clckru','dagd','isgd','osdb','tinyurl']

short_link = s.clckru.short(link)
print(short_link)

expand_link = s.clckru.expand(short_link)
print(expand_link)