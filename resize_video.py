import os

def resize_video(input_path):
    """
    Resize video into different sizes and qualities
    :param input_path: (str) path of input video file
    :return:
    """
    resize_command = "ffmpeg -i " + input_path + " \
	-s 1280x720 720p_bbb.mp4 \
	-s 640x480 480p_bbb.mp4 \
	-s 360x240 240p_bbb.mp4 \
    -s 160x120 120p_bbb.mp4"
    print(resize_command)
    os.system(resize_command)
    return