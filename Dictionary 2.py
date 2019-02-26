"""exdictionary = {"hi":2, "hola":4}
print(exdictionary["ahi"])
if "hi" in exdictionary:
    print("hola")"""

""".clear() - deletes all contents of a dictionary
.items() - returns all key, value pairs
.get(key) - returns the value for the passed key
.keys() - returns a list of all keys
.values() - returns a list of all values

**len() also works with Dictionaries**
"""

"""for x in exdictionary:
    print(x) #This only prints key
    if "a" in x:
        print("hi")"""

list = [9,10,12]
dictionary = {1:2,2:list,3:6,5:8}
for x in dictionary.items():
    print(x)
print(list)

#2
dictionary2 = {1:"hi",2:"ho",3:"ha"}
def function(dictionary,value):
    for x in dictionary:
        if value == dictionary[x]:
            print(x)

function(dictionary2,"hi")

#3
list2 = [1,2,3,4]
dic = {0:1,1:2,2:3,3:4}

#4
acdictionary = {}
j = input("How many words u wanna input")
for t in range(1,int(j)+1):
    k = input("What is you word")
    i = input("What is you Definition")
    acdictionary[k] = i
    print(acdictionary)

#5

list = [0,1,2,3,4,5,6,7]
listdic = {list}



