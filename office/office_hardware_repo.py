from abc import ABC, abstractmethod

from office.office_hardware import OfficeHardware


class DeviceNotFoundException(Exception):
    def __init__(self, device: OfficeHardware):
        self.device = device

    def __str__(self):
        return f"Device not found:\n{self.device}"


class OfficeHardwareRepo(ABC):
    @property
    @abstractmethod
    def hardwares(self) -> list:
        pass

    @abstractmethod
    def add_device(self, device: OfficeHardware):
        pass

    @abstractmethod
    def remove_device(self, device: OfficeHardware):
        pass


class OfficeHardwareRepoImpl(OfficeHardwareRepo):
    __hardwares = []

    @property
    def hardwares(self):
        return self.__hardwares

    def add_device(self, device: OfficeHardware):
        self.hardwares.append(device)

    def remove_device(self, device: OfficeHardware):
        if device in self.hardwares:
            self.hardwares.remove(device)
        else:
            raise DeviceNotFoundException(device)

