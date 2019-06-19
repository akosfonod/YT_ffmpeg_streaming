#TODO: oled screen: ip address get

import os
import signal
import subprocess

DEBUG = True

intro_proc_cmd      = 'ffmpeg -f -i /home/pi/Videos/intro.mp4 -f mpegts udp://localhost:20001'  #intro input
video0_proc_cmd     = 'ffmpeg -f -i /dev/video/video0 -f mpegts udp://localhost:20002'          #video0 input
video1_proc_cmd     = 'ffmpeg -f -i /dev/video/video1 -f mpegts udp://localhost:20003'          #HDMI input
delivery_proc_cmd   = ''#ffmpeg command to stream from UDP port.

def start_ffmpeg_stream(proc_command):
    if DEBUG:
        print 'Starting ffmpeg process: ' + proc_command
    stream_proc = subprocess.Popen(proc_command, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    return stream_proc

def stop_ffmpeg_stream(stream_proc):
    if DEBUG:
        print 'Stoping ffmpeg process: ' + stream_proc
    os.killpg(os.getpgid(stream_proc),signal.SIGTERM)

def main():
    #main function

#Main entrace for the script
if _name_ == "_main_":
    main()