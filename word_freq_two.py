
with open("my_data") as my_file:
    contents = my_file.read().lower().replace("\n", " ").replace('"', ' ').replace("'", " ").replace("?", " ").replace("-", " ").replace("--", " ").replace(".", " ").replace(",", " ").replace("!", " ").replace(";", " ").replace(":", " ").split()

each_word = set(contents)

d = {}

for word in each_word:
    d[word] = contents.count(word)

def help_sorting(num):
    return num[1]

top_twenty = sorted(d.items(), key = help_sorting, reverse = True)
for d in top_twenty [:20]:

    print(d)
