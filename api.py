from flask import Blueprint,render_template,url_for,redirect,jsonify,request

api = Blueprint(__name__,"api")

names = []
amt = 0

@api.route("/")
def home():
    return "Home route"

@api.route("/getDeets",methods=['GET','POST','DELETE','PATCH'])
def getNames():
    global amt
    if request.method == 'POST':
        data = request.get_json()
        for k,v in data["names"].items(): 
            names.append(v)
        return "response : 200"
    
    elif request.method == 'GET':
        return jsonify( {
            "names" : names,
            "amt" : amt
        } );

    elif request.method == 'PATCH':
        data = request.get_json()
        name = data.get("name")
        new_name = data.get("new_name")
        if data.get("new_amt") :
            amt = data.get("new_amt")
        if name in names:
            idx = names.index(name)
            names[idx] = new_name
            return "Updation successful"
        else:
            return "Error 404"
        
    elif request.method == 'DELETE':
        data = request.get_json()
        name = data.get("name")
        if name in names:
            names.remove(name)
            return "Name deleted successfully"
        else:
            return "Name not found , 404"
    

