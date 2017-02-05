import argparse
from boto import ec2
from collections import Counter
import pprint
import operator
import time
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument('--profile', help='choose profile', required=True)
args = parser.parse_args()

region = 'eu-west-1'

conn = ec2.connect_to_region(
    region_name='eu-west-1', profile_name=args.profile)


snaps = conn.get_all_snapshots(owner='self')



for snap in snaps:
    print("Snap ID {id}, Orig_vol_size: {size} ,  Date Taken: {date}, status: {status}").format(
        id=snap.id, size=snap.volume_size, date=snap.start_time, status=snap.status)
    # print(dir(snap))
    #print(dir(snap))
print("There is {count} Snaps!!").format(count=len(snaps))