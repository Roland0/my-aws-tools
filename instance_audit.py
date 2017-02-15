import argparse
from boto import ec2
from collections import Counter
import pprint
import operator

parser = argparse.ArgumentParser()
parser.add_argument('--profile', help='choose profile', required=True)
args = parser.parse_args()

region = 'eu-west-1'

conn = ec2.connect_to_region(
    region_name='eu-west-1', profile_name=args.profile)

reservations = conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]

ec2running = 0
ec2stopped = 0
ec2terminated = 0
ec2types = Counter()
for instance in instances:
    #print("ID: {id} State: {state} Type: {instance_type}").format(id=instance.id, state=instance.state, instance_type=instance.instance_type)
    ec2types[instance.instance_type] += 1
    if instance.state == 'running':
        # print(dir(instance))
        # print("AMI-ID: {instance_ami").format(instance.)
        ec2running += 1
    elif instance.state == 'stopped':
        ec2stopped += 1
    elif instance.state == 'terminated':
        ec2terminated += 1


print("EC2:")
print(" Total instances: {total}").format(total=len(instances))
print("   Running:    {running}").format(running=ec2running)
print("   Stopped:    {stopped}").format(stopped=ec2stopped)
print("   Terminated: {terminated}").format(terminated=ec2terminated)
