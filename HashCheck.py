#Reading was too much work so I made this instead

Hash = input("Enter Downloaded Hash");
HashComparison = input("Enter Official Hash");

if (Hash == HashComparison):
    print("Hash Check Passed")
else:
    print ("Hash Check Failed")