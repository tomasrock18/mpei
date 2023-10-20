import pandas
import numpy
import cv2


def main() -> None:
    # Читаем ядро свёртки
    core: numpy.ndarray = pandas.read_csv("ядро.csv", header=None).to_numpy()

    # Проверяем корректность ядра
    if core.shape[0] != core.shape[1]:
        raise RuntimeError("Ядро свёртки должно быть квадратной матрицей!")
    elif core.shape[0] % 2 == 0:
        raise RuntimeError("Ядро свёртки должно быть матрицей нечётной размерности!")
    for i in core:
        for j in i:
            if type(j) is not numpy.int64:
                raise ValueError("Ядро свёртки должно содержать только целые числа!")

    # Вычисляем нормировочный коэффициент
    core_sum: int = numpy.sum(core)
    if core_sum == 0:
        d: int = 1
    else:
        d: int = core_sum

    # Считываем изображение, преобразуя его в серое
    default_image: numpy.ndarray = numpy.array(cv2.imread("Исходное изображение.jpeg", cv2.IMREAD_GRAYSCALE))

    # Затемняем границу изображения по ядру свёртки
    for border_level in range(core.shape[0] // 2):
        for i in range(border_level, len(default_image) - border_level):
            default_image[i][border_level] = 0
            default_image[i][-1 - border_level] = 0
        for j in range(border_level, len(default_image[0]) - border_level):
            default_image[border_level][j] = 0
            default_image[-1 - border_level][j] = 0

    # Применяем ядро свёртки ко всем пикселям изображения
    for i in range(core.shape[0] // 2, len(default_image) - core.shape[0] // 2):
        for j in range(core.shape[0] // 2, len(default_image[0]) - core.shape[0] // 2):
            for core_i in range(len(core[0])):
                for core_j in range(len(core[0])):
                    pass

    # Сохраняем обработанное изображение
    cv2.imwrite("Обработанное изображение.jpeg", default_image)


if __name__ == "__main__":
    main()
