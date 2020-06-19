from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from .web_scraper  import get_data
from urllib import parse

app = Flask(__name__)
api = Api(app)


class NCDCScraper(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('state', required=True,
                            help='A valid state name has to be provided')
        args = parser.parse_args()

        results = get_data()[args.state]
        output = {
            "State Affected": results[0],
            "Number of Cases (Lab Confirmed)": results[1],
            "Number of Cases (on admission)": results[2],
            "Number of Discharged Cases": results[3],
            "Number of Deaths": results[4]
        }
        return output

api.add_resource(NCDCScraper, '/ncdc-scraper')

if __name__ == "__main__":
    app.run(debug = True,  port= 5000)

