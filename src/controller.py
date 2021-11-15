#!/usr/bin/env python3
import flask
from model import Game

from flask import Flask, request
from flask.templating import render_template


# INITIALIZATION FLASK
app = Flask("virtual-lupus Game",
            static_folder='images')


# INITIALIZATION CONTROLLER
app.game = Game()


# FLASK FUNCTIONS
@app.route("/")
def home():
    """Home page"""
    return render_template("home.html")


@app.route("/register", methods=["POST"])
def register():
    """Register player"""
    if request.method == "POST":
        user = request.form["userId"]
        if app.game.addPlayer(user):
            return render_template("loading.html",
                                   userId=user)
    return render_template("home.html")


@app.route("/lobby", methods=["POST"])
def lobby():
    """Loading player"""
    if request.method == "POST":
        user = request.form["userId"]
        if not app.game.isStart():
            return render_template("loading.html",
                                   userId  = user,
                                   players = app.game.getPlayersName())
        else:
            userRole = app.game.getRoleOf(user)
            return render_template("player.html",
                                    userId         = user,
                                    role           = userRole,
                                    faction        = app.game.getFactionOf(userRole),
                                    description    = app.game.getDescriptionOf(userRole),
                                    imagePath      = app.game.getImagePathOf(userRole),
                                    playersSimilar = app.game.getPlayersSimilarTo(user))


@app.route("/test")
def prova():
    userRole = 'lupo'
    return render_template("player.html",
                            userId         = 'Ezio',
                            role           = userRole,
                            faction        = app.game.getFactionOf(userRole),
                            description    = app.game.getDescriptionOf(userRole),
                            imagePath      = app.game.getImagePathOf(userRole),
                            playersSimilar = [])