#!/usr/bin/python3
from flask import Flask, request
from flask.templating import render_template
import time

from model import Game


# INITIALIZATION FLASK
app = Flask("Lupus on LAN",
            static_folder='images')


# INITIALIZATION CONTROLLER
app.game = Game()


# CUSTOM FUNCTIONS
def goToLobby(userID):
    return render_template("lobby.html",
                            userName = app.game.getNameOf(userID),
                            players  = app.game.getPlayersName())


# FLASK FUNCTIONS
@app.route("/")
def home():
    userIP = request.remote_addr
    if app.game.isAlreadyLogged(userIP):
        return goToLobby(userIP)
    # go to register page
    return render_template("register.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    userIP = request.remote_addr
    if app.game.isAlreadyLogged(userIP):
        return goToLobby(userIP)
    # Check if there is a message
    if request.method == 'POST':
        userName = request.form["userName"]
        if app.game.addPlayer(userIP, userName):
            return goToLobby(userIP)
    return render_template("register.html")


@app.route("/lobby", methods=['GET', 'POST'])
def lobby():
    userIP = request.remote_addr
    if not app.game.isAlreadyLogged(userIP):
        return render_template("register.html")
    # Check if start
    if app.game.isStart():
        name = app.game.getNameOf(userIP)
        if name == 'master':
            return render_template("master.html",
                                    players=app.game.getPlayers())
        else:
            userRole = app.game.getRoleOf(userIP)
            return render_template("player.html",
                                    userName       = name,
                                    role           = userRole,
                                    team           = app.game.getTeamOf(userRole),
                                    description    = app.game.getPlayerDescriptionOf(userRole),
                                    imagePath      = app.game.getImagePathOf(userRole),
                                    playersSimilar = app.game.getPlayersSimilarTo(userIP))
    return goToLobby(userIP)
