from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
  <!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
  <body>
   <form  action='/' method="post">
     <label for="rot_box">Rotate by:</label>
     <input id="rot_box" type="text" value="0" name="rotation-amount"/>
     <textarea name="block_text">{0}</textarea>
     <button type="submit">Submit</button>
 
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])

def encrypt():
    rot_amount = int(request.form['rotation-amount'])
    new_text = request.form['block_text']
    #run caesar algo
    b_text= rotate_string(new_text, rot_amount)#the return from caesar
    
    return form.format(b_text)

    

app.run()