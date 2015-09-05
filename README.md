# Python3-ipv6hostscanner
Probably useless but a functional IPv6 host scanner written in Python3 using threading


Intro
To perform a regular (brute force) network scans in an IPv6 Network is almost impossible it can take over 5.000 years to finish.

This project was purely academic and I just wanted to learn about threading in Python.

This software is not recommended for general usage.....

This  script  will call the OS to actually perform the ping

This software receives two parameters:

a) Prefix to scan in the format 2001:db8::/64 (subnet, not host)
b) Number of simultaneous processes it can run (MAXPINGS) 

One more time it was purely academic stuff but hopefully it can make your day
