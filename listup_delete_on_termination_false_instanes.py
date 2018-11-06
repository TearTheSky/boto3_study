#! /usr/bin/env python3
# coding: utf-8
import sys
import boto3
import datetime
import pprint
import datetime
import time
import json
from boto3.session import Session
from bson import json_util

def listup_delete_on_termination_false_instanes(ec2_cli):
    try:
        response = ec2_cli.describe_instances(
            Filters=[
                {
                    'Name': 'block-device-mapping.delete-on-termination',
                    'Values': [
                        'false'
                    ]
                },
            ],
            #InstanceIds=[
            #    'string',
            #],
            DryRun=False,
            MaxResults=1000
            #NextToken='string'
        )
        return json.dumps(response["Reservations"], default=json_util.default)

    except Exception as e:
        print( '=== エラー内容 ===')
        print( e.args )
        print( e.message )
        return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Caution：引数が足りません。")
        exit()

    my_session = boto3.session.Session(profile_name=sys.argv[1])
    ec2_cli = my_session.client('ec2')

    my_result = listup_delete_on_termination_false_instanes(ec2_cli)
    print(my_result)
