import os
from flask import Flask, request
import werkzeug  

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

def get_fullpath(path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.basename(os.path.normpath(path))
    secure_filename = werkzeug.utils.secure_filename(filename)

    return os.path.normpath(os.path.join(base_dir + '/assets/', secure_filename))

class TaxPayer:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set        
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass
        
        # defends against path traversal attacks
        if path.startswith('/') or path.startswith('..'):
            return None
        
        # builds path
        prof_picture_path = get_fullpath(path)
        try:
            with open(prof_picture_path, 'rb') as pic:
                picture = bytearray(pic.read())
        except FileNotFoundError as err:
            print(err)


        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None
        
        if not path:
            raise Exception("Error: Tax form is required for all users")

        tax_form_path = get_fullpath(path)
        try:
            with open(tax_form_path, 'rb') as form:
                tax_data = bytearray(form.read())
        except FileNotFoundError as err:
            print(err)

        # assume that taxa data is returned on screen after this
        return path