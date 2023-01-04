from flask import Flask
app = Flask(_name_)

@app.route('/')
def hellow_world():
return 'Devops Rocks!!!'