from flask import Flask, request, jsonify, json
from cassandra.cluster import Cluster
import requests
import sys

#cluster = Cluster(['cassandra'])
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return ('<h1>Hello, {}!</h1>'.format(name))

@app.route('/centres', methods=['GET'])
def get_centres():

    centres=[]
    rows = session.execute("SELECT * FROM enrollmykid.centres LIMIT 10")
    for row in rows:
        centre = {'id': row.id, 'service_approval_number': row.serviceapprovalnumber, 'provider_approval_number': row.providerapprovalnumber, 'service_name': row.servicename, 'provider_legal_name': row.providerlegalname, 'service_address': row.serviceaddress, 'suburb': row.suburb, 'state': row.state, 'postcode': row.postcode, 'phone': row.phone, 'fax': row.fax, 'email_address': row.email, 'conditions_on_approval': row.conditionsonapproval, 'number_of_approved_place': row.numberofapprovedplaces, 'overall_rating': row.overallrating, 'type': row.type}
        
        centres.append(centre)
    return jsonify(centres)

@app.route('/centres/<int:id>', methods=['GET'])
def get_centre_by_id(id):

    centres=[]
    rows = session.execute("""SELECT * FROM enrollmykid.centres WHERE id=%(id)s""",{'id': id})
    for row in rows:

        centre = {'id': row.id, 'service_approval_number': row.serviceapprovalnumber, 'provider_approval_number': row.providerapprovalnumber, 'service_name': row.servicename, 'provider_legal_name': row.providerlegalname, 'service_address': row.serviceaddress, 'suburb': row.suburb, 'state': row.state, 'postcode': row.postcode, 'phone': row.phone, 'fax': row.fax, 'email_address': row.email, 'conditions_on_approval': row.conditionsonapproval, 'number_of_approved_place': row.numberofapprovedplaces, 'overall_rating': row.overallrating, 'type': row.type}
        
        centres.append(centre)

    return jsonify(centres)

@app.route('/centres', methods=['POST'])
def create_centre():

    count_rows = session.execute("SELECT COUNT(*) FROM enrollmykid.centres")

    for c in count_rows:
        last_id = c.count
    last_id += 1

    rows = session.execute("INSERT INTO enrollmykid.centres(id, ServiceApprovalNumber, ProviderApprovalNumber, ServiceName, ProviderLegalName, ServiceAddress, Suburb, State, Postcode, Phone, Fax, Email, ConditionsOnApproval, NumberOfApprovedPlaces, OverallRating, Type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (last_id,request.form['serviceApprovalNumber'], request.form['providerApprovalNumber'], request.form['serviceName'], request.form['providerLegalName'], request.form['serviceAddress'], request.form['suburb'], request.form['state'], int(request.form['postcode']), request.form['phone'], request.form['Fax'], request.form['email'], request.form['conditionsOnApproval'], int(request.form['numberOfApprovedPlaces']), request.form['overallRating'], request.form['type'] ))

    return jsonify({'message':'new record created'})

@app.route('/centres/<int:id>', methods = ['PUT'])
def update_ccentre(id):

    rows = session.execute("""UPDATE enrollmykid.centres SET serviceapprovalnumber=%(serviceapprovalnumber)s, providerapprovalnumber=%(providerapprovalnumber)s, servicename=%(servicename)s, providerlegalname=%(providerlegalname)s, serviceaddress=%(serviceaddress)s, suburb=%(suburb)s, state=%(state)s, postcode=%(postcode)s, phone=%(phone)s, fax=%(fax)s, email=%(email)s, conditionsonapproval=%(conditionsonapproval)s, numberofapprovedplaces=%(numberofapprovedplaces)s, overallrating=%(overallrating)s, type=%(type)s  WHERE id=%(id)s""", { 'serviceapprovalnumber': request.form['serviceApprovalNumber'], 'providerapprovalnumber' : request.form['providerApprovalNumber'], 'servicename': request.form['serviceName'], 'providerlegalname' : request.form['providerLegalName'], 'serviceaddress' : request.form['serviceAddress'], 'suburb' : request.form['suburb'], 'state':request.form['state'], 'postcode' : int(request.form['postcode']), 'phone':request.form['phone'], 'fax' : request.form['Fax'], 'email' : request.form['email'], 'conditionsonapproval':request.form['conditionsOnApproval'], 'numberofapprovedplaces' : int(request.form['numberOfApprovedPlaces']), 'overallrating':request.form['overallRating'], 'type':request.form['type'], 'id':id})

    return jsonify({'message':'updated successfully'})


@app.route('/centres/<int:id>', methods = ['DELETE'])
def delete_centre(id):

    session.execute("""DELETE FROM enrollmykid.centres WHERE id={}""".format(id))
    return jsonify({'message':'delete successfull'})

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080)
