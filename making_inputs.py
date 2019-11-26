import string
import secrets
import glob
import os
import os.path
import csv
import random


def pass_gem(size=12):
    chars = string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(chars) for x in range(size))

def user_and_pass(number):
	with open('users.csv', 'w') as f:
		for i in range(number):
			csv_id = i+1
			id_z = str(csv_id).zfill(2)
			prefix = 100 + int(id_z)
			user = str(prefix) + "@hoge.com"
			passw = pass_gem(12)
			r = str(csv_id) + "," + str(user) + "," + str(passw) + "\n"
			f.write(r)


if __name__ == "__main__":
    user_and_pass(50)