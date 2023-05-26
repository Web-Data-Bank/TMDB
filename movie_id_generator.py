import sys, os


file_path = 'file_names.txt'

with open(file_path, 'r') as file:
    movies_id = [int(line.strip()) for line in file]

movies_id.sort()

c = 0
for i in range(int(len(movies_id)/5000)):
    with open("movie_id/"+str(i)+".text", "w") as f:
        for item in movies_id[:5000]:
            f.write(str(item) + "\n")
        del movies_id[:5000]