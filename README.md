# web-scraper
website scraper (i.e. - extractor of info) using python. Note - I didn't create this, but whoever did wants to be anonymous.

The process involves parsing a website before scraping to concentrate the data.

The example website used is the greenlight bookstore's website - https://www.greenlightbookstore.com .

**There's other ways to scrape sites, but they're potentially subpar:**
- clojure - https://clojure.org/
  * issue - slows down websites
    - python - doesn't do this
      * (?) reason - reads data and moves it elsewhere
        - closure will work with the databases of the website's server itself
- tampermonkey
  * has same issue - as clojure
- url extractor - https://www.prepostseo.com/link-extractor
- git bash - https://gitforwindows.org/
