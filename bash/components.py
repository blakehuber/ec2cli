#!/usr/bin/env python3
"""

ec2cli, GPL v3 License

Copyright (c) 2018-2021 Blake Huber

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import sys
import boto3

session = boto3.Session(profile_name='default')
client = session.client('ec2')
ec2 = session.resource('ec2')

container = []


# Instance Ids
ids = [instance.id for instance in ec2.instances.all()]

# EBS Volume Ids
vids = [x['VolumeId'] for x in client.describe_volumes()['Volumes']]

# snapshot Ids
sids = [x['SnapshotId'] for x in client.describe_snapshots(OwnerIds=['self'])['Snapshots']]

# ami ids
amis = [x['ImageId'] for x in client.describe_images(Owners=['self'])['Images']]

# elastic network interfaces (eni)
enis = [x['NetworkInterfaceId'] for x in client.describe_network_interfaces()['NetworkInterfaces']]


# aggregate all ids into single list
container.extend(ids)
container.extend(vids)
container.extend(sids)
container.extend(amis)
container.extend(enis)

for x in container:
    print(x)

##

sys.exit(0)
