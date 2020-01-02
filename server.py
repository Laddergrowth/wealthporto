from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask (__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

    return render_template('index.html', name=username, post_id=post_id)

@app.route('/<string:page_name>')  #this make the code dinamically ao inves the representar todas paginas aqui separadas
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        file = database.write(f'\n{name},{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(database2,delimiter=(','), quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'


