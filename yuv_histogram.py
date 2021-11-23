import os

def yuv_hist_on_video(input_path):
    """
    Overlay YUV histogram on top of video
    :param input_path: (str) path of the video file
    :return:
    """
    output_path = "yuv_" + input_path
    hist_command = "ffmpeg -i " + input_path + " -vf \"split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay\" -c:a copy " + output_path
    print(hist_command)
    os.system(hist_command)
    return