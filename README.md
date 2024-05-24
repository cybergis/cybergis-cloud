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

