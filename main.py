from flask import Flask, request
import subprocess

app = Flask(__name__, static_url_path='/static')

@app.route('/run', methods=['POST'])
def run():
    code = request.get_data().decode('ascii')
    print(code)
    f = open('file.py', 'a')
    f.write(code)
    f.close()
    x = subprocess.run(['python', 'file.py'], stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1]
    print(f'output ==> \n{x}')
    f = open('file.py', 'a')
    f.truncate(0)
    return f'output ==> \n{x}'