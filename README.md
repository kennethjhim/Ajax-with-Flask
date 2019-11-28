### Flask Ajax Zipcode
Go to https://www.zipcodeapi.com/ and click on free use. It will send the key to your email but you have to activate the email first.

Then to test it locally and resolve CORS issues, follow this link

https://www.zipcodeapi.com/zipblog/docs/2016/04/14/zipcode-testing-locally-and-resolving-cors-issues.html

Copy the flask template. Create virtual env as follows

1. Issue in the terminal
`$ python3 -m venv --without-pip env`

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


