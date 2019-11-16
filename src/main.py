""" MAIN """
from controller import app


if __name__ == "__main__":
    app.run(debug=True, host=app._game.getIp(), port=app._game.getPort())
