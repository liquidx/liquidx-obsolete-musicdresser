#!/usr/bin/python
# -*- coding: utf-8 -*-

ya_url_en = "http://global.yesasia.com/en/Search/SearchResult.aspx"
ya_url_b5 = "http://global.yesasia.com/b5/Search/SearchResult.aspx"
ya_url_gb = "http://global.yesasia.com/gb/Search/SearchResult.aspx"

ya_encodings = ['en', 'b5', 'gb']

ya_form_id = 'formAdvancedSearch'
ya_params = {
    'asSectionId': None, # ['music', 'videos', 'mv', 'anime', 'games', 'books', 'comics', 'photos', 'toys', 'electronics']
    'asLanguage': '', # '', ch, cn, md, ml, hk, tw, jp, ws
    'asFormat': 0, #Any
    'asSubtitles': 0, # 1 = tchin, 2 = schin, 3 = eng, 4 = ja, 5 = ko
    'asGenre': 0, # Any
    'asPictureFormat': 0, # 1 = ntsc, 2 = pal
    'asDubbedIn': 0, # 1 = canto, 2 = mand, 3 = eng, 4 = jp, 5 = ko
    'asOrigin': 0, # 1 = hk, 2 = tw, 3 = cn, 4 = !cn, 5 = jp, 6 = ko, 7 = us, 8 = others
    'asRegionCode': 0, # dvd region: 1-7
    'asKeyword':'',
    'asMatchType': 0, # 0 = All, 1 = Any, 2 = Exact
    'asTitle':'',
    'asArtist': '',
    'asDescription':'',
    'asManufacturer': '',
    'asCode':'',
    'asIncludeOutOfStock': 1,
    'asShowAdult': 0,
    'mode': 'adsearch',
    'JavaScriptEnabled':'true'}
    
ya_simple_params = {
    'asSectionID':None,
    'mode':'simplesearch',
    'JavascriptEnabled':'true',
    'asKeyword':''}
    
    
# some logic rules
# if sectionId = music || mv: language = '', ch, cn, md
# if sectionId = videos: language = '', ch ml
# if sectionId = books: language = '', ch, hk, tw, jp, ws
# if sectionId = comics: language = '', hk, jp
# if sectionId = magazines: language = '', ch, jp
# if sectionId != toys, gifts, electronics, games = '', ch
# if sectionId != comics, toys, gifts, electronics, games, magazines, books: language += kr, jp, ws
# if sectionId = all: language = ''

# if sectionId != videos, anime, mv: format = 1=dvd, 2=vcd
# if sectionId != mv: format = (1=dvd, 2=vcd, 3=vhs)
# if sectionId = books: format = (4=hard, 5=paperback, 6=audio, 7=withcd)
# if sectionId = allproducts: format = all above

# if sectionId == videos: genre = (1=tv, 2=movie, 3=special)
# if sectionId == anime: genre = (1=tv, 4=ova)
# if sectionId == mv: genre = (5=karaoke, 6=mv)
# if sectionId == games: genre = (7=ps2, 8=pc, 9=online, 10=gc, 11=gba, 12=xbox, 13=dvd)
# if sectionId == allproducts: genre = all above


from urllib import urlencode, urlopen
import urllib2
import copy
import re
from urlparse import urlparse

imgtag = re.compile('(<IMG.*?>)', re.I|re.M)
srcparam = re.compile('src=[\'\"](.*?)[\'\"]', re.I)
prodimgserver = re.compile('http://i3\.yesasia\.com/assets/imgs/')

params = copy.copy(ya_params)
params['asSectionId'] = 'music'
params['asArtist'] = '陶吉吉 Tao, David'.decode('utf8').encode('big5')
params['asTitle'] = '太平盛世'.decode('utf8').encode('big5')

reqdata = urlencode(params)
resp = urlopen(ya_url_b5, reqdata)

page = resp.read().decode('big5')
allimages = imgtag.findall(page)

#print page.encode('utf-8')

for img in allimages:
    hassrc = srcparam.search(img)
    if hassrc and prodimgserver.search(hassrc.group(1)):
        print hassrc.group(1)
        



