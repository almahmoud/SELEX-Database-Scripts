import re

FileName = "database.txt"
File2 = "new_sdb.txt"
FileNames = [FileName,File2]

valid = ["A","T","C","G"]

fromChange = ["N","R","Y","S","W","K","M","B","D","H","V","U"]
toChange = [["A","C","G","T"],["A","G"],["C","T"],["C","G"],["A","T"],["G","T"],["A","C"],["C","G","T"],["A","G","T"],["A","C","T"],["A","C","G"],["T"]]

previousGene = ""
currentGene = ""
currentSize = 0

genes = []
geneSizes = []
geneTrans = []

sizes = []
trans = []

for eachFile in FileNames:	
	openFile = open(eachFile, 'r')
	

	for Line in openFile:
		match = re.search(r'^(>[^\n]+)', Line)
		if match:
			currentGene = match.group(1)
			if previousGene != currentGene:
				if currentGene in genes:
					j = genes.index(currentGene)
					sizes = geneSizes[j]
					trans = geneTrans[j]
				else:
					genes.append(currentGene)
					sizes = []
					geneSizes.append(sizes)
					trans = []
					geneTrans.append(trans)
				previousGene = currentGene

		else:
			orig = Line.strip().replace("\r","").upper()
			currentSize = len(orig)
			if currentSize > 0:

				currentTrans = []
				if currentSize in sizes:
					i = sizes.index(currentSize)
					currentTrans = trans[i]
					
				else:
					sizes.append(currentSize)
					## It's pass by reference so can add it before adding elements to it
					trans.append(currentTrans)




				nucList = []
				possibilities = 1

				# for nuc in orig:
				# 	if nuc in valid:
				# 		nucList.append([nuc])
				# 	else:
				# 		if nuc in fromChange:
				# 			c = fromChange.index(nuc)
				# 			replacement = toChange[c]
				# 			nucList.append(replacement)
				# 			possibilities = possibilities * len(replacement)
				# 		else:
				# 			print("Error: Don't know what to replace this with: %s", nuc)

				# newList = [""] * possibilities

				if possibilities == 1:
					if orig not in currentTrans:
						print currentGene
						print orig
						currentTrans.append(orig)

				else:
					num = possibilities

					for smList in nucList:
						num = num / len(smList)
						count = 0
						while count < (possibilities-1):
							for rep in smList:
								for r in range(num):
									newList[count] = newList[count] + rep
									count += 1

					for seq in newList:
						if seq not in currentTrans:
							print currentGene
							print seq
							currentTrans.append(seq)
