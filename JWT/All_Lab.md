<img src="images/image1.png" alt="third" width="500">

**Step1**

Login with given credential

<img src="images/image2.png" alt="third" width="500">

**Step2**

Send any set request to repeater

<img src="images/image3.png" alt="third" width="500">

Now when we change endpoint to /admin we have

<img src="images/image4.png" alt="third" width="500">

As we Know JWT has three part we will decode the middle part.

<img src="images/image5.png" alt="third" width="500">

Now we change the wiener to administrator and apply changes

Now we can see admin interface is visible

<img src="images/image6.png" alt="third" width="500">

Simply change the request method and to delete carlos change endpoint to /admin/delete?username=carlos

<img src="images/image7.png" alt="third" width="500">

And user Carlos is deleted successfully.

<img src="images/image8.png" alt="third" width="500">

The second lab is similar to first simply we change algo to none and remove signature part
Header.Payload.Signature

<img src="images/image9.png" alt="third" width="500">


And the lab is solved.

<img src="images/image10.png" alt="third" width="500">

**Step1**

Login with given credential

**Step2:**

Now we create a new RSA key for this install JWT editor from extension.

<img src="images/image11.png" alt="third" width="500">


Now click on New rsa key and generate

**Step3:**

Right click on new key and copy it as public key as JWK

Go to exploit server create a new Keys object like
{
 "keys":[]
}

And in Square bracket paste the key

<img src="images/image12.png" alt="third" width="500">

Store it and make note of kid.

**Step4:**

Go to burpsuite and send the GET /my-account?id=wiener to repeater 

Remove the id=wiener

And we have same response.

<img src="images/image13.png" alt="third" width="500">

**Step4:**

Go to JSON web token which is shown in above Snippet

Replace the kid with our own new kid
And add a jku header and value of the jku is the exploit server 
https://exploit-0a3a007d0365e96780bcb12501e700a6.exploit-server.net/exploit

<img src="images/image14.png" alt="third" width="500">

In payload replace the wiener with administrator

<img src="images/image15.png" alt="third" width="500">

Click on sign and the new JWT is sign.

Now when we send the request to repeater we have

<img src="images/image16.png" alt="third" width="500">

**Step5:**

Now we simply delete user carlos

Sending a post delete request to admin panel the below is snippet of get simply change it to post

<img src="images/image17.png" alt="third" width="500">

<img src="images/image18.png" alt="third" width="500">

**Step1:**

Login with given credential

**Step2:**

Send the my-account request to repeater

<img src="images/image19.png" alt="third" width="500">

Remove ?id=wiener and send request we can see that we are still login

<img src="images/image20.png" alt="third" width="500">

**Step3:**

Now we see json web token 

<img src="images/image21.png" alt="third" width="500">

**Step4:**

Now we generate new public key using JWT editor

<img src="images/image22.png" alt="third" width="500">


**Step5:**

Now we go to repeater again
Click on attack at bottom and select embeded jwt

<img src="images/image23.png" alt="third" width="500">

And click okay we have new jwk header

<img src="images/image24.png" alt="third" width="500">

Change name to administrator and click on sign to sign jwt and we can see we are login as admin

<img src="images/image25.png" alt="third" width="500">

Now we send a Post request at admin/delete endpoint to delete user carlos

<img src="images/image26.png" alt="third" width="500">

And the username is deleted successfully.





