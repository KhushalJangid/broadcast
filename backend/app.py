from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit

app=Flask(__name__,static_url_path='/static')
socketio = SocketIO(app,debug=True,cors_allowed_origins='*',async_mode='eventlet')

@app.route("/")
def lobby():
    return render_template("lobby.html")

@app.route("/join",methods=['POST'])
def lobby():
    roomid = request.form.get('roomId')
    return render_template("lobby.html")

@socketio.on("create-and-join-room")
def join():
    socketio.emit("create-and-join-room")
    return

app.run(debug=True)

