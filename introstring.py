name = 'harry'
# string is imuutable
'''
String indexing starts from 0 if we are counting from the begining & and if we started counting from the last indexing starts from -1
'''
LengthOfString = len(name)
print(LengthOfString)

nameshort = name[0:3]
#start from index 0 all the way till 3 (excluding 3)
print(nameshort)

#negative slicing
'''
['h', 'a', 'r', 'r', 'y']
['-5','-4','-3','-2','-1']
To remember it simply convert the -ve index to correesponding positive index
'''
print(name[-4:-1])
#-1 is not included
print(name[1:4])
print(name[:4])
#if noithing is written it means 0 index
print(name[1:])
#is same as print(name[1:5]) where 5 is length of string
print(name[1:5])

#slicing with skip value
word = 'amazing'
print(word[1:6:2])
# 1 seh chalo 6 tak jao aur 2 steps skip karo