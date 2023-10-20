import numpy
import matplotlib.pyplot


def main() -> None:
    # Определение последовательности значений
    n: int = 8
    x: numpy.array = numpy.linspace(-5, 20, 100)
    y1: numpy.array = 0.3 * n * x + 10 * n
    y2: numpy.array = numpy.cos(0.5 * n * x) + n * numpy.sin(x + n)
    y3: numpy.array = n * numpy.cos(2 * numpy.pi * x) * numpy.exp(-0.1 * n * x)

    # Определение характерных значений зависимостей при помощи методов numpy
    numpy_results: dict[str, dict[str, float]] = {
        "Максимальные значения": {name: numpy.amax(value) for name, value in locals().items() if name[0] == "y"},
        "Минимальные значения": {name: numpy.amin(value) for name, value in locals().items() if name[0] == "y"},
        "Средние значения": {name: numpy.average(value) for name, value in locals().items() if name[0] == "y"},
        "Медианное значения": {name: numpy.median(value) for name, value in locals().items() if name[0] == "y"},
        "Среднеквадратичные значения": {name: numpy.std(value) for name, value in locals().items() if name[0] == "y"}
    }

    # Определение характерных значений зависимостей при стандартных конструкций python3.11
    standard_results: dict[str, dict[str, float]] = {
        "Максимальные значения": {name: max(value) for name, value in locals().items() if name[0] == "y"},
        "Минимальные значения": {name: min(value) for name, value in locals().items() if name[0] == "y"},
        "Средние значения": {name: sum(value) / len(value) for name, value in locals().items() if name[0] == "y"},
        "Медианное значения": {
            name: sorted(value)[len(value) // 2] for name, value in locals().items() if name[0] == "y"
        },
        "Среднеквадратичные значения": {
            name: (sum([(i - (sum(value) / len(value))) ** 2 for i in value]) / len(value)) ** 0.5 for name, value in
            locals().items() if
            name[0] == "y"
        }
    }

    # Вывод характерных значений при помощи f строк
    separator: str = "=" * 50 + "\n"
    print(
        separator + "Numpy:\n" + "\n".join(
            [f"{result}: {value}" for result, value in numpy_results.items()]
        ) + f"\n{separator}" + "Python3:\n" + "\n".join(
            [f"{result}: {value}" for result, value in standard_results.items()]
        ) + f"\n{separator}"
    )

    # Построение графиков полученных последовательностей
    matplotlib.pyplot.plot(x, y1, x, y2, x, y3)
    matplotlib.pyplot.title(f"Графики зависимостей для варианта {n}")
    matplotlib.pyplot.xlabel("x")
    matplotlib.pyplot.ylabel("y")
    matplotlib.pyplot.show()

    # Добавление аддитивного шума к полученным последовательностям
    # y1: numpy.array = 0.3 * n * x * numpy.random.rand() + 10 * n
    # y2: numpy.array = numpy.cos(0.5 * n * x * numpy.random.rand()) + n * numpy.sin(x + n)
    # y3: numpy.array = n * numpy.cos(2 * numpy.pi * x) * numpy.exp(-0.1 * n * x * numpy.random.rand())
    for i in range(len(y1)):
        y1[i] += numpy.random.rand() * 10
        y2[i] += numpy.random.rand() * 10
        y3[i] += numpy.random.rand() * 10

    # Построение графиков обновлённых зависимостей
    matplotlib.pyplot.plot(x, y1, x, y2, x, y3)
    matplotlib.pyplot.title(f"Графики зашумлённых зависимостей для варианта {n}")
    matplotlib.pyplot.xlabel("x")
    matplotlib.pyplot.ylabel("y")
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
