# flask dependencies
from flask import Flask, jsonify, render_template

#  Flask set up
app = Flask(__name__)

# # Database set up and connection
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, desc  #what else here???

# # #import custom functions
# # from bbd import return_sample_names

# engine = create_engine("sqlite:///homecare.db")

# Base = automap_base()
# Base.prepare(engine, reflect=True)

# homecare = Base.classes.homecare
# # Samples = Base.classes.samples
# # Samples_metadata = Base.classes.samples_metadata

# #create session 
# session = Session(engine)

@app.route("/")
def home():
    return render_template("care_provider_Dashboard.html")

# @app.route("/providers")
# def names():
#     care_cluster= session.query(homecare.cer_no, homecare.name, homecare.address, homecare.city,homecare.zipcode_x,
#                             homecare.latitude,homecare.longitude,homecare.ownership, 
#                             homecare.sq, homecare.Population).all()
#     care_cluster_lst=[]            
#     for i in care_cluster:
#         provider_dict={k for k in i}
#         care_cluster_lst.append(provider_dict)
#     return jsonify(care_cluster_lst)


# @app.route("/otu")
# def otu():
#     otu_descriptions = session.query(Otu.lowest_taxonomic_unit_found).all()
#     otu_descriptions_list = [x for (x), in otu_descriptions]
#     return jsonify(otu_descriptions_list)

# @app.route("/otu_descriptions")
# def otu_disc():
#     otu_descriptions = session.query(Otu.otu_id, Otu.lowest_taxonomic_unit_found).all()
#     # otu_dict = {}
#     # for row in otu_descriptions:
#     #     otu_dict[row[0]] = row[1]
#     otu_dict={k:v for k,sample_values in otu_descriptions  }
#     return jsonify(otu_dict)

# @app.route("/metadata/<sample>")
# def sample_query(sample):
#     sample_name = sample.replace("BB_", "")
#     result = session.query(Samples_metadata.AGE, Samples_metadata.BBTYPE, Samples_metadata.ETHNICITY, Samples_metadata.GENDER, Samples_metadata.LOCATION, Samples_metadata.SAMPLEID).filter_by(SAMPLEID = sample_name).all()
#     record = result[0]
#     record_dict = {
#         "AGE": record[0],
#         "BBTYPE": record[1],
#         "ETHNICITY": record[2],
#         "GENDER": record[3],
#         "LOCATION": record[4],
#         "SAMPLEID": record[5]
#     }
#     return jsonify(record_dict)

# @app.route('/wfreq/<sample>')
# def wash_freq(sample):
#     sample_name = sample.replace("BB_", "")
#     result = session.query(Samples_metadata.WFREQ).filter_by(SAMPLEID = sample_name).all()
#     wash_freq = result[0][0]
#     return jsonify(wash_freq)

# @app.route('/samples/<sample>')
# def otu_data(sample):
#     sample_query = "Samples." + sample
#     result = session.query(Samples.otu_id, sample_query).order_by(desc(sample_query)).all()
#     otu_ids = [result[x][0] for x in range(len(result))]   
#     sample_values = [result[x][1] for x in range(len(result))]
#     dict_list = [{"otu_ids": otu_ids}, {"sample_values": sample_values}]
#     return jsonify(dict_list)

if __name__ == '__main__':
    app.run(debug=True)