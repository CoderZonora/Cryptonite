Forensics report:

Tool learnt about: Volatility 
Use: To analyze memory dumps of Windows,Linux,Mac.


Volatility 2 vs 3 : Volatility 2 is the older version of Volatility which relied on the 
concept of profiles which had to be explicitly provided to get a proper output form the memory dump.It had a lot of different plugins 
available for different tasks to be done directly, like the clipboard plugin to directly 
get to clipboard concepts without having to explicitly dump its concepts via the process Id.
Volatility3 on the other hand automatically selects the profile for a particular memory dump file. 
It also relies on plugins but the number of plugins are currently quite limited.


Volatility2:
So to start with a memory analysis mainly starts with seeing the process tree and the active processes at the time when the dump was taken. 
These can be accomplished by the use of the ps-scan, ps-tree plugins. ps-tree works better and provides a hierarchical view of the processes with the Pid & PPids.
We can then also dump out each individual process and the memory associated with them using the procdump and memdump commands to analyze them separately.
procdump gives us just the binary itself while memdump dumps the entire memory associated with that process to disk for further analysis.


Also got to know about cmdscan and consoles to get commmand line output. modscan shows the drivers running and netscan helps to analyze network connections.
imagecopy can be used to convert images from other formats to raw which volatility can analyze.

malfind ,malprocfind and hollowfind are plugins which automatically tries to detect suspicious processes and show them which we can then analyze.
It uses different checks to determine if a file is deemed suspicious.
Like if svchost.exe does not have services.exe as parent process or if a process in memory does not have a coressponding file on disk or there is VAD and PEB mismatch.


Also learnt about the process genelogy on windows and what are the normally expected processed which run on a windows system and their use.
The most basic process is smss.exe which starts at system boot,spawns subprocesses to create other processes like csrss.exe,wininit.exe and winlogon.exe which may then end. 
So the parent process name for these processes might be empty for this reason.SImilarly winlogon.exe spawns services.exe which gives rise 
to the multiple svchost.exe we can see in the process tree.

Also got an introduction to Redline and how to use it to get memory dumps from systems. There are also options to analyze the memory files in a gui interface.

Learnt about autoruns and how malware can persist after reboot and restarts using Auto-Start Extensibility Points(ASEP's).
It basically matches files running in memory with those in Autostart locations.

Prefetch plugin can be used to analyze the Windows prefetch files in memory to see the timestamps of different processes and how many times they have ran.
But it has a limit on the number of entries that can be stores for each process.

Volatility 3 used plugins in the form of windows.pslist.PsList with the required arguments like --pid.

So this cheatsheet helps to remember syntax of dfferent commands between ween vol2 and vol3: https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet
