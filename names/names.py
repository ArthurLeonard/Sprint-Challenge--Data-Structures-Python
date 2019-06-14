import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
names_2_dict = { i : 3 for i in names_2 }

# for i in range(200)
# 	print(i)
# adict.get('dogname', default)
duplicates = []
for name_1 in names_1:
    if names_2_dict.get(name_1, None) != None:
         duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

