import photocollect
import usernames
import argparse
import time

uname = argparse.ArgumentParser()
uname.add_argument("-u", "--username", required=True,help="User Name")
args = vars(uname.parse_args())
uname = args["username"]
print("Collecting Following usernames")
usernames.getfollowing(uname)
print("Collected Successfull")


file = open("userlist.txt","r")
for i in file: 
	print(i.split("\n")[0])
	print("Collecting Photos")
	photocollect.main(i.split("\n")[0])
	print("Collected Successfull")
	print("Saved File : " + i.split("\n")[0] + ".jpg")
	time.sleep(0.1)
file.close()
