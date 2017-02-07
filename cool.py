import argparse
from boto import ec2
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('--profile', help='choose profile', required=True)
parser.add_argument('--keypairname', help='choose keyname', required=True)
args = parser.parse_args()

# import ansible.runner
# import ansible.playbook
# import ansible.inventory
# from ansible import callbacks
# from ansible import utils
# import json

aws_region = "eu-west-1"
instance_type = "t2.medium"
ami = ""


def create_key_pair(profile_name, key_name):
    conn = ec2.connect_to_region('eu-west-1', profile_name=profile_name)

    conn.create_key_pair(key_name=key_name)
    time.sleep(2)
    return

def check_if_key_pair_exists(keypairin, profile_name):
    conn = ec2.connect_to_region('eu-west-1', profile_name=profile_name)
    keypairs = conn.get_all_key_pairs()
    for keypair in keypairs:
        if keypair.name == keypairin:
            return True
    return False



def create_instance(profile_name, instance_type, ami_type, key_pair):
    conn = ec2.connect_to_region('eu-west-1', profile_name=profile_name)
    res = conn.run_instances(instance_type=instance_type, image_id=ami_type, key_name=key_pair)
    return res.instances[0]

def terminate_instance(profile_name, instance_id):
    conn = ec2.connect_to_region('eu-west-1', profile_name=profile_name)
    print("Termiminating instance id: {id}").format(id=instance_id)
    remove = conn.terminate_instances(instance_ids=instance_id)
    print(dir(remove))
    # while remove.state != 'terminated':
    #     print("instance state: {state}").format(state=remove.state)
    #     time.sleep(5)
    return

def remove_keypair(keypair):
    return




if __name__ == '__main__':
    # try:
    #     create_key_pair(profile_name=args.profile, key_name=args.keypairname)
    # except:
    #     sys.exit(1)
    #
    res = create_instance(profile_name=args.profile, instance_type=instance_type, ami_type=ami, key_pair=args.keypairname)
    #print(dir(res))
    #instance = res.instances
    while res.state != 'running':
        time.sleep(5)
        res.update()
    #print(".")
    time.sleep(7)
    print("instance ip: {ip}, instance id: {id}").format(ip=res.ip_address, id=res.id)
    time.sleep(2)
    #print(".")
    terminate_instance(profile_name=args.profile, instance_id=res.id)
    #hosts = [res.ip_address]
    if check_if_key_pair_exists(keypairin=args.keypairname, profile_name=args.profile):
        print("keypair {key} exists").format(key=args.keypairname)
    else:
        print("keypair {key} doesn't exist").format(key=args.keypairname)
