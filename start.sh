#!/bin/sh

# start from remote ssh
export DISPLAY=:0
# stop screen save or blank screen
xdotool keydown Shift_L keyup Shift_L

./gui.py &
