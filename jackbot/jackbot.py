import csv
import os
import sys

# Open pornhub iframes
#with open('pornhub.com-db.csv', newline='') as porns:
#    pornreader = csv.reader(porns, delimiter=',', quotechar='|')
#    for row in pornreader:
#        print(row + "\n")


def main():

    # Can't do much without the list of iframes
    if not os.path.isfile('pornhub.com-db.csv'):
        print("Need to download the csv of pornhub iframes: ")
        print("http://pornhub.com/pornhub.com-db.zip")
        sys.exit(0);
   
    
if __name__ == '__main__':
    main()
