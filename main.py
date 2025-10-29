from flask import Flask, render_template, request,redirect
import uuid
from database_manager import add_entry, get_data

app = Flask(__name__)

def generate_uid():
    new_uuid = uuid.uuid4()
    final_id = str(new_uuid)[0:4]
    return final_id

@app.route('/',methods=['GET','POST'])

def home():
     return render_template('home.html')

@app.route('/create',methods=['GET','POST'])

def create():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        syntax = request.form.get('syntax')
        expiration = request.form.get('expiration')
        is_password_protected = request.form.get('is_password_protected')
        password = request.form.get('password')
        burn_after_read = request.form.get('burn_after_read')
        
        uid = generate_uid()
        
        print(title, content, syntax, expiration, is_password_protected, password, burn_after_read, uid)

        add_entry(uid, title, content, syntax, expiration, is_password_protected, password, burn_after_read)

        return redirect(f'/{uid}')

    else:
        return render_template('create.html')

@app.route('/<uid>')
def view_paste(uid):
    paste_data = get_data(uid)

    if len(paste_data) != 0:
        paste_id, title, content, expiry, is_password, password, language, is_one_view = paste_data[0]

        if paste_id:
            return render_template("view_paste.html", paste_id=uid, title=title, content=content)
        
        else:
            return "Paste Not Found"

@app.route('/about',methods=['GET','POST'])

def about():
    return render_template('about.html')


app.run(debug=True)