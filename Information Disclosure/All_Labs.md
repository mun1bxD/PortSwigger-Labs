  
## Information Disclosure

**Step1**

click on view product


**Step2:**

Send the post request to repeater

**Step3:**

Change product id to any character other then number

And we have answer 2 2.3.31


**Step1**

Click on view product on home page

**Step2**

Now we have to find all comment from a site

For this in target> sitemap right click on wesite id and go to engagement tool > search for comment


**Step3:**

Copy this link and send the get request to repeater

In repeater we have output

**Step1:**

Append /robots.txt  to url

**Step2:**

Now replace /robots.txt with

**Step3:**

Open link

Submit the answer

**Step1:**

when we access admin panel by adding /admin in url it shows message.

**Step2:**

On the other hand if we render the response of GET /admin we can see clearly two user. but we are not able to delete them

**Step3:**

when we replace GET with TRACE we can see in response we have a `X-Custom-IP-Authorization` parameter.

**Step4:**

in order to pass this we simple set the custom Ip to local host for this we Go to proxy-> then http history and in match and replace we add X-Custom-IP-Authorization:127.0.0.1

now when we refresh the main page we have access of admin panel.

Go and delete user carlos.  

**Step1:**

in this app when we type `/.git` in URL we have access to git history

**Step2:**

Simply install them using `wget -r lab-id/.git`

**Step3:**

Install a tool for version control. In this lab we use git cola for GUI.

**Step4:**

open the downloaded folder in git cola.

  

uncommit the last change

  

we can see password here.
