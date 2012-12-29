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
          query = request.url.split("/")[3]
          threading.Thread(target=POSTQueryThread, args=(query,)).start()  
          time.sleep(3)
          return render_template("site.html")
      except Exception, error:
           print error
           pass
    return render_template("index.html")



def POSTQueryThread(query):
      with open("url.txt", 'r') as url:
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
    data = """<style type='text/css'>top-margin:50%;</style><center style="
position:absolute;
top:0;
left:0;
z-index: 15;
width: 100%;
margin:0;
padding:0;
border:0;
background-color: white;
color: black;s
font-family:Arial,Helvetica,sans-serif;

 "><div name='PyProxy-style'><h1>PyProxy</h1><form method='post'><input type='text' name='url' placeholder='http://google.com/' style='width:65%; margin:1px;'/><input style='' type='submit' value='Go!'/></form></div><br/> <!-- Begin BidVertiser code -->

<SCRIPT LANGUAGE="JavaScript1.1" SRC="http://bdv.bidvertiser.com/BidVertiser.dbm?pid=407869&bid=1255216" type="text/javascript"></SCRIPT>

<noscript><a href="http://www.bidvertiser.com">pay per click</a></noscript>

<!-- End BidVertiser code --><br/><br/> </center><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

"""
    with open("templates/site.html", 'w') as site:
        site.write(data+html)
if __name__ == '__main__':
    app.run('0.0.0.0', 81, debug=True)
