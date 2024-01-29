The source code provided had two php files secret.php and index.php. 
Also the webiste was just a simple webpage, nothing but a textbox with a shout button.
secret.php contained this :

![image](https://github.com/CoderZonora/Rishabh_Bachhawat/assets/140229408/dc52c400-9c63-4d33-b185-86eaa95f0144)

This hinted to me that maybe $FL4ggggggggggg was also the actual variable which had the real flag. 
Also the index.php determined the input conditions for the textbox on the website. 

The code showed that the input had to be non-alphanumeric, have less than 7 unique chacters and the total length of the input should be less than 300 characters.
The source code also revealed that text entered into the “shout” input field is passed to a PHP eval() function after first undergoing the above validation checks. In essence, the application dynamically evaluates unsafe PHP code pieced together like so:

$res='some_garbage_text_here $voice some_more_garbage'; where $voice was the input I enter.

After searching a bit I found that one way to exploit this could be to use a XOR function for providing the inputs. Tried this github tool (https://github.com/Keeperr/NAN-generator/tree/master) but did not work as it was very hard to fit the input within the given validation checks.

Another approach I tried was to use unicode characters instead of normal alphabets but even after a lot of tries could not get the flag.

