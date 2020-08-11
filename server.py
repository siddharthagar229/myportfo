from flask import Flask,render_template,url_for,request,redirect
from markupsafe import escape
import csv
app = Flask(__name__)
# print(__name__)


@app.route('/')
def hello_world():
                                                                                            # print(url_for('static', filename='myweb.ico'))             
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/submit_form', methods=['POST', 'GET'])
#  def submit_form():
#     return 'feteg fgfgrhth'


def write_to_file(data):
    with open('database.txt',mode='a') as db:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as db2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if  request.method=='POST':
        try:
            data=request.form.to_dict()
            # print(data)
            write_to_csv(data)
            # return 'form submitted'
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong try again'


     

