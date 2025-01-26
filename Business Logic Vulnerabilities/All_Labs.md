<img src="images/image1.png" alt="third" width="600">

**Step1:**

Login with given credential

**Step2:**

View first product  leather product and add it to card but keep in mind to on intercept

<img src="images/image2.png" alt="third" width="600">

<img src="images/image3.png" alt="third" width="600">

**Step3:**

Change the price to 1 and forward

**Step4:**

Go to cart

<img src="images/image4.png" alt="third" width="600">

And we can see the price is 0.01

<img src="images/image5.png" alt="third" width="600">

Click on place order and lab is solved
  
<img src="images/image6.png" alt="third" width="600">

**Step1:**

Login with given credential

**Step2**

Click on view product , then add to stock

<img src="images/image7.png" alt="third" width="600">

Click on any product other the jacket in my case I click on 4th product padding pool shoes
.
And add to stock

<img src="images/image8.png" alt="third" width="600">

Now add jacket to cart as well

**Step3:**

Notice the total price is

<img src="images/image9.png" alt="third" width="600">

Now when I add padding shoes to negative the price value decrease
 ,
<img src="images/image10.png" alt="third" width="600">

So we decrement it until the value is less then 100 and then place order  

<img src="images/image11.png" alt="third" width="600">

And click on place order to solve the lab

<img src="images/image12.png" alt="third" width="600">

This lab is basically an integer overflow

Understanding Integer Overflow

Integer Overflow occurs when an arithmetic operation attempts to create a numeric value that is outside the range that can be represented with a given number of bits. In many programming languages, integers have a fixed size (e.g., 32 bits), which means they can represent a finite range of numbers. For a signed 32-bit integer, this range is typically from -2,147,483,648 to 2,147,483,647.

When an operation results in a value greater than 2,147,483,647, it "overflows" and wraps around to the minimum value of -2,147,483,648. Similarly, underflow can occur when a value falls below the minimum range, wrapping around to the maximum value.

**Step1:**

Login with given credential

**Step2:**

Add leather jacket to cart

<img src="images/image13.png" alt="third" width="600">

**Step3:**

Now we send Post /cart request to repeater

<img src="images/image14.png" alt="third" width="600">

When I change price to 100 it show

<img src="images/image15.png" alt="third" width="600">

**Step4:**

Send the request to intruder and select null payload and quantity to 99

<img src="images/image16.png" alt="third" width="600">

Payload setting

<img src="images/image17.png" alt="third" width="600">

With this payload we have negative value

Explanation

 if I select the continue indefinitely we can clear notice the value is continuously positive and negative because of over flow

**Step5:**

Go to repeater and select quantity to 47 and send

<img src="images/image18.png" alt="third" width="600">

Now we have negative value near to -1221

<img src="images/image19.png" alt="third" width="600">

**Step6**

Select any product and order it so the the value set between 0 and 100

<img src="images/image20.png" alt="third" width="600">

Click on place order to buy

<img src="images/image21.png" alt="third" width="600">

**Step1:**

Register account  

<img src="images/image22.png" alt="third" width="600">

The id is of my email server

<img src="images/image23.png" alt="third" width="600">

**Step2:**

If we directly access to admin panel it show message admin panel is only accessable if login as 

**Step3:**

Now we update email address to

`anything@dontwannacry.com`

<img src="images/image24.png" alt="third" width="600">

And now I have access to admin panel  

<img src="images/image25.png" alt="third" width="600">

Delete user carlos

<img src="images/image26.png" alt="third" width="600">

Vulnerability:

Email Truncation Vulnerability:

    • When a user registers with an email address that is exceptionally long, the application server truncates the email address to 255 characters. This is likely due to a database or application-level constraint on the maximum length of email addresses.

    • The user exploits this behavior by crafting an email address such that the part before the truncation point appears to belong to a privileged domain (e.g., dontwannacry.com). As a result, the truncated email address looks legitimate, potentially bypassing domain checks or gaining elevated access.  

**Step1:**

First we register account having email address, containing number of dummy character like

`dummycharacter@email server-id`

<img src="images/image27.png" alt="third" width="600">

When I go to my account we can see  

<img src="images/image28.png" alt="third" width="600">

Here email address is 255 char log

**Step2:**

If we go to /admin we can see admin interface is only available for DontWannaCry user

<img src="images/image29.png" alt="third" width="600">

**Step3:**

Now I make an email

`Anything@dontwannacry.com.emailclint` id

The size of anything till .com should be 255 char  

In my case

```
DontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCcccccccc@dontwannacry.com
```
  
My email address

```
DontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCDontWannaCcccccccc@dontwannacry.com.exploit-0afe00dd037e2131811cd89801f80040.exploit-server.net
```

Now when I log in my account I am an admin user


<img src="images/image30.png" alt="third" width="600">

Delete user carlos


<img src="images/image31.png" alt="third" width="600">

**Step1**

login with given credential


<img src="images/image32.png" alt="third" width="600">

**Step2:**

Change password and send the POST /my-account/change-password request to repeater.


<img src="images/image33.png" alt="third" width="600">

**Step3:**

Change the username to administrator

<img src="images/image34.png" alt="third" width="600">

**Step4:**

Remove current password parameter and send request

<img src="images/image35.png" alt="third" width="600">

**Step5:**

Login to administrator user and delete user carlos


<img src="images/image36.png" alt="third" width="600">

**Step1:**

Login with given credential


<img src="images/image37.png" alt="third" width="600">

**Step2:**

Check the normal work flow

Add an item of less price. In my case I have buy a product for testing that’s why credit is decrease.

Now I brough a product like

<img src="images/image38.png" alt="third" width="350">

**Step3:**

Add this item to cart.

**Step4:**

Click on place order and intercept request


<img src="images/image39.png" alt="third" width="600">

We have this request

<img src="images/image40.png" alt="third" width="600">

Forward

<img src="images/image41.png" alt="third" width="600">

Now we note this

GET /cart/order-confirmation?order-confirmed=true

And after confirmation we have product

<img src="images/image42.png" alt="third" width="600">

**Step5:**

Now we add jacket to stock and change error message with the above request

We have intercept place order request  


<img src="images/image43.png" alt="third" width="600">

Change it to


<img src="images/image44.png" alt="third" width="600">

And forward the request.


<img src="images/image45.png" alt="third" width="600">

And lab is solved.


<img src="images/image46.png" alt="third" width="600">

**Step1:**

Go to /admin request

<img src="images/image47.png" alt="third" width="600">

So it is only accessible if we logged in as admin.  

**Step2:**

Login with given credential and intercept this request

<img src="images/image48.png" alt="third" width="600">

**Step3**

Login to account we see it is asking for role

<img src="images/image_unmap0.png" alt="third" width="600">

Logout and then intercept the login request

We have intercepted request

<img src="images/image49.png" alt="third" width="600">

Forward the request

Now click on drop to drop next request

<img src="images/image50.png" alt="third" width="600">

When I drop this it show error in browser

<img src="images/image51.png" alt="third" width="600">

Remove the /role-selector from the url and again click on enter

<img src="images/image52.png" alt="third" width="600">

Now forward this request and turn off intercept

<img src="images/image53.png" alt="third" width="600">

Now we go to admin panel and delete carlos.

<img src="images/image54.png" alt="third" width="600">

**Step1:**

Login with given credential

**Step2:**

We can see at top

<img src="images/image55.png" alt="third" width="600">

**Step3:**

Now go to bottom and we have signup

Enter any email address


<img src="images/image56.png" alt="third" width="600">

Click on signup

<img src="images/image57.png" alt="third" width="600"> 

Now we have multiple coupen NEWCUST5 and SIGNUP 30
  
**Step4:**

Add leather jacket to stock

First we enter coupen1 and then coupen2.

Here we can clearly see that when we enter first coupon and then enter the second one it will not give an error. But i use same coupon multiple time it say that coupon is already used.

Now when I use both the coupon alternatively it will not show an error and the price decrease on the basis of coupon

<img src="images/image58.png" alt="third" width="600">

<img src="images/image_unmap1.png" alt="third" width="600">

**Step1**

Login with given credential

<img src="images/image_unmap2.png" alt="third" width="600">

Now we paste the email in home -> input box at bottom

`wiener@exploit-0a6e0006034e355d8157ba0c01b70082.exploit-server.net`

<img src="images/image_unmap3.png" alt="third" width="600">

Click on signup we have

<img src="images/image_unmap4.png" alt="third" width="600">

Now add a card to cart and apply coupon we have

<img src="images/image_unmap5.png" alt="third" width="600">

Click on place order 

<img src="images/image_unmap6.png" alt="third" width="600">

**Step2:**

Now go to my-account page and paste the code for redeem and we have 

<img src="images/image_unmap7.png" alt="third" width="600">

It means that it is not redeem the discount it is redeem original price of product

**Step3:**

Now we do this step continously to make the 1000 dollar to buy jacket for this we create a macro base on the request chaining

<img src="images/image_unmap8.png" alt="third" width="600">

Now the highlight are the request flow

```
POST /cart
POST /cart/coupon
POST /cart/checkout
GET /cart/order-confirmation?order-confirmed=true
POST /gift-card
```


**Step4:**

Under `Proxy->proxy Setting->sessions`

<img src="images/image_unmap9.png" alt="third" width="600">

Now add a macro with the above sequence

<img src="images/image_unmap10.png" alt="third" width="600">

**Step5:**

Now we make couple of changes

First we have code in 

`GET /cart/order-confirmation?order-confirmed=true` which is used for redeem 

Click Configure item. In the dialog that opens, click Add to create a custom parameter. Name the parameter gift-card and highlight the gift card code at the bottom of the response. 


<img src="images/image_unmap11.png" alt="third" width="600">


Click ok and then ok


1. Select the POST /gift-card request and click Configure item again. In the Parameter handling section, use the drop-down menus to specify that the gift-card parameter should be derived from the prior response (response 4). Click OK.

<img src="images/image_unmap12.png" alt="third" width="600">

Set gift card from previous response


Now click on test macro to test

<img src="images/image_unmap13.png" alt="third" width="600">

Now when we refresh page the macro is working correctly

**Step6:**

Now make few change

Again click on session
    
<img src="images/image_unmap14.png" alt="third" width="600">

Go to session handling rule

Add a rule 

<img src="images/image_unmap15.png" alt="third" width="600">

Under scope add all url

<img src="images/image_unmap16.png" alt="third" width="600">

Under detail add a rule action name "run a macro" and select a macro

<img src="images/image_unmap17.png" alt="third" width="600">

Click on ok


**Step7**

Now we have to continuously execute macro to increase price

Send a request to intruder let my-account and attack to snipper and payload to null

<img src="images/image_unmap18.png" alt="third" width="600">

Payload setting

<img src="images/image_unmap19.png" alt="third" width="600">

In resource pool we create new resource pool with max concurrent request 1

<img src="images/image_unmap20.png" alt="third" width="600">

Under logger tab we can see macro is working correctly

<img src="images/image_unmap21.png" alt="third" width="600">

It may take time because in one request we are sending 5 request

<img src="images/image_unmap22.png" alt="third" width="600">


Finally when we refresh page we have enough money to buy a jacket

<img src="images/image_unmap23.png" alt="third" width="600">

**Step1:**

Login with given credential and check the stay log in box

<img src="images/image_unmap24.png" alt="third" width="600">


**Step2:**

Go to any post and post with incorrect email

<img src="images/image_unmap25.png" alt="third" width="600">

We have an invalid email address

<img src="images/image_unmap26.png" alt="third" width="600">

**Step3:**

Send the POST /post/comment and GET /post?postId=4 repeater

<img src="images/image_unmap27.png" alt="third" width="600">

The get request

<img src="images/image_unmap28.png" alt="third" width="600">

Here we can see that the response notification of POST request is set as notification cookie in GET request.

Here in GET  response we have

<img src="images/image_unmap29.png" alt="third" width="600">

**Step4:**

Now when we change the email in post request 

<img src="images/image_unmap30.png" alt="third" width="600">

Now when we paste the notification in get  request notification we have

<img src="images/image_unmap31.png" alt="third" width="600">

**Step5:**

When we paste the value of stay logged in in notification we have

<img src="images/image_unmap32.png" alt="third" width="600">

Now in POST /post/comment change email with administrator:time-stamp in my case administrator:1737514757171

And send request

<img src="images/image_unmap33.png" alt="third" width="600">

Copy the notification and paste it in GET request we have

<img src="images/image_unmap34.png" alt="third" width="600">

Now here the length of Invalid email address: is 23 character we have to remove it 

Now we send the notification to burp decoder and decode it url follow by decode base 64

<img src="images/image_unmap35.png" alt="third" width="600">

Select 23 byte from decoded notification right click and remove

Again base encode and then url encode

<img src="images/image_unmap36.png" alt="third" width="600">

Paste it in GET request notification

<img src="images/image_unmap37.png" alt="third" width="600">

**Step6:**

Now here the length should be multiple of 16

For this we send a post request with email value

<img src="images/image_unmap38.png" alt="third" width="600">

Again copy paste the notification value from response in get request

<img src="images/image_unmap39.png" alt="third" width="600">

Now here invalid email till 'a' is multiple of 16 ie.32 character

Invalid email address: qqqqqqqqq


Now again send the notification value to decoder and remove first 32 character

<img src="images/image_unmap40.png" alt="third" width="600">


Again encode and base 64 follow by url encode

<img src="images/image_unmap41.png" alt="third" width="600">


Here we can see we the notification cookies is ok for admin

Send the GET request to repeater and change endpoint to /admin

Delete the session cookie entirely, and replace the stay-logged-in cookie with the ciphertext of your self-made cookie. Send the request. Observe that you are now logged in as the administrator and have access to the admin panel.

<img src="images/image_unmap42.png" alt="third" width="600">

Send a get request to 

<img src="images/image_unmap43.png" alt="third" width="600">

And lab is solved
