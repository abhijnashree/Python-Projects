import csv

# with open('file.csv','a',newline="")as myfile:
# 	wr=csv.writer(myfile,dialect='excel')
# 	wr.writerow(['game of thrones','winter is coming'])
# 	wr.writerow(['game of thrones','winter is coming'])
# 	wr.writerow(['game of thrones','winter is coming'])
# 	wr.writerow(['game of thrones','winter is coming'])
# 	wr.writerow(['game of thrones','winter is coming'])




with open('file.csv','r',newline="")as myfile:
	rd=csv.reader(myfile)
	for i in rd:
		print(i)
