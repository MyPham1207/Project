from flask import Flask, request, render_template
from PIL import Image
from featureExtractor import FeatureExtractor
from datetime import datetime
from pathlib import Path
import numpy as np
import pickle

app = Flask(__name__)

# Read img feature
fe = FeatureExtractor()
featuresVec = []
img_paths = []

fv = open('F:/Information Retrieval/Project/Code/featureVector/Feature_Vector.py', 'rb')
featuresVec = pickle.load(fv)
featuresVec = np.array(featuresVec)
fv.close()

@app.route("/", methods=["GET", "POST"])
def page():
    #if request.method == "POST":
        #file = request.files["query_img"]

    #     img = Image.open(file.stream)
    #     uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
    #     img.save(uploaded_img_path)

    #     query = fe.extract(img)
    #     dists = np.linalg.norm(feature - query, axis=1)
    #     ids = np.argsort(dists)[:30]
    #     scores = [(dists[id], img_paths[id]) for id in ids]

    #     print(scores)

    #     return render_template("page.html", query_path=uploaded_img_path, scores=scores)
    return render_template("page.html")
    # else:
    #     return render_template("page.html")
    
    
app.run()