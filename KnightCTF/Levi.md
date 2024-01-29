So the challenge is similar to where are the robots from picoCTF.
We look for the robots.txt text file which tells the engine crawlers about which URL's the crawlers can access on the site. 
So we can just do **http://66.228.53.87:5000/robots.txt**. We can see that it disallows going to /l3v1_4ck3rm4n.html. 


So we can go there by **http://66.228.53.87:5000/l3v1_4ck3rm4n.html**, and it displays the flag.


Flag - KCTF{1m_d01n6_17_b3c4u53_1_h4v3_70}
