# CyberGIS Cloud
Quickly create a Jupyter notebook environment with access to user-defined cloud resources using your own AWS account.

## Steps for a User to get Access Keys
1. Login to AWS.
2. Access AWS IAM service.
3. Navigate to “Users” in the left panel.
4. Click “Create user”.
5. Uncheck “Provide user access to the AWS Management Console - optional”.
6. Click “Next” and then Click “Attach policies directly”.
7. Click “Create policy”.
8. Click “JSON”.
9. Copy and paste the provided permissions policy.
10. Give the policy a name.
11. Click “Next” and then “Create policy”.
12. Go back to your IAM Create user tab, click the refresh icon under “Permission policies” and attach the new policy.
13. Click “Next” and “Create user”.
14. Click on your new user and then click “Security credentials”.
15. Click “Create access key”.
16. Click “Other”.
17. Click “Next” and then ”Create access key”.
18. Copy your access key and secret access key.

## Testing
In order to test, first clone this repository and navigate to the directory containing the Dockerfile. Build the Dockerfile from `docker build -t cybergis .`. Then, run `docker run -it --rm -v ${PWD}:/root cybergis`. In `index.html`, all instances of `https://midware.cigi.illinois.edu:500` and `wss://midware.cigi.illinois.edu:500` should be replaced with `http://localhost:500` and `ws://localhost:500` respectively. Furthermore, the provided `ssl_context` parameter must be removed from the `app.run` function at the bottom of `app.py`. Start the webserver with `python3 app.py` and then open `index.html`. Before the full release of CyberGIS Cloud, testing on the web server can be considered.
