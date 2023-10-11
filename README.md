# CyberGIS Cloud

Various configuration scripts (that must be publicly available) are [here](https://github.com/anuj-p/CyberGIS-cluster-scripts).

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
10. Click “Next” and then “Create policy”.
11. Go back to your IAM Create user tab, click the refresh icon under “Permission policies” and attach the new policy.
12. Click “Next” and “Create user”.
13. Click on your new user and then click “Security credentials”.
14. Click “Create access key”.
15. Click “Other”.
16. Click “Next” and then ”Create access key”.
17. Copy your access key and secret access key.
