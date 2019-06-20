
#! /bin/bash
#
# Diffusion youtube avec ffmpeg

# Configurer youtube avec une résolution 720p. La vidéo n'est pas scalée.

VBR="2500k"                                    # Bitrate de la vidéo en sortie
FPS="30"                                       # FPS de la vidéo en sortie
QUAL="30"                                      # Preset de qualité FFMPEG
YOUTUBE_URL="rtmp://a.rtmp.youtube.com/live2"  # URL de base RTMP youtube

SOURCE="/dev/video0"                 # Source UDP (voir les annonces SAP)
KEY="yourYTkey"                      # Clé à récupérer sur l'event youtube

#ffmpeg -re -i "$SOURCE" -c copy -f flv "$YOUTUBE_URL/$KEY"

#ffmpeg -y -re -f video4linux2 -standard NTSC -s 720x480 -i /dev/video0 -c:v h264_omx -an -f flv "$YOUTUBE_URL/$KEY"

#Set anaolg input device to composite video: 	v4l2-ctl -d /dev/video0 -i 0
#response for that: 				Video input set to 0 (Composite: Camera, ok)
#check available video devices:			v4l2-ctl --list-devices
#print temperature:				/opt/vc/bin/vcgencmd measure_temp

#ffmpeg -f v4l2 -standard NTSC -thread_queue_size 512 -i /dev/video0 \
#       -f alsa -thread_queue_size 512 -i hw:1,0 \
#       -vcodec libx264 -preset superfast -crf 25 -s 640x480 -r 25 -aspect 16:9 \
#       -acodec libmp3lame -channels 2 -ar 44100 \
#       -f flv "$YOUTUBE_URL/$KEY"

#ffmpeg -f v4l2 -standard NTSC  -i /dev/video0 -fflags nobuffer \
#       -f alsa -thread_queue_size 512 -i hw:0,0 -vcodec h264 -acodec aac -ac 1 -ar 8000 \
#       -ab 32k -map 0:0 -map 1:0 -strict experimental -f flv "$YOUTUBE_URL/$KEY" 

#ffmpeg -f v4l2 -standard NTSC  -i /dev/video0 \
#       -f alsa -thread_queue_size 512 -i hw:0,0 -acodec aac -ac 1 -ar 16000 \
#       -ab 32k -map 0:0 -map 1:0 -strict experimental -vcodec h264 -preset ultrafast \
#       -f flv "$YOUTUBE_URL/$KEY"

#ffmpeg -f v4l2 -standard NTSC  -i /dev/video0 \
#       -f alsa -thread_queue_size 512 -i hw:0,0 \
#       -acodec aac -ac 1 -ar 16000 \
#       -vcodec libx264 -preset ultrafast -crf 30 -r 30 -b:v 2000k -maxrate 2500k \
#       stream_test_dual_output.mp4 | -f flv "$YOUTUBE_URL/$KEY" 
       
ffmpeg -c:v h264_mmal -i Xiaomi-FIMI-A3_SD.mp4\
       -c:a aac \
       -c:v h264_omx -b:v 2000k -maxrate 2500k \
       -f flv -r "$FPS" "$YOUTUBE_URL/$KEY"