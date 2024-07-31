<h3>List of interesting small things I learn here and there which might be used in a CTF</h3>

- CSP can also allow specific inline scripts by their cryptographic hashes.It has a report only mode. Detailed explanation: https://b13.com/blog/introduction-to-content-security-policy-csp

- You can have custom styled messages loaded into the devtools console ,like facebook uses to give warning about self-XSS. 
https://stackoverflow.com/questions/42165204/how-can-i-display-a-warning-to-users-who-open-the-chrome-console-like-facebook

- ftp server thing : https://blog.s1r1us.ninja/CTF/tangled_browsers

- redos attack: https://blog.huli.tw/2023/06/12/en/redos-regular-expression-denial-of-service/

- Prototype pollution in Javascript or python class pollution
	https://www.coursera.org/learn/javascript-security-part-2/lecture/wMlwD/prototype-pollution-exploit
	time: after 13:50. You can use prototype pollution to run other scripts in your source.
	
- You can use ANSI escape sequences to do cool things with the terminal and hide stuff. 
Eg: https://github.com/swag-wafu/mitre-2019/blob/master/Nyan.md 
	https://www.youtube.com/watch?v=JUOx3puwniE
	
	
- https://trufflesecurity.com/blog/anyone-can-access-deleted-and-private-repo-data-github Can be a misc challenge regarding getting a flag from deleted repo.

- SSTI to read file which links to github pull request about JSON sql in sqlmap which gives idea about JSON based sqli attack which they then havr to perform on the database.
