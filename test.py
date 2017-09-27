from azkaban import *

fetcher = CookiesFetcher(user, pwd)
project = Project('WillTest', 'first test', fetcher)
project.create_prj()
project.upload_zip('/tmp/h2h-20170923030038.zip')
for flow in project.fetch_flow():
    execution = flow.execute()
    execution.handle_timeout()

print('all end....')
