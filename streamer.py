#TODO: oled screen: ip address get ✔
#TODO: control gopro H7 black and get the stream: https://github.com/KonradIT/goprowifihack/tree/master/HERO7
#TODO: control xiaomi yi and get the stream:      https://github.com/deltaflyer4747/Xiaomi_Yi

import os
import signal
import subprocess

DEBUG = True

video_intro     = #path to intro video which begins the stream, you should have this file available locally
video_device0   = #path of video device0
video_device1   = #path of video device1

intro_proc_cmd      = 'ffmpeg -c:v h264_mmal -i "' + video_intro   +'" -c:a aac -c:v h264_omx -b:v 2000k -maxrate 2500k -f mpegts udp://localhost:20001'    #intro input
video0_proc_cmd     = 'ffmpeg -c:v h264_mmal -i "' + video_device0 +'" -c:a aac -c:v h264_omx -b:v 2000k -maxrate 2500k -f mpegts udp://localhost:20002'    #video0 input
video1_proc_cmd     = 'ffmpeg -c:v h264_mmal -i "' + video_device1 +'" -c:a aac -c:v h264_omx -b:v 2000k -maxrate 2500k -f mpegts udp://localhost:20002'    #HDMI input
delivery_proc_cmd   = 'ffmpeg '#ffmpeg command to stream from UDP port.

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