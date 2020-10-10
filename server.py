from flask import Flask, render_template, request, redirect
import csv ,os
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/<page_link>')
def second_page(page_link):
    return render_template(page_link)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_txt(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'

def write_to_txt(data):
    try:
        with open('database1.txt', mode='a') as database1:
            email = data['email']
            subject = data['subject']
            message = data['message']
            database1.write(f'\n{email},{subject},{message}')
    except:
        return'something went wrong'

def write_to_csv(data):
    try :
        with open('database2.csv', mode='a') as database2:
            email = data['email']
            subject = data['subject']
            message = data['message']
            csv_writer = csv.writer(database2, delimiter=",", quotechar='"',quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])
    except:
        return'failed to save in database'
