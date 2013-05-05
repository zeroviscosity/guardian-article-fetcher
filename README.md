guardian-article-fetcher
========================

A fetcher for The Guardian newspaper's Open Platform API

Arguments with their defaults (all are optional):

*format='json'
*page_size=10 
*page=1
*api_key=None
*from_date=None
*to_date=None
*tag=None
*show_fields=None
*show_tags=None
*show_refinements=None
*section=None
*max=0 

    from guardiannewspaper import ArticleFetcher
    
    fetcher = ArticleFetcher()
    for articles in fetcher.fetch():
        # Do something with the list of articles
        
Calling `fetch()` returns a generator that yields a list of articles on each
iteration. 
