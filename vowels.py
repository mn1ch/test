#!/usr/bin/python
s = "azcbobobegghakl"
vowels_counter = 0 
for c in s:
    if c in "aeiou":
        vowels_counter += 1
print("Number of vowels: %d" % vowels_counter)
