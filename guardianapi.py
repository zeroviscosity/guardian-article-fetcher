#!/usr/bin/env python

import sys
import requests
import json
from argparse import ArgumentParser
from dateutil import parser


class ArticleFetcher():
    def __init__(self, max_pages=0, page_size=10, page=1, api_key=None, 
            from_date=None, to_date=None, section=None, tag=None,
            show_fields=None, show_tags=None, show_refinements=None):
        """Defines the fetcher url"""
        self.page = page
        self.max_pages = max_pages
        
        params = []
        params.append('page-size=%d' % page_size)
        
        if api_key:
            params.append('api-key=%s' % api_key)
        if from_date:
            params.append('from-date=%s' % from_date)
        if to_date:
            params.append('to-date=%s' % to_date)
        if section:
            params.append('section=%s' % section)
        if tag:
            params.append('tag=%s' % tag)
        if show_fields:
            params.append('show-fields=%s' % show_fields)
        if show_tags:
            params.append('show-tags=%s' % show_tags)
        if show_refinements:
            params.append('show-refinements=%s' % show_refinements)
        
        self.url = 'http://content.guardianapis.com/search?format=json&%s' % \
                '&'.join(params)
        self.url += '&page=%d'
    
    def get_total_pages(self):
        """Retrieves the total number of pages for the current operation"""
        r = requests.get(self.url % 1)
        resp = (json.loads(r.text))['response']
        return min(self.max_pages, resp['pages'])
        
    def get_data(self, page_number):
        """Fetches a page of articles from the API"""
        percent = 100.0 * page_number / self.total_pages
        print 'Fetching page %i of %i ... %f%%' % (page_number, 
                self.total_pages, percent)
                
        r = requests.get(self.url % page_number)
        resp = (json.loads(r.text))['response']
        if resp['status'] == 'ok' and len(resp['results']) > 0:
            return resp['results']
        return []
        
    def fetch(self):
        """Starts the fetching process"""
        self.total_pages = self.get_total_pages()
        for i in range(self.page, self.total_pages + 1):
            for article in self.get_data(i):
                yield article


