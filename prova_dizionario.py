my_dict = {
    "ImageWidth" : [4000]
}

my_dict["ImageWidth"].append(3000)

for key in my_dict.keys():
    key = str(key) + "1"

print(my_dict)