import csv
import json
from operator import itemgetter
from flask import Flask, render_template , request , redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    print(page_name)
    return render_template(f'{page_name}')

def get_work_data(id):
    with open('templates/projects/myworks.json') as f:
        data = json.load(f)
        result = filter(lambda work_id: work_id['id'] == id, data)
        return list(result)

@app.route('/projects/<string:page_name>')

def projects_page(page_name):
    query_param =  {k:v for k, v in request.args.items()}
    p_id = int(query_param['id'])
    works = [
        {
            "id":"0",
            "title":"E-commerce Project",
            "images":["e-commerce-project-main.JPG"],
            "description": "Lorem Something etc"

        },
        {
            "id":"1",
            "title":"Mini Rakuten TV",
            "images":["mini-rakuten.PNG"],
            "description": "Lorem Something etc"

        },
        {
            "id":"2",
            "title":"Japan Tours",
            "images":["jatours-main.JPG"],
            "description": "Lorem Something etc"

        }
    ]

    return render_template(f'projects/{page_name}', project=works[p_id])


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
