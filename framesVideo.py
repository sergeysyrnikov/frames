from os.path import join
import cv2
import os, glob
import pathlib
import time

path_file_video = 'test.mp4'
path_folder = 'frames'
name_imgs_d = {0: '1.jpeg', 1: '2.jpeg', 2: '3.jpeg'}

class CreateFrames():

    def __init__(self, path_file_video, path_folder, name_imgs):
        self.path_file = path_file_video
        self.path_folder = path_folder
        self.name_dict = name_imgs

    def check_folder(self, path_folder):
        try:
            if not os.path.exists(path_folder):
                os.mkdir(path_folder)
        except Exception as ex:
            print(ex)

    def remove_folder(self, path_folder):
        try:
            cur_path = pathlib.Path(__file__).parent.absolute()
            l_path = glob.glob(join(cur_path, path_folder, '*.jpeg'))
            # print(l_path)
            for el in l_path:
                os.remove(el)
        except Exception as ex:
            print(ex)

    def video_frames(self):
        print('Starting process. Please waiting!')
        cap = cv2.VideoCapture(self.path_file)
        start_time = time.time()
        # print(start_time)
        start_i = 0
        try:
            self.check_folder(self.path_folder)
            self.remove_folder(self.path_folder)
            name_image_start = '0'
            j = 0
            k = 0
            name_image = '0_'
            name_save_img = ''
            while cap.isOpened():
                ret, frame = cap.read()

                fps = int(cap.get(5))
                # print(fps)

                if not ret:
                    break
                else:
                    # cv2.imshow('Video', frame)
                    if (start_i % int(fps/3)) == 0:
                        if (start_i % fps) == 0:
                            if start_i != 0:
                                j += 1
                            k = 0
                            name_image = str(j) + '_'
                            name_save_img = name_image  + self.name_dict[k]
                            cv2.imwrite(join(self.path_folder, name_save_img), frame)
                        else:
                            k += 1
                            name_save_img = name_image  + self.name_dict[k]
                            cv2.imwrite(join(self.path_folder, name_save_img), frame)
                    start_i += 1
                    
                if cv2.waitKey(1) == ord('q'):
                    break
                # cv2.waitKey(int(1000/fps))
            # print(start_i)
            cap.release()
            # cv2.destroyAllWindows()

            delta = (time.time() - start_time)
            print('Time in working: %.4sc.' % delta)
            print('Finished all!')

        except Exception as ex:
            print(ex)


obFrames = CreateFrames(path_file_video=path_file_video, path_folder=path_folder, name_imgs=name_imgs_d)
obFrames.video_frames()




