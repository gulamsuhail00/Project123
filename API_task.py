from flask import Flask,request,jsonify

app=Flask(__name__)
available_user=[
    {
        "id":0,
        "user":"Gulam"
    },
    {
        "id":1,
        "user":"John"
    },
    {
        "id":2,
        "user":"Rahul"
    },
    {
        "id":3,
        "user":"Jose"
    },
]

@app.route('/sample.com/api/v1/users', methods=['GET','POST'])
def users():
    if request.method=='GET':
        return jsonify(available_user)
    if request.method=='POST':
        new_user=request.form['user']
        iD=available_user[-1]['id']+1

        new_obj = {
            'id':iD,
            'user':new_user
        }
        available_user.append(new_obj)
        return jsonify(available_user),201

@app.route('/sample.com/api/v1/users/int:<id>', methods=['DELETE'])
def user_delete(id):
    for index,user in enumerate(available_user):
        if user['id'] == id:
            available_user.pop(index)
            return  jsonify(available_user)

if __name__ == '__main__':
    app.run()
