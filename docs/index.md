# azkaban_client
client based on restful API




#### Create a project

```py

from azkaban import *

fetcher = CookiesFetcher(user, pwd)
project = Project('WillTest', 'first test', fetcher)
project.create_prj()

```


#### Upload zip file to the project

```py
project.upload_zip('/tmp/xxx.zip')
```

#### Get all flows from a prject

```py
project.fetch_flow()
```
