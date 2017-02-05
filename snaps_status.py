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

conn = ec2.connect_to_region(region_name='eu-west-1', profile_name=args.profile)


# snaps = conn.get_all_snapshots(snapshot_ids=args.snap)
# print(dir(snaps[0]))
# for snap in snaps:
#     print(snap.status).format(status=snap.status)

mins = 5
old_time = datetime.utcnow() - timedelta(minutes=mins)
while True:
    snaplist = conn.get_all_snapshots()
    for snap in snaplist:
        start_time = datetime.strptime(snap.start_time, '%Y-%m-%dT%H:%M:%S.000Z')
        if start_time > old_time:
            print("ID: {snap_id} Status: {status} Progress: {progress} Cur. Date: {date}" ).format(snap_id=snap.id,
                                                                                  status=snap.status,
                                                                                  progress=snap.progress,
                                                                                  date=datetime.utcnow())
    time.sleep(10)
    old_time = datetime.utcnow() - timedelta(minutes=mins)



de