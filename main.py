from flask import request, Flask, render_template, redirect, url_for
import urllib

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
@app.route("/<query>", methods=['GET', 'POST'])
def main(query=None, url=None):
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

    if request.method == "POST":
        url = request.form['url']
	f = open("url.txt",'w') 
	f.write(url)
	f.close()
        if not url.startswith("http"):
	    url = "http://"+url 

        stuff = urllib.urlopen(url).read()
        with open("templates/site.html", 'w') as file:
            file.write(data+stuff)
	    return render_template("site.html")   
    if query:
	f = open('url.txt', 'r')
	stuff = f.read()
	if not stuff.startswith("http"): stuff = "http://"+stuff
	stuff = urllib.urlopen(stuff+"/"+query).read()
        f.close()
        with open("templates/site.html", 'w') as file:
            file.write(data+stuff)
            return render_template("site.html")
       
    return render_template("index.html")


if __name__ == '__main__':
    app.run('0.0.0.0', 81, debug=True)
