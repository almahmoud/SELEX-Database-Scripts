import re

File = "selex_db"

previousGene = ""
currentGene = ""
currentSize = 0

genes = []
geneSizes = []
geneTrans = []

sizes = []
trans = []

openFile = open(File, 'r')

loop = True
original = openFile.readlines()
result = []

while(loop):
	loop = False
	for Line in original:
		match = re.search(r'^(>[^\n]+)', Line)
		if match:
			currentGene = match.group(1)
		else:
			if "/" not in Line:
				result.append(currentGene)
				result.append(Line.strip())
			else:
				loop = True
				parts = Line.split(" ")
				found = False
				for each in parts:
					if "/" in each and not found:
						found = True
						poss = each.split("/")
						for nuc in poss:
							result.append(currentGene)
							result.append(Line.replace(each,nuc))
	original = result
	result = []

for Line in original:
	if ">" in Line:
		print Line
	else:
		print Line.replace("\r","").replace(" ","").replace("\n","").upper()



