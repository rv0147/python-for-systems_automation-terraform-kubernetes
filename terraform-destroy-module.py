import os
import subprocess
import time
import argparse

parser   = argparse.ArgumentParser(description='This program need to have a region name passed as a parameter. Example: dev, stage, prod')
parser.add_argument('regionname', help=':pass a region name as parameter to the script- for example: ./scriptname dev or python scriptname dev')
args = parser.parse_args()

path = "/home/user/path-to-the-terraform-modules"
current = os.getcwd()
print("current directory is %s" % current)


if args.regionname == "dev":
  os.chdir("/home/user/path-to-the-terraform-modules/dev")
elif args.regionname == "stage":
  os.chdir("/home/user/path-to-the-terraform-modules/stage")
elif args.regionname == "prod":
  os.chdir("/home/user/path-to-the-terraform-modules/prod")
else:
  print("please enter a valid region as an argument  like dev or stage or prod")

refresh = subprocess.call(['terraform', 'refresh'])

start_time = time.localtime()

print("Timer started at %s" % time.strftime('%X', start_time))


code = subprocess.call(['terraform', 'destroy' , '-auto-approve'])
if code == 0:
  print("code executed successfully")
else:
  print("error code is %i" % code)


stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print("Timer stopped at %s" % time.strftime('%X', stop_time))

print("Total time: %s seconds" % difference)
