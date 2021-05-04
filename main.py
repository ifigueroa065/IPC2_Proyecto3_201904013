from flask import Flask,request,Response
from flask_cors import CORS

app=Flask(__name__)
#Cualquier IP
cors = CORS(app, resources={r"/*": {"origin": "*"}})


@app.route("/")
def inicio():
    return('<h1>hola mundo</h1>')


@app.route('/events/', methods=['POST'])
def post_events():
    data = open('salida.txt', 'w+')
    data.write(request.data.decode('utf-8'))
    data.close()

    return Response(response=request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')


@app.route('/events/', methods=['GET'])
def get_events():
    data = open('salida.txt', 'r+')
    return Response(response=data.read(),
                    mimetype='text/plain',
                    content_type='text/plain')
if __name__ =='__main__':
    app.run(debug=True,port=5000) 