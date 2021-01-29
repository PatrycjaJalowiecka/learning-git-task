Zakupy = ["chleb", "bułki", "pączek", "marchew", "seler", "rukola"]
Zakupy_dict = {"piekarnia" : ["chleb", "bułki", "pączek"], "warzywniak" : ["marchew", "seler", "rukola"]}
Ilość = len(Zakupy)
Zakupy_dict1 = {key: [Zakupy.capitalize() for Zakupy in Zakupy_dict[key] ] for key in Zakupy_dict } 

def cap_string(d): 
    return d.capitalize()

Zakupy_dict2 = {}

for key in Zakupy_dict1:
    Zakupy_dict2[cap_string(key)] = Zakupy_dict1[key]
    
for k in Zakupy_dict2:
    print("Idę do", k, "i kupuję tam", Zakupy_dict2[k])
print("W sumie kupuję %s produktów." % Ilość ) 