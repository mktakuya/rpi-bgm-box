#!/usr/bin/env python
# coding:utf-8
import subprocess
from multiprocessing import Process
from rq import use_connection, Queue
from flask import Flask, render_template, request, redirect
import player


use_connection()
app = Flask(__name__)
queue = Queue()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    url = request.form['youtube-url']
    queue.enqueue_call(func=player.play, args=(url,))
    return redirect('/')


if __name__ == '__main__':
    app.run()

