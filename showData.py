# showData.py will show the data in one run folder under the DATA folder
import os
import cv2


def showData(path):
    """
    showData will show the data in one run folder under the DATA folder
    :param path: the path of the data
    :return: None
    """
    for root, dirs, files in os.walk(path):

        for file in files:
            if file.endswith(".png"):
                img = cv2.imread(os.path.join(root, file))
                
                # convert the LIDAR image into a polar map
                polar_img = cv2.linearPolar(img, (img.shape[1]/2, img.shape[0]/2), img.shape[1]/2, cv2.WARP_FILL_OUTLIERS)
                cv2.imshow("polar_img", polar_img)
                cv2.imshow("image", img)
                cv2.waitKey(100)
                # cv2.destroyAllWindows()


if __name__ == '__main__':
    # get current path
    cwd = os.getcwd()
    showData(cwd + "/DATA" + "/2011_09_26_drive_0001_sync") 
    showData(cwd + "/DATA" + "/2011_09_26_drive_0002_sync")