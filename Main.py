"""
Author: Mark Craft
Date: 9/18/2023
Retrieve public facing documents from  related websites
Then downloads the file locally on your machine
"""
from googlesearch import search
from tqdm import tqdm
# Google query to replicate
query = "site:*.org filetype:pdf"
all_links = []
i = 0
count_down = 0

kal_links_write = open("kal2_links", 'a')
params = {'filter': '0'}
# Add each result to a text file, appends to the end of the file, may need to clear out duplicates
results = search(query, tld="co.in", num=20, start=294, stop=0, pause=10)

with tqdm(total=100, unit='file') as progress_bar:
	for j in search(query, tld="co.in", num=10, start=294, stop=0, pause=30, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36", extra_params=params):
		if j not in all_links:
			all_links.append(j)
			print(j)
			progress_bar.update(1)
			i += 1
			print("current count = " + str(i))
			count_down += 1
			kal_links_write.write(j)
			kal_links_write.write("\n")

print("pdf results down (new start point for next run): " + str(count_down))
print("Total number of links found " + str(i))
kal_links_write.close()

"""
outfilename = "kal_nodups.txt"
infilename = "kal_links"

lines_seen = set() # holds lines already seen
outfile = open(outfilename, "w")
for line in open(infilename, "r"):
	if line not in lines_seen:  # not a duplicate
		outfile.write(line)
		lines_seen.add(line)

outfile.close()
"""