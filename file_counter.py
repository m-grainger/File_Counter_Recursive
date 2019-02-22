import os

"""
Important!  Please read!

Drop this file in the directory you want to scan.  For example, if I want to count EML files of a converted PST job, I would throw
it here --> /inbox/123_abc_company_1234567/EMLFiles

This is not thouroughly tested, and is meant to be useful for troubleshooting why your conversion totals do not match.  Use this in conjunction of 
tail.exe to create lists that you can compare to each other to see where the mis-matches are.

"""

# creates a list of directories in a given folder
dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), d))]

total_count = []

for x in dirs:
	total = 0 #initializing a counter

	for r, d, files in os.walk(x):
		total += len(files)
		print(f"Scanning {d}...")

	with open(f"counts.txt", "a") as f:
		f.write(f"{x} - Total: {total}\n")
	total_count.append(total)	

with open(f"counts.txt", "a") as f:		
	f.write(f"\nTotal Files Counted: {sum(total_count)}")
print("Complete :)")
