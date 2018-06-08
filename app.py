from flask import Flask, render_template, request, redirect, url_for

from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

charities = {'Animals': 
                {'American Humane Society': 'americanhumane.org', 
                'Jane Goodall Institute': 'janegoodall.org',
                'Wildlife Conservation Society': 'wcs.org'},
            'Cancer': 
                {'Cancer Research Institute': 'cancerresearch.org',
                'National Breast Cancer Coalition Fund': 'breastcancerdeadline2020.org',
                'Prevent Cancer Foundation': 'preventcancer.org'},
            'Environment': 
                {'Conservation Fund': 'conservationfund.org',
                'Earthworks': 'earthworksaction.org',
                'Environmental Defense Action Fund': 'edfaction.org'},
            'Homelessness': 
                {'Center for Community Change': 'communitychange.org',
                'Homes for Our Troops': 'hfotusa.org',
                'National Alliance to End Homelessness': 'endhomelessness.org'},
            'Women\'s Rights': 
                {'Center for Reproductive Rights': 'reproductiverights.org',
                'Global Fund for Women': 'globalfundforwomen.org',
                'Women for Women International U.S.': 'womenforwomen.org'}
            }

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
        charity_dict = search_charity(interest)
        app.logger.debug('searched interest: ' + interest)
        return render_template('result.html', charity_dict=charity_dict)
    return render_template('search.html', charity_names=list(charities.keys()))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)

