from Builder.ComputerBuilder import ComputerBuilder


class OfficeComputer:
    @staticmethod
    def construct():
        return ComputerBuilder() \
                .set_cpu('Intel Core i5') \
                .set_gpu('Integrated Intel UHD Graphics') \
                .set_ram('16GB DDR5') \
                .set_storage('512GB SSD') \
                .set_power_supply('500W Bronze') \
                .set_os('Windows 11 Home') \
                .build()
                    