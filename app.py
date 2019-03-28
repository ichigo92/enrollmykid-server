from flask import Flask, request, jsonify, json
from cassandra.cluster import Cluster
import requests
import sys

cluster = Cluster(['cassandra'])
session = cluster.connect()

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return ('<h1>Hello, {}!</h1>'.format(name))

@app.route('/centres', methods=['GET'])
def get_centres():

    weather_data=[]
    rows = session.execute("SELECT * FROM enrollmykid.childcares LIMIT 10")
    for row in rows:
        weather = {'id': row.id, 'service_approval_number': row.serviceapprovalnumber, 'provider_approval_number': row.providerapprovalnumber, 'service_name': row.servicename, 'provider_legal_name': row.providerlegalname, 'service_address': row.serviceaddress, 'suburb': row.suburb, 'state': row.state, 'postcode': row.postcode, 'phone': row.phone, 'fax': row.fax, 'email_address': row.emailaddress, 'conditions_on_approval': row.conditionsonapproval, 'number_of_approved_place': row.numberofapprovedplaces, 'overall_rating': row.overallrating, 'type': row.type}
        
        weather_data.append(weather)
    return jsonify(weather_data)

@app.route('/centres/<int:id>', methods=['GET'])
def get_centre_by_id(id):

    weather_data=[]
    rows = session.execute("""SELECT * FROM enrollmykid.childcares WHERE id=%(id)s""",{'id': id})
    for row in rows:

        weather = {'id': row.id, 'service_approval_number': row.serviceapprovalnumber, 'provider_approval_number': row.providerapprovalnumber, 'service_name': row.servicename, 'provider_legal_name': row.providerlegalname, 'service_address': row.serviceaddress, 'suburb': row.suburb, 'state': row.state, 'postcode': row.postcode, 'phone': row.phone, 'fax': row.fax, 'email_address': row.emailaddress, 'conditions_on_approval': row.conditionsonapproval, 'number_of_approved_place': row.numberofapprovedplaces, 'overall_rating': row.overallrating, 'type': row.type}
        
        weather_data.append(weather)

    return jsonify(weather_data)

@app.route('/centres', methods=['POST'])
def create_centre():

    rows = session.execute("INSERT INTO enrollmykid.childcares (id, ServiceApprovalNumber, ProviderApprovalNumber, ServiceName, ProviderLegalName, ServiceAddress, Suburb, State, Postcode, Phone, Fax, EmailAddress, ConditionsOnApproval, NumberOfApprovedPlaces, OverallRating, Type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (7,request.form['ServiceApprovalNumber'], "Vancouver", 14.7, "dark clouds", "02n", ))

    return jsonify({'message':'new record created'})

@app.route('/centres/<int:id>', methods = ['PUT'])
def update_ccentre(id):

    rows = session.execute("""UPDATE enrollmykid.childcares SET EmailAddress=%(emailaddress)s WHERE id=%(id)s""", {'name': request.form['city'], 'id': id})
    print(rows,file=sys.stderr)

    return jsonify({'message':'updated successfully'})


@app.route('/centres/<int:id>', methods = ['DELETE'])
def delete_centre(id):

    session.execute("DELETE FROM enrollmykid.childcares WHERE id=(%s)", (id,))
    return jsonify({'message':'delete successfull'})

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080)
