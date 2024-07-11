What are synchronous and asyncronous functions?
https://code.pieces.app/blog/synchronous-and-asynchronous-programming-in-javascript

What is Truthy and Falsy?
[]()

Basics of javascript programming security: 
Basics of javascript authentication methods like Cookies,JWT etc.

Facebook warning when opening console in dev tools. Maybe use something similar in a CTF?

Clickjacking,how to prevent iframes of your site using `X-Frame-Options:Deny` or `frame-ancestors` CSP policy.

Subsource integrity - Having hases of the js and css files addes to the code such that browser can check that what is being loaded by the CDN 
for example is the exact same code that the developer wrote and has not being tampered with by a malicious bad actor.

If you use Regex with exec like so: `console.log(reg.exec(str))` the cursor will have a state at the last matched position even for new strings, 
the state is global and the index rolls back to 0 after encountering an end once.

Another <b>recommended<b> way of doing other things than just matching: Call the method on the String class instead of the RegEx class. 
This way you can use the patters individually instead of having a global cursor. 
String class methods supported by RegEx are:

```
String.prototype.match;
String.prototype.matchAll;
String.prototype.search; // returns the index  of first match or -1 if no match
String.prototype.replace;
String.prototype.replaceAll;
String.prototype.split;
```
How to use:

`console.log(str.match(reg));`


Prototype pollution:
Background on objects and classes etc:
	If you assign a property as undefined it does not delete it!. It sets the value to undefined but its still listed under the object.
	So if you call it like `ob.x; => undefined` which is also the output if you call properties not under the object. 
	

What is package-lock? A package.json file but with hash of the dependencies as well so that Supply chain or MITM will be prevented.
	
Summary of imp. points:

Serverless javascript may not be directly vulnerable to DoS but may be vulnerable to Money Dos malicious payloads may spike up running time and bills to a lot.
Always use CI/CD and deploy scripts. Don't store secrets hardcoded, either .env or manually put. 	
Don't console.log everything as it might have private info, just log enough things so that you can trace errors and find out how to fix them.
Use shell commands inside <b>Child.spawn</b> and not exec or others.
Use PHP and not serverless if you want one thread per process.

Use <b>SYNK</b> to check for vulnerable packages along with npm sudit as they have a large database.
Run untrusted code in a Docker container first to check it. Use firewalls to prevent your local 
application being accessible to other people on the same network like in an office.
Dont use public networks when devloping or running application 

Don't deploy dev dependencies into production.
specify the kind of dependency in the package.json like devdependency,bundle dependencies,optional dependencies etc. 
For exact details see [here](https://docs.npmjs.com/cli/v10/configuring-npm/package-json#dependencies)
Use https://npm.anvaka.com or https://www.npmjs.com/package/@nodesecure/cli to find details(visually) about dependencies you want to use to 
make an informed decision about if it is good for your use case.