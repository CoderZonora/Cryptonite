The challenge gave two files : A wav file called peaceful.wav and a jpg called 'clue.jpg'. First tried Aperisolve on the jpg file but found nothing. Then when seeing the metadata saw some encoded data in the comments:

![Screenshot 2024-01-24 190226](https://github.com/CoderZonora/KnightCtf/assets/140229408/e5c6da5b-e9e7-4876-99df-b067224d7a7c)

Used [Multidecoder](https://www.cachesleuth.com/multidecoder/) and found text it was base32 encrypted. Original text was : **theoceanisactuallyreallydeeeepp**. Tried this as the steghide password but to no luck.


For the .wav file I tried a morse decoder but it did not work so it was not morse code in the audio. After searching a bit for tools which  are somehow connected to the word **deep** ( as that was mentioned hyperbolically in the text ) found Deep Sound and used it successfully on the audio file with the extracted phrase as password to get a flag.png file. But could not figure out where the flag was in this. 

Later learnt that it was just there if I had used strings on the image.

Flag : KCTF{mul71_l4y3r3d_57360_ec4dacb5}

