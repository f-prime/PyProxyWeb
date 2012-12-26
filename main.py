from flask import request, Flask, render_template, redirect, url_for
import urllib

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        url = request.form['url']
 
    if url.startswith("http"):
        stuff = urllib.urlopen(url).read()
        with open("templates/site.html", 'w') as file:
            file.write("<h1>PyProxy</h1><div style='position: absolute; '> <form method='post'><input type='text' name='url' placeholder='Website'/><input type='submit' value='Go!'/></form></div><br/><br/><br/><br/>"+stuff)
	    return render_template("site.html")
    else:
        url = "http://"+url
        stuff = urllib.urlopen(url).read()
        with open("templates/site.html", 'w') as file:
            file.write("<h1>PyProxy</h1><div style='position: absolute;'><form method='post'><input type='text' name='url' placeholder='Website'/><input type='submit' value='Go!'/></form></div><br/><br/><br/><br/>"+stuff)
            return render_template("site.html")    
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
