



**Step1**

Login with given credential


**Step2**

Send any set request to repeater

image1

Now when we change endpoint to /admin we have



As we Know JWT has three part we will decode the middle part.



Now we change the wiener to administrator and apply changes

Now we can see admin interface is visible


Simply change the request method and to delete carlos change endpoint to /admin/delete?username=carlos


And user Carlos is deleted successfully.



The second lab is similar to first simply we change algo to none and remove signature part
Header.Payload.Signature


And the lab is solved.





**Step1**

Login with given credential

**Step2:**

Now we create a new RSA key for this install JWT editor from extension.



Now click on New rsa key and generate

**Step3:**

Right click on new key and copy it as public key as JWK

Go to exploit server create a new Keys object like
{
 "keys":[]
}

And in Square bracket paste the key


Store it and make note of kid.

**Step4:**

Go to burpsuite and send the GET /my-account?id=wiener to repeater 

Remove the id=wiener

And we have same response.


**Step4:**

Go to JSON web token which is shown in above Snippet

Replace the kid with our own new kid
And add a jku header and value of the jku is the exploit server 
https://exploit-0a3a007d0365e96780bcb12501e700a6.exploit-server.net/exploit



In payload replace the wiener with administrator



Click on sign and the new JWT is sign.

Now when we send the request to repeater we have


**Step5:**

Now we simply delete user carlos

Sending a post delete request to admin panel the below is snippet of get simply change it to post






**Step1:**

Login with given credential

**Step2:**

Send the my-account request to repeater



Remove ?id=wiener and send request we can see that we are still login


**Step3:**

Now we see json web token 



**Step4:**

Now we generate new public key using JWT editor




**Step5:**

Now we go to repeater again
Click on attack at bottom and select embeded jwt


And click okay we have new jwk header


Change name to administrator and click on sign to sign jwt and we can see we are login as admin




Now we send a Post request at admin/delete endpoint to delete user carlos



And the username is deleted successfully.





