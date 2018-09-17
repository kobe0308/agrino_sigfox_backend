from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'Hello World!'

    
class SensorDataAPI(Resource):
    def get(self):
        pass

    def put(self):

        print("hi mom, I'm here")
        print(request.form['data'])
        print(request.form['ts'])
        return {'hihi':'qq'}
    
class ImageDataAPI(Resource):
    def get(self):
        pass

    def put(self):
        pass

api.add_resource(SensorDataAPI, '/v1.0/sensordata')
api.add_resource(ImageDataAPI,'/v1.0/imagedata')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1984, debug=True)



