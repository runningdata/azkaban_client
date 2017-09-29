
```py

# -*- coding: utf-8 -*


user = 'azkaban'
pwd = 'azkaban'
host = 'http://10.2.19.62:8081'
import urllib2,json, urllib

from azkaban_client.azkaban import *

import argparse, requests

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--group',dest='group',
                    action='store',
                    default='jlc',
                    help='specify the target schedule group: jlc, xiaov')
parser.add_argument('--jobtype',dest='jobtype',
                    action='store',
                    default='etls',
                    help='specify the target jobtype: m2h, etls, h2m')
parser.add_argument('--schedule',dest='schedule',
                    action='store',
	            type=int,
                    default=0,
                    help='specify the target schedule type: 0(day), 1(week), 2(month)')
parser.add_argument('--cancel',dest='cancel',
		    type=bool,
                    action='store',
                    default=True,
                    help='going to cancel a flow if it has been reached timeout?')
parser.add_argument('--flow_timeout',dest='flow_timeout',
                    type=int,
                    action='store',
                    default=210,
                    help=u'timeout for a flow')
args = parser.parse_args()

def get_file_name(proj):
    zip_file = '/tmp/{filename}.zip'.format(filename=proj)
    print('Got job file %s' % zip_file)
    return zip_file

def go_schedule(project, target_file):
    # get cookies
    fetcher = CookiesFetcher(user, pwd)

    # create project
    project = Project('WillTest', 'first test', fetcher)
    project.create_prj()

    # upload zipfile to the project
    project.upload_zip(target_file)

    # execute and monitor all the flows in this project
    for flow in project.fetch_flow():
        execution = flow.execute()
        execution.handle_timeout()
    print('all end for %s ....' % project.name)

print args
prj_name = 'h2h-20170928161948'
go_schedule(prj_name, get_file_name(prj_name))


```
