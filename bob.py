#!/usr/bin/python
s = "azcbobobegghakl"
bobs = 0 
for i in range(0, len(s)):
    chunk = s[i:i + 3]
    if chunk == "bob":
        bobs += 1
print ("Number of times bob occurs is: %d"%bobs)
