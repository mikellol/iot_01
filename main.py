"""
@author M.Velarde
@since 2022-5-10
@descrip.Ejercicio de Flask
"""
#unclusion del modulo 
from flask import Flask
app = Flask ('__main__')
@app.route('/test', methods=['GET'])
def go_home ():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')