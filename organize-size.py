import re
import copy

HTPSELEX = "new_htpselex.txt"
SELEXDB = "new_sdb.txt"
FileNames = [[HTPSELEX,"HTPSELEX"],[SELEXDB,"SELEXDB"]]
for eachFile in FileNames:

	dbName = eachFile[1]
	openFile = open(eachFile[0], 'r')
	genes = []
	geneSizes = []
	geneTrans = []
	currentGene = ""
	currentSize = 0
	sizes = []
	trans = []

	for Line in openFile:
		match = re.search(r'^>([^\n]+)', Line)
		if match:
			currentGene = ">" + dbName + ": " + match.group(1)
			sizes = []
			trans = []
			if currentGene not in genes:
				genes.append(currentGene)
				geneSizes.append(sizes)
				geneTrans.append(trans)
			else:
				i = genes.index(currentGene)
				sizes = geneSizes[i]
				trans = geneTrans[i]

		else:
			Line = Line.strip()
			currentSize = len(Line)
			if currentSize > 1 and currentSize in sizes:
				i = sizes.index(currentSize)
				currentTrans = trans[i]
				currentTrans.append(Line)
			else:
				sizes.append(currentSize)
				i = sizes.index(currentSize)
				currentTrans = []
				currentTrans.append(Line)
				trans.append(currentTrans)

	for g in range(len(genes)):
		print genes[g]
		for trans in geneTrans[g]:
			for t in trans:
				print t
