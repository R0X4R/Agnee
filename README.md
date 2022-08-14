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

```console
$ agnee -h

Find sensitive information using Dorks.

USAGE:
    agnee -d domain.tld

OPTIONS:
    -d DOMAIN, --domain DOMAIN  Define the domain to scan
    -a, --all                   Use all search-engines (default "Bing")
    -e ENGINE, --engine ENGINE  List of search-engines to use [-e "bing, google"] (comma separated)
    -o OUTPUT, --output OUTPUT  Save the results in the output file
    -p PAGE, --page PAGE        Number of pages to scrape
    -q, --quite                 Suppress all the output
```

---

Agnee uses [`search_engines`](https://github.com/tasos-py/Search-Engines-Scraper) to find sensitive information about given domain using multiple dorks through mutltiple search-engines. I have modified some code of `search_engines` and used it in this script to get the custom results and currently it only find results from bing, google and yahoo (will implement more in future for sure).

### Installation

```css
sudo pip3 install git+https://github.com/R0X4R/Search-Engines-Scraper.git && pip3 install agnee
```

> **Note**: Before installing agnee you must need git and python3 installed on your system.

### Usage

+ **Simple usage arguments**
    
    ```console
    agnee -d testphp.vulnweb.com

    https://www.exploit-db.com/ghdb/6630
    https://www.exploit-db.com/ghdb/5665
    http://testphp.vulnweb.com/secured/phpinfo.php
    ```

+ **To use a specific engine**

    ```console
    agnee -d testphp.vulnweb.com -e yahoo

    Yahoo Dork: inurl:"/.git" testphp.vulnweb.com -github

    https://www.exploit-db.com/ghdb/6630
    https://www.exploit-db.com/ghdb/5665
    http://testphp.vulnweb.com/secured/phpinfo.php
    ```

+ **To search specific number of pages**
    ```console
    agnee -d testphp.vulnweb.com -p 1
	```
	
+ **Use all the search-engines**

    ```console
    agnee -d testphp.vulnweb.com -all
    ```
    > **Note**: Sometimes google may block your requests so you need to wait for few hours.
<br>

### Donate
If this tool helped you or you like my work

</br><a href="https://www.buymeacoffee.com/R0X4R"><img src="https://img.buymeacoffee.com/button-api/?text=Help me to buy oscp&emoji=😇&slug=R0X4R&button_colour=5F7FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00"/></a> <a style=" width: 135px; background-color: #1065b7; text-align: center; font-weight: 800; padding: 11px 0px; color: white; font-size: 12px; display: inline-block; text-decoration: none; " href='https://pmny.in/bIKNZngt4ys1'> Donate Now </a>   <a href="https://ko-fi.com/i/IK3K34SJSA"><img src="https://ko-fi.com/img/githubbutton_sm.svg"></a><br/><br/>
