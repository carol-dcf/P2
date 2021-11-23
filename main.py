import cut_video as cv
import yuv_histogram as yh
import resize_video as rv
import change_audio as ca

if __name__ == "__main__":
    # Interactive menu
    ex = 1
    while ( ex != 0 ):
        print("\033[1m\nChoose an exercise:\033[0m")
        print("\t 1. Cut video" + "\n\t 2. YUV histogram" + "\n\t 3. Resize video" + "\n\t 4. Change audio" + "\n\t 0. Exit")

        ex = int(input())

        #### 1 #####
        if (ex == 1):
            print("\033[1mEXERCISE 1\033[0m")
            second_start = int(input("Enter initial second: "))
            N_seconds = int(input("Enter number of seconds: "))
            cv.cut_N_seconds("bbb.mp4", second_start, N_seconds)


        #### 2 #####
        elif (ex == 2):
            print("\n\033[1mEXERCISE 2\033[0m")
            yh.yuv_hist_on_video("cut_bbb.mp4")

        elif (ex == 3):
            #### 3 #####
            print("\n\033[1mEXERCISE 3\033[0m")
            rv.resize_video("cut_bbb.mp4")

        elif (ex == 4):
            #### 4 #####
            print("\n\033[1mEXERCISE 4\033[0m")
            ca.audio2mono("cut_bbb.mp4", "mp3")

        elif (ex == 0):
            print("Application closed.")
        else:
            print("Not a valid option.")