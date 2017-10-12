## preparation

create venv in source-dir 
```
virtualenv venv
source venv/bin/activate
 
pip install flask flask-ask zappa requests
##pip install boto3 #optional
```


## deploy lambda
https://developer.amazon.com/de/blogs/post/8e8ad73a-99e9-4c0f-a7b3-60f92287b0bf/new-alexa-tutorial-deploy-flask-ask-skills-to-aws-lambda-with-zappa

```
zappa deploy dev
```

```
(venv) mprescha@isdeblnnm148 ~/git/alexa-read-bucket on master [+!?]$ zappa deploy dev
(six 1.10.0 (/Users/mprescha/git/alexa-read-bucket/venv/lib/python2.7/site-packages), Requirement.parse('six==1.11.0'), set([u'zappa']))
Calling deploy for stage dev..
Creating alexa-read-buck-dev-ZappaLambdaExecutionRole IAM Role..
Creating zappa-permissions policy on alexa-read-buck-dev-ZappaLambdaExecutionRole IAM Role.
Downloading and installing dependencies..
 - cryptography==2.1.1: Downloading
100%|████████████████████████████████████████████████████████████████████| 2.18M/2.18M [00:00<00:00, 3.57MB/s]
 - cffi==1.11.2: Downloading
100%|██████████████████████████████████████████████████████████████████████| 406K/406K [00:00<00:00, 3.51MB/s]
Packaging project as zip.
Uploading alexa-read-buck-dev-1507817480.zip (6.9MiB)..
100%|████████████████████████████████████████████████████████████████████| 7.21M/7.21M [00:01<00:00, 6.99MB/s]
Scheduling..
Scheduled alexa-read-buck-dev-zappa-keep-warm-handler.keep_warm_callback with expression rate(4 minutes)!
Uploading alexa-read-buck-dev-template-1507817496.json (1.6KiB)..
100%|████████████████████████████████████████████████████████████████████| 1.64K/1.64K [00:00<00:00, 6.82KB/s]
Waiting for stack alexa-read-buck-dev to create (this can take a bit)..
100%|██████████████████████████████████████████████████████████████████████████| 4/4 [00:09<00:00,  2.83s/res]
Deploying API Gateway..
Deployment complete!: https://we77adufv0.execute-api.eu-west-1.amazonaws.com/dev
```