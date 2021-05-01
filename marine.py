import urllib.request
import ssl
import csv



ssl._create_default_https_context = ssl._create_unverified_context

def northern():
    url = "https://www.ndbc.noaa.gov/data/realtime2/TBIM4.txt"
    file = urllib.request.urlopen(url,"r")
    tsv_file = file
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    for row in read_tsv:
	    print(row)
    tsv_file.close()
		

def southern():
	url = "https://www.ndbc.noaa.gov/data/realtime2/45149.txt"
	file = urllib.request.urlopen(url)
	

	for line in file:
		print(line)
    

def northOrSouth(nothern, southern):
    nOrS = input("Would you like to see Northern or Southern data?")

    if(nOrS=="Southern"):
	    southern()
    elif(nOrS=="Northern"):
	    nothern()

    else: print("Invalid input")
northOrSouth(northern, southern)


