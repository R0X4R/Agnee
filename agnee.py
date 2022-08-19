#!/usr/bin/env python3
"""
AGNEE v1.1
AUTHOR: ESHAN SINGH (R0X4R)

CREDITS https://github.com/tasos-py FOR THE SEARCH_ENGINES LIBRARY
"""

#@> IMPORTING ALL DEPENDENCIES
from search_engines import Google, Bing, Yahoo, Startpage, config
from tldextract import extract
from sys import stdout, exit
from random import choice
from time import sleep
import argparse

def parse_args():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description="Find sensitive information using Dorks.", usage="agnee -d domain.tld", add_help=False)
    parser._optionals.title = "OPTIONS"

    parser.add_argument("-d", "--domain", dest="domain", help="Define the domain to scan")
    parser.add_argument("-a", "--all", dest="all", help="Use all search-engines (default \"Bing\")", action='store_true')
    parser.add_argument("-h", "--help", dest="help", action='store_true')
    parser.add_argument("-e", "--engine", dest="engine", help="List of search-engines to use [-e \"bing, google\"] (comma separated)", default="bing")
    parser.add_argument("-o", "--output", dest="output", help="Save the results in the output file")
    parser.add_argument("-p", "--page", dest="page", help="Number of pages to scrape", default=config.SEARCH_ENGINE_RESULTS_PAGES, type=int)
    parser.add_argument("-q", "--quite", dest="quite", help="Suppress all the output", action='store_true')   
    
    return parser.parse_args()

cmd = parse_args()

#@> DEFINING COLOR VARIABLES
R = '\033[91m'
W = '\033[0m'
Y = '\033[93m'

def usage():
    print("""
Find sensitive information using dorks from different search-engines.

USAGE:
    %sagnee -d domain.tld%s

OPTIONS:
    -d, --domain    string    Define the domain to scan
    -e, --engine    string    List of search-engines to use [-e "bing, google"] (comma separated)
    -a, --all                 Use all search-engines (default "Bing")
    -h, --help                Show this help message and exit
    -o, --output    string    Save the results in the output file
    -p, --page      int       Number of pages to scrape results.
    -q, --quite               Suppress all the output and store in the file.
    """ % (Y, W))

if cmd.help:
    usage()
    exit()

if cmd.domain is None:
    usage()
    print("[%sERROR%s] %sPlease add domain to scan using -d/--domain.%s" % (R, W, Y, W))
    exit()

if not cmd.engine is None or not cmd.all:
    engines = [
            e.strip() for e in cmd.engine.lower().split(',')
        ]
else:
    usage()
    print("[%sERROR%s] %sPlease choose an engine or use --all%s" % (R, W, Y, W))
    exit()

if cmd.quite:
    if cmd.output is None:
        usage()
        print("[%sERROR%s] %sPlease specify the output file using -o/--output%s" % (R, W, Y, W))
        exit()

#@> DECLARING SEARCH VARIABLES
odomain = extract(str(cmd.domain)).domain
bsearch = Bing()
gsearch = Google()
ysearch = Yahoo()
ssearch = Startpage()
# dsearch = Duckduckgo()

"""User-agent list (random library will choose it randomly)"""
agntList = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2820.59 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/75.0",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2",
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.14.1) Presto/2.12.388 Version/12.16",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
]
uagents = choice(agntList)

"""List of all dorks"""
dorks = [
    "inurl:\"/.git\" "+cmd.domain+" -github",
    "site:"+cmd.domain+" ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
    "site:"+cmd.domain+" ext:sql | ext:dbf | ext:mdb",
    "site:"+cmd.domain+" intitle:index.of | ext:log | ext:php intitle:phpinfo \"published by the PHP Group\" | inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor | inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config | inurl:\"/phpinfo.php\" | inurl:\".htaccess\" | ext:swf",
    "site:"+cmd.domain+" intext:\"sql syntax near\" | intext:\"syntax error has occurred\" | intext:\"incorrect syntax near\" | intext:\"unexpected end of SQL command\" | intext:\"Warning: mysql_connect()\" | intext:\"Warning: mysql_query()\" | intext:\"Warning: pg_connect()\"",
    "site:"+cmd.domain+" ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv",
    "site:"+cmd.domain+" ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:env | ext:ini",
    "site:"+cmd.domain+" \"PHP Parse error\" | \"PHP Warning\" | \"PHP Error\"",
    "site:"+cmd.domain+" inurl:wp-content | inurl:wp-includes",
    "inurl:\"/sym404/root/\" \""+cmd.domain+"\"",
    "site:"+cmd.domain+" not for distribution | confidential | “employee only” | proprietary | top secret | classified | trade secret | internal | private | WS_FTP | ws_ftp | log | LOG",
    "site:.s3.amazonaws.com | site:storage.googleapis.com | site:amazonaws.com \""+odomain+"\"",
    "intitle:traefik inurl:8080/dashboard \""+odomain+"\"",
    "intitle:\"Dashboard [Jenkins]\" \""+odomain+"\"",
    "site:sharecode.io | site:controlc.com | site:codepad.co |site:ideone.com | site:codebeautify.org | site:jsdelivr.com | site:codeshare.io | site:codepen.io | site:repl.it | site:jsfiddle.net \""+odomain+"\"",
    "site:gitter.im | site:papaly.com | site:productforums.google.com | site:coggle.it | site:replt.it | site:ycombinator.com | site:libraries.io | site:npm.runkit.com | site:npmjs.com | site:scribd.com \""+odomain+"\"",
    "site:stackoverflow.com \""+cmd.domain+"\"",
    "site:justpaste.it | site:heypasteit.com | site:pastebin.com \""+odomain+"\"",
    "site:"+cmd.domain+" ext:action | ext:struts | ext:do",
]

def saveFile(file, result):
    """
    Save the output in a file
    """
    file = open((file), "a")
    file.write(str(result))
    file.write('\n')
    file.close()

def googSearch():
    """
    Google search function
    """
    for dork in dorks:
        gdork = '\n' + "Google Dork: %s" % (str(dork)) + '\n'
        if cmd.output is not None:
            saveFile(cmd.output, gdork)
        if not cmd.quite:
            stdout.write(str(gdork) + '\n')
        gsearch.set_headers({'User-Agent': uagents})
        gout = gsearch.search(str(dork), cmd.page)
        for links in gout.links():
            if cmd.output is not None:
                stdout.write(str(links) + '\n')
                saveFile(cmd.output, links)
            elif cmd.quite:
                saveFile(cmd.output, links)
            else:
                stdout.write(str(links) + '\n')
        sleep(2)

def bingSearch():
    """
    Bing search function
    """
    for dork in dorks:
        bdork = '\n' + "Bing Dork: %s" % (str(dork)) + '\n'
        if cmd.output is not None:
            saveFile(cmd.output, bdork)
        if not cmd.quite:
            stdout.write(str(bdork) + '\n')
        bsearch.set_headers({'User-Agent': uagents})
        bout = bsearch.search(str(dork), cmd.page)
        for links in bout.links():
            if cmd.output is not None:
                stdout.write(str(links) + '\n')
                saveFile(cmd.output, links)
            elif cmd.quite:
                saveFile(cmd.output, links)
            else:
                stdout.write(str(links) + '\n')
        sleep(2)

# def duckSearch():
#     for dork in dorks:
#         dsearch.set_headers({'User-Agent': uagents})
#         dout = dsearch.search(str(dork), cmd.page)
#         for links in dout.links():
#             stdout.write(str(links) + '\n')
#         sleep(2)

def yahoSearch():
    """
    Yahoo search function
    """
    for dork in dorks:
        ydork = '\n' + "Yahoo Dork: %s" % (str(dork)) + '\n'
        if cmd.output is not None:
            saveFile(cmd.output, ydork)
        if not cmd.quite:
            stdout.write(str(ydork) + '\n')
        ysearch.set_headers({'User-Agent': uagents})
        yout = ysearch.search(str(dork), cmd.page)
        for links in yout.links():
            if cmd.output is not None:
                stdout.write(str(links) + '\n')
                saveFile(cmd.output, links)
            elif cmd.quite:
                saveFile(cmd.output, links)
            else:
                stdout.write(str(links) + '\n')
        sleep(2)

def starSearch():
    """
    Startpage search function
    """
    for dork in dorks:
        sdork = '\n' + "Startpage Dork: %s" % (str(dork)) + '\n'
        if cmd.output is not None:
            saveFile(cmd.output, sdork)
        if not cmd.quite:
            stdout.write(str(sdork) + '\n')
        ssearch.set_headers({'User-Agent': uagents})
        sout = ssearch.search(str(dork), cmd.page)
        for links in sout.links():
            if cmd.output is not None:
                stdout.write(str(links) + '\n')
                saveFile(cmd.output, links)
            elif cmd.quite:
                saveFile(cmd.output, links)
            else:
                stdout.write(str(links) + '\n')
        sleep(2)

def main():
    try:
        if cmd.all:
            bingSearch()
            starSearch()
            googSearch()
            yahoSearch()
        else:
            for s in engines:
                if s == "bing":
                    bingSearch()
                elif s == "google":
                    googSearch()
                elif s == "yahoo":
                    yahoSearch()
                elif s == "startpage":
                    starSearch()
    except KeyboardInterrupt:
        """
        If ctrl+c is pressed
        """
        print('\n'+"CTRL+C, pressed stoping the engine")
        exit(0)

if __name__ == '__main__':
    main()