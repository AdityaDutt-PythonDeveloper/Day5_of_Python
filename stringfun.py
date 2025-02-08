string = "Aditya"
print(len(string))
print(string.endswith('ya'))

word = 'aabbccddaa'
print(word.count('a') , word.count('c'))
print(word.capitalize())
print(word.find("daa"))
print(word.replace("daa", "cbb"))#this new string will be shared in new mermory area 
print(word)
#This proves that string are inmutable