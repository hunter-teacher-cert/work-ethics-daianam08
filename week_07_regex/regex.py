# NOTE from Daiana: Unsure why it prints out with all the spaces and the names separated in this way, but I got the names to print out at least! When I did this in the regex program, it selected the names no problem. Thanks again for the extension!

import re

def find_name(line):
    pattern = r"((\w+)|(Mr|Ms|Mx)?(\.)?( )(\w)( )?(\w)?( )?(\D)?( )?(\w+))"
    result = re.findall(pattern,line)

    # print("---")

    # pattern = r"[\w]"
    # result = result + re.findall(pattern,line)

    return result


#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19"
#print(result)

f = open("namefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)