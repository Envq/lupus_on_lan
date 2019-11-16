"""Implementation of the controller of the game"""
from model import Game
from roles import MASTER, COLORS

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
        user = request.form["userId"]

        if user == MASTER:
            app._game.addMaster()
            return render_template("loading.html", userId=user)

        if user and not app._game.thereIs(user) and not app._game.gameFull():
            app._game.addPlayer(request.form["userId"])
            return render_template("loading.html", userId=user)

    return render_template("home.html")


@app.route("/lobby", methods=["POST"])
def lobby():
    """Loading player"""
    if request.method == "POST":
        user = request.form["userId"]

        if not app._game.gameFull() or not app._game.isMaster():
            return render_template("loading.html", userId=user, players=app._game.getPlayers())

        else:
            app._game.initRoles()
            if user == MASTER:
                return render_template("master.html", players=app._game.getPlayers(),
                                       colors=COLORS)

            else:
                role = app._game.getPlayers()[user]
                description = app._game.getDescriptionOf(role)
                return render_template("player.html", userId=user, role=role, description=description)


# MAIN
if __name__ == "__main__":
    app.run(debug=True)
    # http://localhost:5000/
