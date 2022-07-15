#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from flask import Flask, render_template, request
from car import Car

app = Flask(__name__)
my_car = Car()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/go", methods=("GET", "POST"))
def go():
    if request.method == "POST":
        direction = request.values.get("direction", "reset")
        speed = request.values.get("speed", 0)
        stack = request.values.get("stack", "")
    else:
        direction = request.args.get("direction", "reset")
        speed = request.args.get("speed", 0)
        stack = request.args.get("stack", "")
    print("Stack: { ", stack, " }")
    # control
    my_car.all_suspend()
    try:
        my_car.go[direction](speed)
    except KeyError:
        pass
    return ""


if __name__ == "__main__":
    try:
        server = make_server('0.0.0.0', 8080, app)
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        my_car.cleanup()
