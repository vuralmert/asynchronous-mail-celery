<h1>Asynchronous Mail App</h1>
<blockquote>Mail App with Django, Django Rest Framework, Celery, Redis and Docker</blockquote>
<br>
<h2>How Asynchronous Mail App Works?</h2>
<ul>
<li>A client can create a custom mail with Mail Form.
<li>Each mail contains; to field, subject, body, cc and attachments.
<li>Client can also schedule a mail that is set as default. (New features to be add)
</ul>
<h2>Installation</h2>
<ol>
<li><b>Get the code</b>
<p>Clone the repository<pre>git clone https://github.com/vuralmert/asynchronous-mail-celery.git</pre></p>
<li><b>Install the project dependencies</b>
<p>Enter the following command<pre>pip install -r requirements.txt</pre></p>
<li><b>Run the commands to generate the database</b>
<p>Enter the following commands<pre>python manage.py makemigrations</pre><pre>python manage.py migrate</pre></p></ol>
<h2>Usage</h2>
<p>Once you have complete dowloading requirements and migrating and none of the services failed after you have run the following command,<pre>python manage.py runserver</pre>
<ol>
<li><b>Access and Interact with API Front-end App (Django Rest Framework)</b></li>
<p>The API Front-end application should be running and you can see it via your web browser at <a href="http://127.0.0.1:8000/mail_form/"></a>http://127.0.0.1:8000/mail_form which will take you to the main web app interface where
you can create and send your mails.</p>
<p>You can check your previous mails and use query parameters to filter, order or search them via your web browser at <a href="http://127.0.0.1:8000/send_mail/"></a>http://127.0.0.1:8000/send_mail which will take you to the Django Rest Framework interface where you can do these operations.</p>
<p>For the developers I created a Swagger UI which you can access it via your web browser at  <a href="http://127.0.0.1:8000/docs/"></a>http://127.0.0.1:8000/docs which will take you
to the page that you can see all of your apis and schemas.</p>
<li><b>Access Django Admin</b></li>
<ol>
<li>Create the admin user</li>
<p>To access the admin interface first you gonna need to generate a super-user with the following command<pre>python manage.py createsuperuser</pre>You will be prompted to add a <code>username</code> and <code>password</code> for your user.<br></br>
<li>Logging to admin interface</li>
<p>Once you have complete creating the super-user you can visit <a href="http://127.0.0.1:8000/admin/"></a>http://127.0.0.1:8000/admin which will take you to the admin interface login screen. You should enter the <code>username</code> and <code>password</code> created in the previous step.
</ol>
<li><b>Scheduling Mails with Celery</b></li>
<ol>
<li>To use this feature first you need to install Redis from <a href="https://redis.io/download/"></a>https://redis.io/download/ and then config your Redis files. Once Redis server is installed, open the terminal and run the following command to start the server.<br></br><pre>redis-server</pre></li>
<li>Before running any commands or connecting any clients to the Redis server, you must ensure that Redis is running.<br></br><pre>redis-cli ping</pre>Returns <code>PONG</code> if the server is up and running.</li><br></br>
<li>After making sure that Redis is installed and working properly enter the custom command that I created for ease of use of the codes we will use for Celery and Flower.<br></br><pre>python manage.py run_and_schedule</pre></li>
<p>The API Back-end application and tasks should be running and your scheduled mails will be sent to the active users you have created from the admin interface. You can check running and previous tasks via your web browser at <a href="http://127.0.0.6:5555/"></a>http://127.0.0.6:5555 which will take you to the Flower interface.</p> 
</ol></ol>
<h2>Endpoints</h2>
<ul>
<li><code>GET     /send_mail</code>
<li><code>POST    /send_mail</code>
<li><code>POST    /mail_form</code>
<li><code>GET     /sent_mails</code>
<li><code>GET     /schedule_mail</code>
</ul>
<h2>Used Technologies</h2>
<ul>
<li>Python
<li>Django
<li>Django Rest Framework
<li>Celery
<li>Redis
<li>Flower
<li>Docker
</ul>
