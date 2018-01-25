#!/usr/bin/python
s = 'azcbobobegghakl'
longest_subset = ""


for i in range(len(s)):
    temp_subset = s[i]
    print ("temp_subset: %s" % temp_subset)
    for letter in s[i+1:]:
        print ("Checking letter: %s" % letter)
        if letter >= temp_subset[-1]:
            temp_subset += letter
            print temp_subset
            if len(temp_subset) > len(longest_subset):
                longest_subset = temp_subset
                print longest_subset
        else:
            print "not valid letter!"
            break

       
print ("Longest substring in alphabetical order is: %s" % longest_subset)
