from office.office_hardware import Scanner, Printer, Xerox
from office.office_hardware_repo import OfficeHardwareRepo, OfficeHardwareRepoImpl


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
