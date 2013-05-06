# guardian-article-fetcher

#### A fetcher for The Guardian newspaper's Open Platform API

### Usage

    from guardianapi import ArticleFetcher
    
    fetcher = ArticleFetcher()
    for article in fetcher.fetch():
        print article # Or do something more interesting
        
Calling `fetch()` returns a generator of articles in JSON format. Articles are 
retrieved one page at a time, with `page_size` articles being retrieved with 
each page. To get the total number of pages available, use `get_total_pages()`.

### Parameters

All parameters are optional. With the exception of `max_pages`, they all map to
API parameters. For more information, visit:
http://www.guardian.co.uk/open-platform/getting-started

* `max_pages`
  * Default: 0
  * This the only paramenter that is not passed along to The Guardian API. If 
  `max_pages` is left at 0, then it will retrieve as many pages as possible. 
  Otherwise it will retrieve the minimum of the total number of pages avaible 
  and `max_pages`.
* `page_size`
  Default: 10
  * `page_size` can be set as high as 50, but The Guardian recommends keeping it 
  * at 10 to optimize performance.
* `page`
  * Default: 1
  * This parameter can be used to skip ahead if need be.
* `api_key`
  * Default: None
  * While an API key is not required, some fields, such as body fields, are only 
  available if you have one.
* `from_date`
  * Default: None
  * Format: YYYY-MM-DD
* `to_date`
  * Default: None
  * Format: YYYY-MM-DD
* `section`
  * Default: None
  * See http://explorer.content.guardianapis.com/#/sections?format=json for the
  available options.
* `tag`
  * Default: None
  * Allows search refinement via tags. Comma separate multiple tags.
* `show_fields`
  * Default: None
  * Specifies the information wanted from the articles. Fields can be specified 
  as comma-separated strings (eg: 'headline,standfirst,thumbnail' or use 'all' 
  to get all avaiable data.
* `show_tags`
  * Default: None
  * Tags are not returned unless requested. `show_tags` can be set to 'all' or to
  specific tag types.
* `show_refinements`
  * Default: None
  * See http://www.guardian.co.uk/open-platform/getting-started for more info.

### To Do

Add XML support

### Origin

This project is an offshoot of the fetcher used by my team (@Kevinyuen and @echau) 
in the Big Data Week 13 Hackathon in Toronto: https://github.com/Kevinyuen/bdw13-hackathon 
