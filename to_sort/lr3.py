import cv2
import numpy


def main() -> None:
    # Reading images
    im_default: cv2.typing.MatLike = cv2.imread("Исходное.BMP", cv2.IMREAD_GRAYSCALE)
    im_160: cv2.typing.MatLike = cv2.imread("160.BMP", cv2.IMREAD_GRAYSCALE)

    # Defining arrays to compare
    arr_zero = numpy.zeros((len(im_default), len(im_default[0])))
    arr_160 = numpy.zeros((len(im_default), len(im_default[0])))

    # Updating comparing array
    for i in range(len(arr_160)):
        for j in range(len(arr_160[0])):
            new_value = im_default[i][j] + 160
            if new_value > 255:
                arr_160[i][j] = 255
            else:
                arr_160[i][j] = new_value

    print(numpy.array_equal(arr_zero, arr_160 - im_160))


if __name__ == "__main__":
    main()
