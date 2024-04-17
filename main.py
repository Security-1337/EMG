import wave
import sys
import argparse
import struct

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str)

args = parser.parse_args()

try:
    data = wave.open(args.file,  mode="r")
    frames_count = data.getnframes()
    frame_rate = data.getframerate()
    read_data = data.readframes(frames_count)
    new_data = struct.unpack("<" + str(frames_count) + "h", read_data)
    datap = list(new_data)

    def ActAverage():
        sum_of_list = 0
        index = 0
        while index != frames_count:
            sum_of_list = sum_of_list + datap[index]
            index = index + 1
        average = sum_of_list/frames_count
        return average
    def ActMax():
        max_value = max(datap)
        return max_value
    def ActLength():
        l = frames_count/frame_rate
        return l
    def ActEnergy():
        energy = ActAverage() * ActLength()
        return energy

    print ("Среднее значение сигнала подхода:\n", ActAverage(),
        "\nПиковое значение сигнала подхода:\n", ActMax(),
        "\nЭнергия активности подхода:\n", ActEnergy(),
        "\nПродолжительность активности:\n", ActLength())
except Exception as e:
    print (e)