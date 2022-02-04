#!/usr/bin/env python
import json
from typing import Dict

from acitoolkit import Session, Tenant, AppProfile, BridgeDomain, EPG, PhysDomain, Context, NetworkPool, Node


def main():

    # Connection
    # session = Session("https://10.10.20.14", "admin", "C1sco12345")
    session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
    session.login()

    vpc_name = "VPC10-IPG"
    url = "/api/mo/uni/infra/funcprof/accbundle-{}.json".format(vpc_name)
    resp = session.get(url)
    if not resp.ok:
        print("Fail")
    else:
        print("dir: {}".format(dir(resp)))
        print("content: {}".format(resp.text))
        print("type: {}".format(type(resp.text)))

        content: Dict = json.loads(resp.text)
        print("totalCount: {}".format(content['totalCount']))
        if content['totalCount'] is "1":
            print("found: {}".format(content['imdata']))
        else:
            print("NOT found: {}".format(content['imdata']))

        # print("??: {}".format(resp.text['totalCount']))


if __name__ == '__main__':
    main()
