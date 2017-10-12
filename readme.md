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
 
