from flask import Flask
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# 确保上传文件夹存在
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return "Hello, Home Inventory!"

if __name__ == '__main__':
    app.run(debug=True)
