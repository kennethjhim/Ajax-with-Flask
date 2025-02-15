### Flask Ajax Zipcode
Go to https://www.zipcodeapi.com/ and click on free use. It will send the key to your email but you have to activate the email first.

Then to test it locally and resolve CORS issues, follow this link

https://www.zipcodeapi.com/zipblog/docs/2016/04/14/zipcode-testing-locally-and-resolving-cors-issues.html

Copy the flask template. Create virtual env as follows

1. Issue in the terminal
`$ python3 -m venv env`

2. Activate by going
`$ source env\bin\activate`

3. Install all requirements by
`$ pip install -r requirements.txt`

4. Issue

`$ flask run`

In the application/templates folder copy the following to index.html

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Ajax Zip Code</title>
    <style>
      #entry {
        margin: 2em 1em;
      }
      #location {
        margin: 1em;
      }
    </style>
  </head>
  <body>

    <div id="entry">
      Zip code: <input id="zipcode" type="text" name="zipcode" />
      <button id="ajax-button" type="button">Submit</button>
    </div>

    <div id="location">
    </div>

    <script>
      
      var api = 'https://www.zipcodeapi.com/rest/js-8Qys7e6Y1CAKRN2A4m0g2osY54aeKUfIcI3Oi9xYeSoDLJ3Q8qlCi2ghcumWemKc/info.json/';

      function findLocation() {
        var zipcode = document.getElementById('zipcode');
        var url = api + zipcode.value + '/degress';
        console.log(url)

        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);

        xhr.onreadystatechange = function () {
          if(xhr.readyState < 4) {
            showLoading();
          }
          if(xhr.readyState == 4 && xhr.status == 200) {
            setTimeout(function() { }, 2000);
            outputLocation(xhr.responseText);
          }
        };
        xhr.send();
      }

      function showLoading() {
        var target = document.getElementById('location');
        target.innerHTML = 'Loading...';
      }

      function outputLocation(data) {
        var target = document.getElementById('location');
        var json = JSON.parse(data);
        var address = json.city + " " + json.state;
        // console.log(json);
        target.innerHTML = address;
      }

      var button = document.getElementById ("ajax-button");
      button.addEventListener("click", findLocation);
    </script>

  </body>
</html>

```

### Flask Ajax Button

1. Issue in the terminal
`$ python3 -m venv env`

2. Activate by going
`$ source env\bin\activate`

3. Install all requirements by
`$ pip install -r requirements.txt`

4. Issue

`$ flask run`


In the index.html, add the following

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Asynchronous Button</title>
    <style>
      #blog-posts {
        width: 700px;
      }
      .blog-post {
        border: 1px solid black;
        margin: 10px 10px 20px 10px;
        padding: 6px 10px;
      }

      button.favorite-button, button.unfavorite-button {
        background: #0000FF;
        color: white;
        text-align: center;
        width: 70px;
      }
      button.favorite-button:hover, button.unfavorite-button:hover {
        background: #000099;
      }

      button.favorite-button {
        display: inline;
      }
      .favorite button.favorite-button {
        display: none;
      }
      button.unfavorite-button {
        display: none;
      }
      .favorite button.unfavorite-button {
        display: inline;
      }

      .favorite-heart {
        color: red;
        font-size: 2em;
        float: right;
        display: none;
      }
      .favorite .favorite-heart {
        display: block;
      }
    </style>
  </head>
  <body>
    <div id="blog-posts">
      <div id="blog-post-101" class="blog-post {% if '101' in favorites %}favorite{% endif %}">
        <span class="favorite-heart">&hearts;</span>
        <h3>Blog Post 101</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed scelerisque nunc malesuada mauris fermentum commodo. Integer non pellentesque augue, vitae pellentesque tortor. Ut gravida ullamcorper dolor, ac fringilla mauris interdum id. Nulla porta egestas nisi, et eleifend nisl tincidunt suscipit. Suspendisse massa ex, fringilla quis orci a, rhoncus porta nulla. Aliquam diam velit, bibendum sit amet suscipit eget, mollis in purus. Sed mattis ultricies scelerisque. Integer ligula magna, feugiat non purus eget, pharetra volutpat orci. Duis gravida neque erat, nec venenatis dui dictum vel. Maecenas molestie tortor nec justo porttitor, in sagittis libero consequat. Maecenas finibus porttitor nisl vitae tincidunt.</p>
        <button class="favorite-button">Favorite</button>
        <button class="unfavorite-button">Unfavorite</button>
      </div>
      <div id="blog-post-102" class="blog-post {% if '102' in favorites %}favorite{% endif %}">
        <span class="favorite-heart">&hearts;</span>
        <h3>Blog Post 102</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed scelerisque nunc malesuada mauris fermentum commodo. Integer non pellentesque augue, vitae pellentesque tortor. Ut gravida ullamcorper dolor, ac fringilla mauris interdum id. Nulla porta egestas nisi, et eleifend nisl tincidunt suscipit. Suspendisse massa ex, fringilla quis orci a, rhoncus porta nulla. Aliquam diam velit, bibendum sit amet suscipit eget, mollis in purus. Sed mattis ultricies scelerisque. Integer ligula magna, feugiat non purus eget, pharetra volutpat orci. Duis gravida neque erat, nec venenatis dui dictum vel. Maecenas molestie tortor nec justo porttitor, in sagittis libero consequat. Maecenas finibus porttitor nisl vitae tincidunt.</p>
        <button class="favorite-button">Favorite</button>
        <button class="unfavorite-button">Unfavorite</button>
      </div>
      <div id="blog-post-103" class="blog-post {% if '103' in favorites %}favorite{% endif %}">
        <span class="favorite-heart">&hearts;</span>
        <h3>Blog Post 103</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed scelerisque nunc malesuada mauris fermentum commodo. Integer non pellentesque augue, vitae pellentesque tortor. Ut gravida ullamcorper dolor, ac fringilla mauris interdum id. Nulla porta egestas nisi, et eleifend nisl tincidunt suscipit. Suspendisse massa ex, fringilla quis orci a, rhoncus porta nulla. Aliquam diam velit, bibendum sit amet suscipit eget, mollis in purus. Sed mattis ultricies scelerisque. Integer ligula magna, feugiat non purus eget, pharetra volutpat orci. Duis gravida neque erat, nec venenatis dui dictum vel. Maecenas molestie tortor nec justo porttitor, in sagittis libero consequat. Maecenas finibus porttitor nisl vitae tincidunt.</p>
        <button class="favorite-button">Favorite</button>
        <button class="unfavorite-button">Unfavorite</button>
      </div>
    </div>

    <script>
      function favorite() {
        var parent = this.parentElement;
        console.log(parent.id)

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/favorite', true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.onreadystatechange = function () {
          if(xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            if(result == 'True') {
              parent.classList.add("favorite");
            }
          }
        };
        xhr.send("id=" + parent.id);
      }

      var buttons = document.getElementsByClassName("favorite-button");
      for(i=0; i < buttons.length; i++) {
        buttons.item(i).addEventListener("click", favorite);
      }

      function unfavorite() {
        var parent = this.parentElement;
        console.log(parent)

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/unfavorite', true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.onreadystatechange = function () {
          if(xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            console.log('Result: ' + result);
            if(result == 'True') {
              parent.classList.remove("favorite");
            }
          }
        };
        xhr.send("id=" + parent.id);
      }

      var buttons = document.getElementsByClassName("unfavorite-button");
      for(i=0; i < buttons.length; i++) {
        buttons.item(i).addEventListener("click", unfavorite);
      }
    </script>

  </body>
</html>

```

Then in the routes.py

```py
from application import app
from flask import render_template, session, request, jsonify

@app.route("/index")
@app.route("/")
def index():

    if not session:
        session['favorites'] = []
        session['unfavorites'] = []
        session.modified = True

    return render_template("index.html", favorites=session['favorites'], unfavorites=session['unfavorites'])


@app.route("/favorite", methods = ['GET', 'POST'])
def favorite():
    print(session)

    if request.method == 'POST':
        id = request.form.get('id')[-3:]
        print(id)

    if id not in session['favorites']:
        session['favorites'].append(id)

        if id in session['unfavorites']:
            session['unfavorites'].remove(id)

        session.modified = True
    print(session)
    return "True"


@app.route("/unfavorite", methods = ['GET', 'POST'])
def unfavorite():
    print(session)

    if request.method == 'POST':
        id = request.form.get('id')[-3:]
    
    if id not in session['unfavorites']:
        session['unfavorites'].append(id)

        if id in session['favorites']:
            session['favorites'].remove(id)

        session.modified = True

    print(session)
    return "True"
```


### Flask Ajax Form

Again copy the template and create the virtual environment.


