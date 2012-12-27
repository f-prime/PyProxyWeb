from flask import request, Flask, render_template, redirect, url_for
import urllib

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        url = request.form['url']
 	data = """<center><div style='z-index: 15;
margin:1%;
padding:1%;
background: white;
color: black;
font-family:Arial,Helvetica,sans-serif;


'><h1>PyProxy</h1><form method='post'><input type='text' name='url' placeholder='http://google.com/' style='width:65%; margin:1px;'/><input style='' type='submit' value='Go!'/></form></div></center>"""
        if url.startswith("http"):
            stuff = urllib.urlopen(url).read()
            with open("templates/site.html", 'w') as file:
                file.write(data+stuff)
	        return render_template("site.html")
        else:
            url = "http://"+url
            stuff = urllib.urlopen(url).read()
            with open("templates/site.html", 'w') as file:
                file.write(data+stuff)
                return render_template("site.html")    
    return render_template("index.html")


if __name__ == '__main__':
    app.run('0.0.0.0', 81, debug=True)
