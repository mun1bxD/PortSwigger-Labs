**Step 1:**

Login with given credential

**Step 2:**

Create a .php and save this exploit

`<?php echo file_get_contents('/home/carlos/secret'); ?>`

**Step 3:**

We can see in burpsuite the file is upload and in responcewe have answer

**Step 1:**

In this lab we cannot directly upload a file it give error

**Step 2:**

So in this lab we change the content type to image/png in burpuite and file will be uploaded

So first we intercept the request.

**Step 3:**

Change content type to image/png or image/jpeg

I first send it to repeater

From here it is clear that file is uploaded.

**Step4:**

Stop intercept and see the result

**Step 1:**

In this lab we again upload file with same payload.but it will not give error and not execute the file.

**Step 2:**

In this case we will upload file to one level up. But the ../ will be url encoded like

Send the request to repeater

**Step 3:**

Change file name to

../payload.php but url encoded like:..%2fpayload.php

In url we have the result

**Step1**

First upload fille payload.php

**Step 2**

Now we turn on intercept and try by changing changing extension

Send it to repeater.

**Step 3**

Now we change the server setting  by sending .htaccess extension and add this line

`AddType application/x-httpd-php .newEXT`

Here the extension is change to newEXT

Now we upload file with extension payload.newEXT

Now fie is uploaded and webshell is executed successfully.

**Step 1:**

First we upload file as it is

It only get png and jpg file

**Step 2:**

Again we turn on intercept and send the request to repeater.

**Step3**

Now we changing extension by adding null bytes

Now  the file is uploaded successfully

**Step1**

To solve this lab we make a file with php extension and a payload in its meta deta. Other properties of a images file.

So we use command

`exiftool -Comment="<?php echo 'starting point<< ' . file_get_contents('/home/carlos/secret') . ' >>Ending of file'; ?>" cat.png -o payload.php`

Now we one php file is created but other properties of png file

Uploading this file and we have a secret.
