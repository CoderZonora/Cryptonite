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