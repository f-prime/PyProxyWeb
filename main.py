from flask import request, Flask, render_template
import urllib

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
@app.route("/<query>", methods=['GET', 'POST'])
def main(query=None):

    if request.method == "POST":
      try:
        url = request.form['url']
        if not url.startswith("http"):
            url = "http://"+url
        write(url)
        html = urllib.urlopen(url).read()
        site(html)
        return render_template("site.html")
      except Exception, error:
         print error
         pass

    if query:
      try:
        with open("url.txt", 'r') as url:
            query = request.url.split("/")[3]
            source = urllib.urlopen(url.read() +"/"+ query).read()
            site(source)
        return render_template("site.html")
      except Exception, error:
           print error
           pass

def write(url):
   with open("url.txt", 'w') as file:
       file.write(url)

def site(html):
    data = """<center><div style='z-index: 15;
margin:1%;
padding:1%;
background: white;
color: black;
font-family:Arial,Helvetica,sans-serif;
'><h1>PyProxy</h1><form method='post'><input type='text' name='url' placeholder='http://google.com/' style='width:65%; margin:1px;'/><input style='' type='submit' value='Go!'/></form></div><br/> <!-- Begin BidVertiser code -->

<SCRIPT LANGUAGE="JavaScript1.1" SRC="http://bdv.bidvertiser.com/BidVertiser.dbm?pid=407869&bid=1255216" type="text/javascript"></SCRIPT>

<noscript><a href="http://www.bidvertiser.com">pay per click</a></noscript>

<!-- End BidVertiser code --> </center>"""
    with open("templates/site.html", 'w') as site:
        site.write(data+html)
if __name__ == '__main__':
    app.run('0.0.0.0', 81, debug=True)
