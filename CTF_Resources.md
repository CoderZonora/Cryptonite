# Useful Tools and Resources

1. **Lots of tools in one place for various domains:** [CyberChef](https://gchq.github.io/CyberChef/)

2. **OCR for math equations:** [LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR)

3. **Image forensics online:** [Aperi Solve](https://www.aperisolve.com/)

4. **Tool for codes and ciphers:** [Multi Decoder](https://www.cachesleuth.com/multidecoder/)

5. **Zip cracking:** `zip2john` - A component of johntheripper for zip files. [More Info](https://superuser.com/a/1737639)

6. **OSINT search:** 
   - [Whatsmyname](https://whatsmyname.app/)
   - [GeoMasstr](https://geomastr.com/)
   - [GeoSpy](https://geospy.ai/)
   - [Overpass Turbo](https://overpass-turbo.eu/)

7. **Web scraping:** [Scrapy](https://scrapy.org/)

8. **Volatility cheatsheet 2 vs 3:** [Volatility Cheatsheet](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet)

9. **Unsalted hash lookup table online:**
   - [Crackstation](https://crackstation.net/)
   - [MD5 Lookup](https://md5.gromweb.com/?md5=8d763385e0476ae208f21bc63956f748)

10. **CSP bypass callback APIs:** [JSONBee](https://github.com/zigoo0/JSONBee)

11. **Payloads for different things:** [Payloads All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings)

12. **Unicode Lookup:** [Unicode Lookup](https://unicodelookup.com/)

13. **Web challenges basic steps:**

   **If blind (No src given):**
   - `ctrl + U` -> scripts.js (Go through source)
   - Crack JWT token
   - SQLi: if internal 500 error => yes. Try `'`, `"`, or `1=1-- -`
   - Look into Devtools, Headers, Cookies, LocalStorage -> copy requests -> [Curlconverter](https://curlconverter.com/) -> python script to fuzz common endpoints like `robots.txt`, `sitemap.xml`.
   - Gobuster: Basically a directory brute-forcer. Change user-agent to prevent detection by CTF organisers.
   - If `{{ 7 * 7 }}` => `49` then try SSTI jinja2 or `#{5*5}` in some software.
   - `; ls` => lists file or bash error => RCE possible
   - XSS: `<h1>hi</h1>`
   - DOM clobber

   **If source given:**
   - Go through source.
   - If you see some special code which might be copied from somewhere, try to paste the code in the browser and check. Don't just GPT it! - Ref: Downunderctf prototype pollution.
   - Find type of database. Search for strings like `sqlite` etc. Search for `?` to check which SQL queries are vulnerable.
   - Search for `innerHTML`
   - `render()` OR `views` folder => SSTI (Server-side template injection)
   - If `subprocess` imported => RCE
