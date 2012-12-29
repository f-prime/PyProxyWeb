from flask import request, Flask, render_template
import urllib, threading, time

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
@app.route("/<query>", methods=['GET', 'POST'])
def main(query=None):

    if request.method == "POST":
      try:
        url = request.form['url']
        threading.Thread(target=POSTThread, args=(url,)).start()
        time.sleep(3)
        return render_template("site.html")
      except Exception, error:
         print error
         pass

    if query:
      try:
          threading.Thread(target=POSTQueryThread, args=(query,)).start()  
          time.sleep(3)
          return render_template("site.html")
      except Exception, error:
           print error
           pass
    return render_template("index.html")



def POSTQueryThread(query):
      with open("url.txt", 'r') as url:
          query = request.url.split("/")[3]
          source = urllib.urlopen(url.read() +"/"+ query).read()
          site(source)

def POSTThread(url):
    if not url.startswith("http"):
        url = "http://"+url
    write(url)
    html = urllib.urlopen(url).read()
    site(html)

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
