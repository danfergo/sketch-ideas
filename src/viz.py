import cv2


class Viz:

    def show(self, frame_name, rgb):
        cv2.imshow(frame_name, rgb[..., ::-1])
        cv2.waitKey(1)


    def stop(self):
        cv2.destroyAllWindows()
