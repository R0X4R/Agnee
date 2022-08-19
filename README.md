<h1 align="center">
  <br>
  <a href="https://github.com/R0X4R/Agnee"><img src=".github/static/logo.png" width="60%" alt="Agnee logo"></a>
</h1>

<h4 align="center"><b>Find sensitive information using dorks from different search-engines.</b></h4><br>

<p align="center">
  <a href="https://github.com/R0X4R/Agnee/releases">
    <img src="https://img.shields.io/github/release/R0X4R/Agnee.svg?label=version">
  </a>
  <a href="#"><img src="https://madewithlove.org.in/badge.svg"></a>
<a href="https://twitter.com/R0X4R/"><img src="https://img.shields.io/badge/twitter-%40R0X4R-blue.svg"></a>
<a href="https://github.com/R0X4R/Agnee/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/R0X4R/Agnee/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="https://github.com/R0X4R?tab=followers"><img src="https://img.shields.io/badge/github-%40R0X4R-orange"></a>
  <a href="https://github.com/R0X4R/Agnee/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/R0X4R/Agnee?color=dark-green&label=issues%20fixed">
  </a>
  <a href="https://travis-ci.com/R0X4R/Agnee">
      <img src="https://img.shields.io/travis/com/R0X4R/Agnee.svg?color=dark-green&label=tests">
  </a>
</p>

<p align="center"><img src=".github/static/usage.png" alt="Agnee usage"></p>

---

Agnee uses [`search_engines`](https://github.com/tasos-py/Search-Engines-Scraper) to find sensitive information about given domain using multiple dorks through mutltiple search-engines. I have modified some code of `search_engines` and used it in this script to get the custom results and currently it only find results from bing, google and yahoo (will implement more in future for sure).

### Installation

```bash
sudo pip3 install git+https://github.com/R0X4R/Search-Engines-Scraper.git && sudo pip3 install agnee
```

> **Note**: Before installing agnee you must need git and python3 installed on your system.

### Usage

+ **Simple usage arguments**
    
    ```css
    $ agnee -d testphp.vulnweb.com

    https://www.exploit-db.com/ghdb/6630
    https://www.exploit-db.com/ghdb/5665
    http://testphp.vulnweb.com/secured/phpinfo.php
    ```

+ **To use a specific engine**

    ```css
    $ agnee -d testphp.vulnweb.com -e yahoo

    Yahoo Dork: inurl:"/.git" testphp.vulnweb.com -github

    https://www.exploit-db.com/ghdb/6630
    https://www.exploit-db.com/ghdb/5665
    http://testphp.vulnweb.com/secured/phpinfo.php
    ```

+ **To search specific number of pages**
    ```css
    $ agnee -d testphp.vulnweb.com -p 1
    ```
	
+ **Use all the search-engines**

    ```css
    $ agnee -d testphp.vulnweb.com -all
    ```
    > **Note**: Sometimes google may block your requests so you need to wait for few hours.
---

### Donate
If this tool helped you or you like my work

|[`buymeacoffee.com/R0X4R`](https://www.buymeacoffee.com/R0X4R)|[`pmny.in/bIKNZngt4ys1`](https://pmny.in/bIKNZngt4ys1)|[`ko-fi.com/R0X4R`](https://ko-fi.com/i/IK3K34SJSA)|
|--------|--------|------|

**Warning:** This code was originally created for personal use, do not abuse the traffic, please use with caution.
