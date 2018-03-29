# flask dependencies
from flask import Flask, jsonify, render_template
import os

#  Flask set up
app = Flask(__name__)

# Database set up and connection
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, desc  #what else here???

# #import custom functions
# from bbd import return_sample_names

engine = create_engine("sqlite:///database/homecare.db")

Base = automap_base()
Base.prepare(engine, reflect=True)

#table class name
homecare = Base.classes.homecare
# Samples = Base.classes.samples
# Samples_metadata = Base.classes.samples_metadata

#create session 
session = Session(engine)

@app.route("/")
def home():
    return render_template("index.html")
#serve up data to the clustered marker map
@app.route("/location_data")
def get_homecareDta():
    homecar= session.query(homecare.latitude,homecare.longitude, homecare.name,  homecare.sq).all()
    # care_cluster_lst=[]            
    # for i in care_cluster:
        # provider_dict={k for k in i}
        # care_cluster_lst.append(provider_dict)
    return jsonify(homecar) 
# serve up data to the find provider form
@app.route("/search_data")
def find_provider():
    resultSet= session.query( homecare.cer_no, homecare.name,  homecare.sq, homecare.city, homecare.state).all()
    # care_cluster_lst=[]            
    # for i in care_cluster:
        # provider_dict={k for k in i}
        # care_cluster_lst.append(provider_dict)
    return jsonify(resultSet)

#serve up data to the service type  map
# @app.route("/serviceType") 
# def serviceType():
#     return render_template("service_type_map.html")

@app.route("/serviceType")
def get_ServiceTypeDta():
    offerService= (session.query(homecare.latitude,homecare.longitude, homecare.name,  homecare.sq,
            homecare.ncs,homecare.pts, homecare.sps,  homecare.hhas).all())
    # care_cluster_lst=[]            
    # for i in care_cluster:
        # provider_dict={k for k in i}
        # care_cluster_lst.append(provider_dict)
    return render_template("service_type_map.html", data=offerService)

#run
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port, debug=True)