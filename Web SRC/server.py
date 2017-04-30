from flask import Flask, render_template, request
import base64
from PIL import Image
from io import BytesIO
import json
import codecs
from algo import create_model
import numpy as np

app = Flask(__name__)


global model
model = create_model()

def pre_process(img):
	img = Image.open(img)
	img = img.resize((224,224), Image.ANTIALIAS)
	img = np.expand_dims(np.array(img), 0)
	return img

@app.route('/getImage',methods=['GET','POST'])
def get_image():
	if request.method == 'POST':
		i = request.get_json()
		print(i)
		j = i['imageString']
		filename = "static/img.jpg"
		imgdata = base64.b64decode(j)
		with open(filename, 'wb') as f:
			f.write(imgdata)
		homepage()
		return 'OK!'
	return "LOL NO"


@app.route('/')
def homepage():
	name = 'img.jpg'
	image = pre_process('static/'+name)
	plant = ['Healthy Apple', 'Apple infected with Rot', 'Apple infected with Rust', 
					 'Apple infected with Scab']

	pred = model.predict(image)

	d = {}
	for index, value in enumerate(pred[0]):
		d[plant[index]] = value*100

	plant_name = 'Apple'
	treatment = {
		"Apple infected with Scab": "One method of apple scab treatment is to apply a fungicide, such as Myclotect™ 2 – 4 times in the spring as the leaves emerge.\nThe use of a growth hormone regulator such as Cambistat® to minimize the effects of foliar diseases has been proven an effective apple scab treatment.\nCultural practices can be an effective apple scab preventive treatment because they reduce the apple scab disease source.\n",
		"Healthy Apple": "Go Healthy!\n",
		"Apple infected with Rot": "Keep a clean, maintained growing site\nProper sanitation\nFungicide Spray\n",
		"Apple infected with Rust": "Look for for galls and small yellow spots on the leaves, two primary symptoms of cedar-apple disease.\nSever affected branches 2 inches from the gall with bypass pruners or long-reach pruners using a clean straight cut.\nApply contact fungicide to trees in close proximity to the infected cedar according to the manufacturer’s guidelines.\nApply systemic fungicide, which is absorbed through capillary action and travels throughout the tree.\n"
	}

	treatment_technique = treatment[plant[np.argmax(pred)]]

	plant_img = name

	return render_template('index.html', plant_name=plant_name, treatment_technique=treatment_technique,
												 dictionary = d, plant_img=plant_img)

if __name__ == '__main__':
	app.run(host= '0.0.0.0')
	app.run(debug=True)
	app.run(extra_files=['templates/index.html'])
	app.config['TEMPLATES_AUTO_RELOAD'] = True
