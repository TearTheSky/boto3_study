#! /usr/bin/env python3
# coding: utf-8
import sys
import boto3
import argparse
from boto3.session import Session

def parse_args():
    parser = argparse.ArgumentParser(
        description="S3バケットの一覧を取得し、そのバケット名とイベント通知設定について出力するスクリプト。",
        usage="{}  --profile <aws profile name> ".format(__file__))
    parser.add_argument('--profile', required=True,
                        help="利用するAWSクレデンシャルのプロファイル名")
    return parser.parse_args()

def listup_buckets_with_events_notification(s3_cli):
    bucket_list = s3_cli.list_buckets()
    for a_bucket in bucket_list["Buckets"]:
        try:
            a_bucket_notification = s3_cli.get_bucket_notification_configuration(Bucket = a_bucket["Name"])
            print(a_bucket["Name"])
            print(a_bucket_notification)
            print()
            continue
        except Exception as AccessDenied:
            print("Access Denied Bucket Notification or Nothing")
            print()

            continue


if __name__ == "__main__":
    args = parse_args()

    my_session = boto3.session.Session(profile_name=args.profile)
    s3_cli = my_session.client('s3')

    my_result = listup_buckets_with_events_notification(s3_cli)
    print(my_result)
