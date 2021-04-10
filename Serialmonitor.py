import serial
from time import sleep

def main():
	si = serial.Serial('COM3',baudrate=9600,timeout=1)
	print("Welcome to the UltimateRoman Serial Monitor...\n")
	while True:
                try:
                        c = si.readline().decode('ascii')
                        if c:
                                print(c)
                        sleep(1)

                except Exception as e:
                        print("Error: ", e)
                        sleep(5)
                        

if __name__ == "__main__":
	main()
