#!/usr/bin/env python3
"""
Camilo Castro | Word game api 
"""
#imports
import json
from flask import Flask
import logging


#define the flask application object from class 'Flask
app = Flask(__name__)
logging.getLogger('werkzeug').disabled = True

#Open dictionary file 
with open('small_project/Week2_version/jsondict.json', 'r') as api_dict:
        jason = json.load(api_dict)

#define app endpoint fullset
@app.route('/full', methods=['GET'])
def full_set():       
    return jason

# entry = input("enter letter")
#define app endpoint fullset
@app.route('/A', methods=['GET'])
def A_set():        
    return jason['A']

#define app endpoint fullset
@app.route('/B', methods=['GET'])
def B_set():        
    return jason['B']

#define app endpoint fullset
@app.route('/C', methods=['GET'])
def C_set():        
    return jason['C']

#define app endpoint fullset
@app.route('/D', methods=['GET'])
def D_set():        
    return jason['D']

#Run-time code
def main():
    """runtime code"""
    app.run(port=2224)
    #print(jason["B"])

#Call main function
if __name__ == "__main__":
    main()
