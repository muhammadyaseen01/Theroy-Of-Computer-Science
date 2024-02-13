import re
# People whose CNIC number starts with 1, are residents of Khyber Pakhtunkhwa province, similarly, 2 represents FATA, 3 for Punjab, 4 for Sindh, 5 represents Balochistan, 6 for Islamabad and 7 represents Gilgit-Baltistan province.

#CODE:

# cnic_pattern = re.compile(r'^(\d{5})-\d{7}-\d$')
# cnic_pattern = re.compile(r'^[1-7]\d{4}-\d{7}-\d$')
# cnicPattern = re.compile(r'^[1-7][0-9]{4}-[0-9]{7}-[0-9]$') #r for raw-input/regex
cnicPattern = '^[1-7][0-9]{4}-[0-9]{7}-[0-9]$'


# cnic = "12345-1234567-1"
cnic = input("Enter your CNIC number: ")

match = re.search(cnicPattern, cnic)
if match:
    firstDigit = cnic[0]
    latsDigit = cnic[-1]
    if firstDigit == '1':
        print("KPK")
    elif firstDigit == '2':
        print("FATA")
    elif firstDigit == '3':
        print("PUNJAB")
    elif firstDigit == '4':
        print("SINDH")
    elif firstDigit == '5':
        print("BALOCHISTAN")
    elif firstDigit == '6':
        print("ISLAMABAD")
    elif firstDigit == '7':
        print("GILGIT-BALTISTAN")
    # print("First digit of CNIC:", firstDigit)
else:
    print("Invalid CNIC number format")
