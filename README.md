# web-scraper
website scraper (i.e. - extractor of info) using python. Note - I contributed to the code, but whoever created most of this wants to be anonymous. Another scraper in another repository provided help to me by Prad Basu (connected with me through Beyond Animal) - https://github.com/BrittanyBunk/Beyond-Animal - using clojure. Unfortunately they never provided instructions on performing this, but I feel python's better (see reasons why below).

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

**Subpar IDE's for python:**
- spyder
  * reason - >>clunky
    - reason - >100mb download file
- Wing - https://wingware.com/
  * issue - $
- [online-python.com](https://www.online-python.com/)
  * issue - lacks connectivity - -> call programs, libraries, etc.
    - that would normally be on the comp
      * ex - BeautifulSoup4
 
**supplement - -> IDE:**
- jupyter
  * is a notebook
- colab - https://colab.research.google.com/
  * updater - public
