import csv
import os
from operator import itemgetter
from flask import Flask, render_template , request , redirect, url_for, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    print(page_name)
    return render_template(f'{page_name}.html')

def showjson(id):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "templates/projects", "myworks.json")
    data = json.load(open(json_url))
    result = filter(lambda work_id: work_id['id'] == id, data)
    return list(result)

@app.route('/projects/<string:page_name>')
def projects_page(page_name):
    query_param =  {k:v for k, v in request.args.items()}
    p_id = query_param['id']
    work = showjson(p_id)
    return render_template(f'projects/{page_name}.html', project=work[0])


def write_to_file(data):
    with open('database.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        name= data['name']
        db.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a' ,newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        name= data['name']
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong! Try Again!'
