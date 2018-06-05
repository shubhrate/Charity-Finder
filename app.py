from flask import Flask, render_template, request, redirect, url_for

from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

charities = {'Animals': ['American Humane Society','Jane Goodall Institute','Wildlife Conservation Society'],
            'Cancer': ['Cancer Research Institute','National Breast Cancer Coalition Fund','Prevent Cancer Foundation'],
            'Environment': ['Conservation Fund','Earthworks','Environmental Defense Action Fund'],
            'Homelessness': ['Center for Community Change','Homes for Our Troops','National Alliance to End Homelessness'],
            'Women\'s Rights': ['Center for Reproductive Rights','Global Fund for Women','Women for Women International U.S.']}

def search_charity(interest):
    if interest in charities.keys():
        return charities[interest]
    else:
        return ["Sorry, we do not have data for " + interest]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        interest = request.form['interest']
        charity_list = search_charity(interest)
        app.logger.debug('searched interest: ' + interest)
        return render_template('result.html', cl=charity_list)
    return render_template('search.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)

