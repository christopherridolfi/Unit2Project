#What is a dictionary
example_dictionary = {"year":2019,"maker":"honda","4door":True}#dictionary
print(example_dictionary["maker"])
print(example_dictionary["year"])

#adding/append dictionary
example_dictionary["type"] = "civic type r" #creates the key "type? and adds the value "civic type r" to it.
print(example_dictionary["type"])
#remove things from dictionary
#del dictionaryname["new key"]
del example_dictionary["year"]

#Challenge:
dictionarynames = {"name1":"chris","name2":"David","name3":"rob"}
print(dictionarynames)

dictionarynum = {"hi":1,"ho":2,"Hu":3}
del dictionarynum["hi"]
print(dictionarynum)

emptydictionary = {}
emptydictionary["just"] = "hello bro"
emptydictionary["chriz"] = "my name"
emptydictionary["dumb"] = "me"
print(emptydictionary)


keys = ["alex","hi","abama"]
lastone = {keys[0]:1,keys[1]:2,keys[2]:3}
if "a" in keys[0][0]:
    g = keys[0]
    del lastone[g]
if "a" in keys[1][0]:
    f = keys[1]
    del lastone[f]
if "a" in keys[2][0]:
    c = keys[2]
    del lastone[c]
    print(lastone)

for x in keys:
    if "a" in x[0]:
        del emptydictionary[keys[x]]