from office.Validator import Validator
from office.office_hardware import Scanner, Printer, Xerox
from office.office_hardware_repo import OfficeHardwareRepo, OfficeHardwareRepoImpl, DeviceNotFoundException


class Company:
    __name: str

    @property
    def name(self):
        return self.__name

    def __init__(self, name: str):
        self.__name = name
        self.__repo: OfficeHardwareRepo = OfficeHardwareRepoImpl()

    def receive_devices(self, devices: list):
        for device in devices:
            self.__repo.add_device(device)

    def lend_devices(self, devices: list):
        for device in devices:
            self.__repo.remove_device(device)

    def __get_devices(self, device_type):
        devices = []
        for device in self.__repo.hardwares:
            if isinstance(device, device_type):
                devices.append(device)
        return devices

    @property
    def scanners(self):
        return self.__get_devices(Scanner)

    @property
    def printers(self):
        return self.__get_devices(Printer)

    @property
    def xeroxes(self):
        return self.__get_devices(Xerox)


company = Company("Company")

devices = []
while True:
    device_type = input("What device do you want to give to the company?\n1 - Printer, 2 - Scanner, "
                        "3 - Xerox\n\"stop\" to stop.\n")
    if device_type == "stop":
        break
    device_type = int(device_type)
    if device_type not in [1, 2, 3]:
        print("Try again.")
        continue
    model = input("Enter device's model: ")
    if not Validator.validate(model):
        print("Company can not afford to receive a no name device.")
        continue
    if device_type == 1:
        devices.append(Printer(model))
    elif device_type == 2:
        devices.append(Scanner(model))
    elif device_type == 3:
        devices.append(Xerox(model))
    print("Device is added to the list.\n")

company.receive_devices(devices)

print("\nAvailable devices:\n")

for scanner in company.scanners:
    print(scanner)

for printer in company.printers:
    print(printer)

for xerox in company.xeroxes:
    print(xerox)

devices = []
while True:
    device_type = input("What device do you want to get from the company?\n1 - Printer, 2 - Scanner, "
                        "3 - Xerox\n\"stop\" to stop.\n")
    if device_type == "stop":
        break
    device_type = int(device_type)
    if device_type not in [1, 2, 3]:
        print("Try again.")
        continue
    model = input("Enter device's model: ")
    if not Validator.validate(model):
        print("Company can not afford to receive a no name device. So it's not retrievable.")
        continue
    if device_type == 1:
        devices.append(Printer(model))
    elif device_type == 2:
        devices.append(Scanner(model))
    elif device_type == 3:
        devices.append(Xerox(model))
    print("Device is added to the list.\n")

try:
    company.lend_devices(devices)
except DeviceNotFoundException as exc:
    print("Your request can not be fulfilled.")
    print(exc)

print("\nAvailable devices:\n")

for scanner in company.scanners:
    print(scanner)

for printer in company.printers:
    print(printer)

for xerox in company.xeroxes:
    print(xerox)
