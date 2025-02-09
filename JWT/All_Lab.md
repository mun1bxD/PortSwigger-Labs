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


<img src="images/image27.png" alt="third" width="500">

**Step1:**

Login with given credential

<img src="images/image28.png" alt="third" width="500">

**Step2:**

Now we will break jwt using jwtlist

```bash
hashcat -a 0 -m 16500 eyJraWQiOiI2NGM3YjY4OC04ZWFkLTQxYjUtOGJlYi0zOGQzZTZjYTkwNGMiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczNjQzNzkwMywic3ViIjoid2llbmVyIn0.2lfp7ol4pSQp6QN7WGyo8NYBQSlZFWRXuX6fHVpW94s jwt.secrets.list
```
This list is present github [jwt.secrets.list](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list)

<img src="images/image29.png" alt="third" width="500">

In result we have cracked jwt is secret

<img src="images/image30.png" alt="third" width="500">

Now we generate new jwt key and replace k with `secret1`

<img src="images/image31.png" alt="third" width="500">

Now we type /admin in url

<img src="images/image32.png" alt="third" width="500">

Send the request to repeater

Change name from wiener to administrator

<img src="images/image33.png" alt="third" width="500">

And sign using key

<img src="images/image34.png" alt="third" width="500">

In my case the jwt editor  signing is not working I use below  python script to generate a token

```python
import jwt
import base64
import json
# Header
header = {
    "kid": "50ca54a1-98cf-4981-9166-dfce1979ed1c",
    "alg": "HS256"
}
payload = {
    "iss": "portswigger",
    "exp": 1736442966,
    "sub": "administrator"
}
# Secret Key (decoded from base64)
secret_base64 = "c2VjcmV0MQ=="
secret = base64.b64decode(secret_base64).decode("utf-8")
# Encode JWT
token = jwt.encode(payload, secret, algorithm="HS256", headers=header)
print("Generated JWT:", token)
```

And we have admin access

<img src="images/image35.png" alt="third" width="500">

Send a get request to /admin/delete?username=carlos 

<img src="images/image36.png" alt="third" width="500">

And the lab is solved

<img src="images/image37.png" alt="third" width="500">


**Step1:**

Login with given credential

**Step2:**

Access /admin from url it show not accessible

**Step3:**

From http history send /admin to repeater

<img src="images/image38.png" alt="third" width="500">

**Step4:**

Now there is a traversal issue in kid so we point it to dev/null in order to return empty string

And set the sub to administrator

<img src="images/image39.png" alt="third" width="500">

Generate a symmetric key from JWT editor extension and add an empty byte in k parameter

<img src="images/image40.png" alt="third" width="500">

Click on sign to sign

<img src="images/image41.png" alt="third" width="500">

Here I use the below python script for generating JWT token 

```python
import jwt
import base64
import json
# Header
header = {
    "alg": "HS256",
    "kid": "../../../dev/null",
    "typ": "JWT"
}
payload = {
    "iss": "portswigger",
    "exp": 1736442966,
    "sub": "administrator"
}
# Secret Key (decoded from base64)
secret_base64 = "AA=="
secret = base64.b64decode(secret_base64).decode("utf-8")
# Encode JWT
token = jwt.encode(payload, secret, algorithm="HS256", headers=header)
print("Generated JWT:", token)
```

When I send the request we have admin access

<img src="images/image42.png" alt="third" width="500">

Now we send the Get request to /admin/delete?username=carlos to solve lab

<img src="images/image43.png" alt="third" width="500">

## Vulnerability

The server uses the `kid` parameter to locate the key file on the filesystem. However:  
1. The server does not sanitize the `kid` value.  
2. An attacker can use path traversal sequences like `../../../../../../../dev/null` to point the `kid` to arbitrary files on the server.  

In this lab, the server does not verify the contents of the key file, so:  
- If the `kid` points to `/dev/null`, it reads from the null device, which always returns an empty string.  
- This effectively makes the signing key an empty string.  

## Why Use `/dev/null` and `AA==`

### 1. `/dev/null`:
- It’s a special file that discards all input and returns nothing (empty string) on read.  
- By pointing `kid` to `/dev/null`, the server treats the signing key as an empty string.  

### 2. `AA==`:
- This is the Base64 encoding of a null byte (`\x00`).  
- The JWT Editor extension does not allow using an empty string as a key, so using a null byte as a workaround is sufficient.  
- The null byte (`AA==`) functions like an empty key when signing and verifying JWTs.  




