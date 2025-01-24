**What is path traversal?**

Path traversal is also known as directory traversal. These vulnerabilities enable an attacker to read arbitrary files on the server that is running an application. This might include:

- Application code and data.
- Credentials for back-end systems.
- Sensitive operating system files.

In some cases, an attacker might be able to write to arbitrary files on the server, allowing them to modify application data or behavior, and ultimately take full control of the server.

**Reading arbitrary files via path traversal**

Imagine a shopping application that displays images of items for sale. This might load an image using the following HTML:

`<img src="/loadImage?filename=218.png">`

The `loadImage` URL takes a `filename` parameter and returns the contents of the specified file. The image files are stored on disk in the location `/var/www/images/`. To return an image, the application appends the requested filename to this base directory and uses a filesystem API to read the contents of the file. In other words, the application reads from the following file path:

`/var/www/images/218.png`

This application implements no defenses against path traversal attacks. As a result, an attacker can request the following URL to retrieve the /etc/passwd file from the server's filesystem:

`[https://insecure-website.com/loadImage?filename=../../../etc/passwd](https://insecure-website.com/loadImage?filename=../../../etc/passwd)`

This causes the application to read from the following file path:

`/var/www/images/../../../etc/passwd`

The sequence `../` is valid within a file path, and means to step up one level in the directory structure. The three consecutive `../` sequences step up from `/var/www/images/` to the filesystem root, and so the file that is actually read is:

`/etc/passwd`

On Unix-based operating systems, this is a standard file containing details of the users that are registered on the server, but an attacker could retrieve other arbitrary files using the same technique.

On Windows, both `../` and `..\` are valid dirversal sequences. The following is an example of an equivalent attack against a Windows-based server:

`[https://insecure-website.com/loadImage?filename=..\..\..\windows\win.ini](https://insecure-website.com/loadImage?filename=..\..\..\windows\win.ini)`

<img src="images/image1.png" alt="third" width="800">

**Step1:**

Click on view details and intercept it in burpsuite.

<img src="images/image2.png" alt="third" width="400">

**Step 2**

We have intercept request  like this:

<img src="images/image3.png" alt="third" width="800">

**Step 3**

Forward this request

<img src="images/image4.png" alt="third" width="800">

Now we change path and also send it to repeater to see the response

<img src="images/image5.png" alt="third" width="800">

And lab is solved.

**Common obstacles to exploiting path traversal vulnerabilities**

Many applications that place user input into file paths implement defenses against path traversal attacks. These can often be bypassed.

If an application strips or blocks directory traversal sequences from the user-supplied filename, it might be possible to bypass the defense using a variety of techniques.

You might be able to use an absolute path from the filesystem root, such as `filename=/etc/passwd`, to directly reference a file without using any traversal sequences.

<img src="images/image6.png" alt="third" width="800">

**Step1**

Intercept request by clicking on view description button

**Step 2**

Request look like this

<img src="images/image7.png" alt="third" width="800">

Forward it

<img src="images/image8.png" alt="third" width="800">

Again forward multiple time we have request

<img src="images/image9.png" alt="third" width="800">

**Step3**

Send it to repeater

And change filename =/etc/passwd

<img src="images/image10.png" alt="third" width="800">

And lab is solved

**Common obstacles to exploiting path traversal vulnerabilities - Continued**

You might be able to use nested traversal sequences, such as ....// or ....\/. These revert to simple traversal sequences when the inner sequence is stripped.

<img src="images/image11.png" alt="third" width="800">

This lab is very similar to the above labs.

We simply forward intercept multiple time and in image request we use this exploit

filename=....//....//....//....//etc/passwd

<img src="images/image12.png" alt="third" width="800">

**Common obstacles to exploiting path traversal vulnerabilities - Continued**

In some contexts, such as in a URL path or the `filename` parameter of a `multipart/form-data` request, web servers may strip any directory traversal sequences before passing your input to the application. You can sometimes bypass this kind of sanitization by URL encoding, or even double URL encoding, the `../` characters. This results in `%2e%2e%2f` and `%252e%252e%252f` respectively. Various non-standard encodings, such as `..%c0%af` or `..%ef%bc%8f`, may also work.

For Burp Suite Professional users, Burp Intruder provides the predefined payload list Fuzzing - path traversal. This contains some encoded path traversal sequences that you can try.

<img src="images/image13.png" alt="third" width="800">

this lab is very similar to the above labs.

We simply forward intercept multiple time and in image request we use this exploit

filename=....//....//....//....//etc/passwd

We only double encode // and /

double encode:`..%25%32%66%25%32%66..%25%32%66%25%32%66..%25%32%66%25%32%66etc%25%32%66passwd`

<img src="images/image14.png" alt="third" width="800">

**Common obstacles to exploiting path traversal vulnerabilities - Continued**

An application may require the user-supplied filename to start with the expected base folder, such as /var/www/images. In this case, it might be possible to include the required base folder followed by suitable traversal sequences. For example: filename=`/var/www/images/../../../etc/passwd.
`
<img src="images/image15.png" alt="third" width="800">

Above step is skip because this is same as other

<img src="images/image16.png" alt="third" width="800">

**Common obstacles to exploiting path traversal vulnerabilities - Continued**

An application may require the user-supplied filename to end with an expected file extension, such as .png. In this case, it might be possible to use a null byte to effectively terminate the file path before the required extension. For example: filename=`../../../etc/passwd%00.png.`

<img src="images/image17.png" alt="third" width="800">

<img src="images/image18.png" alt="third" width="800">

**Note:** there is one thing that in all lab we forward request after intercept until we get image get request.

Example:intercept result forward

<img src="images/image19.png" alt="third" width="500">

<img src="images/image20.png" alt="third" width="500">

<img src="images/image21.png" alt="third" width="500">

<img src="images/image22.png" alt="third" width="500">

<img src="images/image23.png" alt="third" width="500">
