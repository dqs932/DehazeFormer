from __future__ import absolute_import

import os
import glob
import numpy as np

import cv2

from siamfc import TrackerSiamFC

from siamfc import *


def get_frames(video_name): 

    if video_name.endswith('avi') or \
       video_name.endswith('mp4') or \
       video_name.endswith('mov'):
        
        cap = cv2.VideoCapture(video_name)
        
        for i in range(50):
            cap.read()

        while True:
            ret, frame = cap.read()
            if ret:
                yield frame 
            else:
                break
    else:
        seq_dir = os.path.expanduser(video_name)
        images = sorted(glob.glob(os.path.join(seq_dir, 'img', '*.jpg')))
        
        for img in images:
            frame = cv2.imread(img)
            yield frame

def newtrack(self, img_files, box):
    frame_num = len(img_files)
    boxes = np.zeros((frame_num, 4))
    boxes[0] = box
    toc = 0
    times = np.zeros(frame_num)

    for f, img_file in enumerate(img_files):

        tic = cv2.getTickCount()

        # img = ops.read_image(img_file)

        # begin = time.time()
        if f == 0:
            self.init(img, box)
        else:
            boxes[f, :] = self.update(img)
            toc += cv2.getTickCount() - tic
        # times[f] = time.time() - begin
            
    toc /= cv2.getTickFrequency()

    fps = total_length / toc

    print("fps{}".format(fps))

    return boxes, times




if __name__ == '__main__':
   
    net_path = 'pretrained\\siamfc_alexnet_e50.pth'

    tracker = TrackerSiamFC(net_path=net_path)

    """
        这里传入你需要进行跟踪的视频的路径，我上面定义了自动判断函数，
        无论传入的是后缀名为.mp4或者.avi的视频还是传入视频序列,
        都可以自动判断，进行数据读取。
        若是视频,写入该视频的文件名(加上相对路径),如data\\A.mp4
        若是视频序列,写如该序列的名字,data\\OTB100\\Biker
        (不用加img,路径处理的时候自动添加了)
   
    """
    video_name = 'data\\Running2.mp4'


    first_frame = True
    boxes = []
    toc = 0
    
    for frame in get_frames(video_name):
        tic = cv2.getTickCount()
        if first_frame:
            try:
                init_rect = cv2.selectROI('SiamFC', frame, False, False)
                # init_rect = [262,94,16,26]
            except:
                exit()    

            boxes.append(init_rect)
            tracker.init(frame, init_rect)
            first_frame = False
        
        else:
            box = tracker.update(frame)
            x, y, w, h = [int(i) for i in box]
            boxes.append(box)
            toc += cv2.getTickCount() - tic
            current_len = len(boxes) 
            toc_fre = toc / cv2.getTickFrequency()
            current_speed = current_len / toc_fre 
            current_speed = "{:.2f}".format(current_speed)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Speed: {} fps".format(current_speed), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow('SiamFC', frame)
            cv2.waitKey(30)
        
    total_length = len(boxes)        
    toc /= cv2.getTickFrequency()
    fps = total_length / toc

    print('\n****************************************')
    print('SiamFC_Total_Time: {:02.1f}s Mean_Speed: {:3.1f}fps'.format(toc, fps))
    print('*****************************************\n')

    cv2.destroyAllWindows()