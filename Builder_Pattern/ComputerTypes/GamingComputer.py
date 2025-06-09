from Builder.ComputerBuilder import ComputerBuilder


class GamingComputer:
    @staticmethod
    def construct():
        return ComputerBuilder() \
                .set_cpu('Intel Core i9') \
                .set_gpu('NVIDIA RTX 4090') \
                .set_ram('32GB DDR5') \
                .set_storage('2TB NVMe SSD') \
                .set_power_supply('850W Gold') \
                .set_os('Windows 11 pro') \
                .build()
                    