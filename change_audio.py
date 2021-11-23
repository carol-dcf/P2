import os

def audio2mono(input_path, new_audio_codec):
    """
    Convert audio of a video into mono and change the type of audio codec it uses
    :param input_path: (str) path of the video file
    :param new_audio_codec: (str) type of new audio code (e.g. mp3, aac...)
    :return:
    """
    output_path = "mono_" + str(new_audio_codec) + "_" + input_path
    audio_command = "ffmpeg -i " + input_path + " -acodec " + new_audio_codec + " -ac 1 " + output_path
    print(audio_command)
    os.system(audio_command)
    return