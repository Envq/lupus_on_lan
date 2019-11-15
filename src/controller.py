"""Implementation of the controller of the game"""
from model import Game

from flask import Flask, request
from flask.templating import render_template



# INITIALIZATION FLASK
app = Flask("virtual-lupus Game")

# INITIALIZATION CONTROLLER
app._game = Game()
app._names = list()


# FUNCTIONS
@app.route("/")
def home():
    """Home page"""

    return render_template("home.html")


@app.route("/register", methods=["POST"])
def register():
    """Register player"""
    if request.method == "POST":
        name = request.form["name"]

        if name and not app._game.thereIs(name):    
            app._game.addPlayer(request.form["name"])

            return render_template("loading.html")

    return render_template("home.html")


@app.route("/lobby", methods=["POST"])
def lobby():
    """Loading player"""

    if not app._game.gameFull():
        return render_template("loading.html", players=app._names)
    
    else: 
        pass
        # TODO: case master, player1, ...
        # return render_template("master.html")
        # return render_template("player.html")


@app.route("/player", methods=["POST"])
def player():
    """Player page"""
    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"]

        return render_template("player.html", name = name, role = role)


@app.route("/master", methods=["POST"])
def master():
    """Master page"""

    return render_template("player.html", players = app._game.getPlayers())



# MAIN
if __name__ == "__main__":
    app.run(debug=True, host="192.168.1.110")
    # http://localhost:5000/