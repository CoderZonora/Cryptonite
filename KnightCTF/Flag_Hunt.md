Had to bruteforce the password for the zip. Used fcrackzip with rockyou.txt list.


![image](https://github.com/CoderZonora/KnightCtf/assets/140229408/8f318805-f828-442b-8722-b8c6fb1b96dd)


It was '**zippo123**'.


There were many files and when I sorted by size and type found that there was a audio file which had morse code which decoded to **MORSECODETOTHERESCUE!!** and out of all the images one was a bit larger size. 

![image](https://github.com/CoderZonora/KnightCtf/assets/140229408/0494e24f-d963-4898-b7a6-4d11d1f729f4)

![image](https://github.com/CoderZonora/KnightCtf/assets/140229408/dab9c5a6-1038-4d55-ad4b-148bb32a9de9)

Also there was a n0t3.txt which said that the flag is here and to use LowerCase. 


So used steghide on the image file with passphrase **morsecodetotherescue** which gave the flag.


Flag: KCTF{3mb3d_53cr37_4nd_z1pp17_4ll_up_ba6df32ce}
