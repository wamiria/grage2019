import serial
import argparse

def pitching(bluetooth_serial):
    send_char = 'a'
    bluetooth_serial.write(send_char)
    print "pitching"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--serial_device')
    args = parser.parse_args()

    ser = serial.Serial(args.serial_device, 9600)

    pitching(ser)

    ser.close()
