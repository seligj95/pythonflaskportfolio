import csv
import os
from operator import itemgetter
from flask import Flask, render_template , request , redirect, url_for, json
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/playground')
def playground_page():
    return render_template(f'/playground/index.html')

@app.route('/cocktail-shacker')
def cocktail_page():
    return render_template(f'/playground/bootcamp/cocktail-shacker/index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    try:
        if '.html' in page_name:
            return render_template(page_name)
        elif '.xml' in page_name:
            return render_template('sitemap.xml')
        return render_template(f'{page_name}.html')
    except TemplateNotFound:
        return render_template('404.html')
        

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


def get_json(path, filename):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, path, filename)
    data = json.load(open(json_url))
    return data
    

def get_project_by_id(id, category, data):
    result = []
    for key in data[category]:
        for rowKey in data[category][key]:
            if rowKey['id'] == id:
                result.append(rowKey)
    
    return result

@app.route('/projects/<string:page_name>')
def projects_page(page_name):
    query_param =  {k:v for k, v in request.args.items()}
    p_id = query_param['id']
    category = query_param['category']
    path =  "templates/projects"
    filename = "myworks.json"
    data = get_json(path, filename)
    projectLenght = 0

    for key in data[category]:
        projectLenght += len(data[category][key])


    work = get_project_by_id(p_id, category, data)
    if '.html' in page_name:
        return render_template(
            f'projects/{page_name}', 
            project=work[0], 
            category=category, 
            projectLenght= projectLenght
        )

    return render_template(
        f'projects/{page_name}.html', 
        project=work[0], 
        category=category, 
        projectLenght= projectLenght
        )


@app.route('/works')
def works_page():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "templates/projects", "myworks.json")
    data = json.load(open(json_url))
    return render_template('works.html', projects=data)


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
