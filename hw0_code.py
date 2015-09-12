file = open('iowa-liquor-sample.csv','r')
count = 0;

for line in file:
	if "single malt scotch" in line.lower():
		count = count + 1
print "There are a total of %d lines in this file that contain 'single malt scotch'" % count
