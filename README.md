# Sakura Manga Tracker
Grabs manga from Batoto, and stuffs it into a nice HTML wrapper.

<h1>What is this?</h1>
<p>It's a bunch of python that will automatically download manga from batoto and put it into a nice easily-readable format.
<p>Currently only Batoto scraping is supported, more may be in the works eventually.
<p>If you dump a bunch of images following the directory structure, the display half should still work on its own.

<h1>How do I make it work?</h1>
<p>First, you need python. I've done all my testing and development on 3.4, so that's the ideal version to run it under.
<p>There are two .py files you should worry about -- "server.py" and "autoscrape.py".
<p>Server will run as a stand-alone HTTP server on port 8000, which makes it so that you can access the program's interface through a standard web browser. Run it with 
```
python server.py
```
and all should be well. If you're running your own server with a python module, you can ignore this, though you might have to do a little config to make sure that all the links are still pointing at the right places.

<p>Autoscraper works the same way:
```
python autoscraper.py
```
which will automatically run the scraper and queue it up to run again every hour. The scraper is what actually downloads the pages you want. 
<p>If you're running windows, you should add both of these files to your task scheduler engine. On linux, stuff them in your crontab. Alternatively, you can directly run "RunScraper.py" (in the Scraper dir) on whatever interval you like.

<h1>How do I use it?</h1>
<p>Once it's all set up, visit <a href="http://localhost:8000/index.py">http://localhost:8000/index.py</a> and you'll be good to go.
<p>Fill out forms and follow directions from there.
<p>Once you've imported something and added it to your grid, it will show up in index.py. Red outline means updated.
<p>When you open a manga page, it will load only after the last image you've seen, and it will save your position for later. Fiddle with the "page" field in the URL if you want to change this.

<h1>It's broken!</h1>
<p>Check errors.log to see if there's something going on, like a broken connection.
<p>Also try <a href="http://localhost:8000/index.py?page=user">resetting your profile</a> to see if that clears things up.
<p> If that fails, <a href="mailto:antonpaquin@gmail.com">send me an email.</a>

<h1>I want to rice it!</h1>
<p>When you create a profile it adds a dir to Users and copies a bunch of CSS into that ("Users/???/CSS/*"). Most pages you see when you have a user cookie will take CSS from there. It's safe to edit.

<hr>
<p>This is a program that grew organically over a period of about six months. It's been cleaned up a lot in this latest revision, but there still might be some weirdness.
Let me know if you have anything you'd like to add; otherwise, enjoy the manga!
