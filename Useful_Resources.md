1. Lots of tools in one place for variety of domains : [CyberChef](https://gchq.github.io/CyberChef/)

2. OCR for math equations: https://github.com/lukas-blecher/LaTeX-OCR

3. Image forensics online : [Aperi Solve](https://www.aperisolve.com/)

4. This tool is designed to solve a wide variety of codes and ciphers. [Multi Decoder](https://www.cachesleuth.com/multidecoder/)

5.Zip cracking: zip2john - A component of johntheripper for zip files.   https://superuser.com/a/1737639

6.OSINT search: https://whatsmyname.app/ - Maybe help you find some link others cannot

7.Web scraping: https://scrapy.org/

8.Volatility cheatsheet 2 vs 3: https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet

9: Unsalted hash lookup table online: https://crackstation.net/

10. CSP bypass callback api's: https://github.com/zigoo0/JSONBee

11. Payloads for all kinds of different things:
  https://github.com/swisskyrepo/PayloadsAllTheThings
12.Web challenges basic steps:
  
  If blind (No src given):
  
  ctrl + U -> scripts.js (Go through source)
  
  Crack jwt token

  sqli:if internal 500 error => yes. Try '  " ' or 1=1-- -
  
  Look into Devtools,Headers,Cookies,Localstorage => copy requests => https://curlconverter.com/ => python script fuzz endpoints

  Gobuster : Basically a directory brute-forcer. Change user-agent to prevent detection by CTForganisers
  
  If {{ 7 * 7 }} => 49 then try SSTI jinja2.

  ; ls => lists file or bash error => RCE possible
  
  xss ```<h1>hi</h1>```
  
  dom clobber

If source given:
Go thorugh source.

Find type of database. Search for strings like sqlite etc. Search for ? to check which sql queries are vulnerable.

Search for innerHTML

render() OR views folder => SSTI (Server side template injection)

If subprocess imported =>  RCE
