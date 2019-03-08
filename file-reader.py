import os.path
import os
import glob


""" 
Clear all smaller play files that may have been created previously
"""
def clearSourceFiles(sourceFilePath):
	for filepath in glob.iglob('source\\*.csv'):
	    if filepath != sourceFilePath:
	    	os.remove(filepath)

""" 
Splits large play by play files spanning multiple years into
smaller csv files including only one season.
"""
def createYearlyFiles():
	sourceFilePath = "source\\play-by-play-2008-2018.csv"
	f = open(sourceFilePath, "r")

	clearSourceFiles(sourceFilePath)

	plays = f.readlines()
	key   = plays[0]
	plays = plays[1:]

	fileDict = {}
	for line in plays:
		p = line.split(",")
		if p[1][4:6] in ["01", "02"]:
			print(p[1])
			filename = "source/play-by-play-" + str(int(p[1][0:4])- 1) + ".csv"
		else:
			filename = "source/play-by-play-" + p[1][0:4] + ".csv"
		if filename not in fileDict:
			print("Created " + filename)
			fileDict[filename] = open(filename, "w")
			fileDict[filename].write(key)


		fileDict[filename].write(line)

	for key in fileDict:
		fileDict[key].close()

if __name__ == "__main__":
	createYearlyFiles()
