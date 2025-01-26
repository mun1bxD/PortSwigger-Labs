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

<img src="images/image_unmap1.png" alt="third" width="600">

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
