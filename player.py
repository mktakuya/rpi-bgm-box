#!/usr/bin/env python
# coding:utf-8
import subprocess

def play(url):
    download = subprocess.Popen("youtube-dl '{0}' -q -o -".format(url),
            stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    #subprocess.call("mplayer - -novideo", stdin=download.stdout, shell=True)

    mplayer = subprocess.Popen("mplayer - -novideo",
            stdin=download.stdout, shell=True)
    mplayer.wait()

    """
    cmd = "youtube-dl '%s' -r 50K --buffer-size 20M -q -o - | mplayer - -novideo" % (url)
    subprocess.call(cmd, shell=True)
    """

