#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from car import Car

ENA = 40
IN1 = 38
IN2 = 36
IN3 = 37
IN4 = 35
ENB = 33

app = Flask(__name__)
mycar = Car(ENA, IN3, IN4, ENB, IN1, IN2, Car.TURN_RATIO_DEFAULT)

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
	mycar.allReset()
	try:
		mycar.go[direction](speed)
	except KeyError:
		pass
	# return
	return ""

if __name__ == "__main__":
	try:
		app.run(host="0.0.0.0", port=80, debug=True)
	except KeyboardInterrupt:
		pass
	finally:
		mycar.cleanup()
