## Typetalk WebSocket client sample

### Setup

#### Install required libraries

```
$ pip install -r requirements.txt
```

#### Register application to issue token

[Create your application](https://typetalk.in/my/develop/applications/register) to use API. When issuing client id and client secret, you should select "Client Credentials" for "Grant Type".

### Run sample application

You should set the following environment variables to run the sample application in advance.

```
$ export TYPETALK_CLIENT_ID=XXXX
$ export TYPETALK_CLIENT_SECRET=XXXX
$ ./main.py
```
