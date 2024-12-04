import configparser

class ConfigProvider:
    _config = configparser.ConfigParser()
    _config.read("./config_automation.ini")

    _core_host: str = _config["CONFIG AUTOMATION"]["CORE_HOST"]
    _core_port: str = _config["CONFIG AUTOMATION"]["CORE_PORT"]
    _core_database: str = _config["CONFIG AUTOMATION"]["CORE_DATABASE"]
    _core_user: str = _config["CONFIG AUTOMATION"]["CORE_USER"]
    _core_password: str = _config["CONFIG AUTOMATION"]["CORE_PASSWORD"]
    _landing_zone_host: str = _config["CONFIG AUTOMATION"]["LANDING_ZONE_HOST"]
    _landing_zone_port: str = _config["CONFIG AUTOMATION"]["LANDING_ZONE_PORT"]
    _landing_zone_database: str = _config["CONFIG AUTOMATION"]["LANDING_ZONE_DATABASE"]
    _landing_zone_user: str = _config["CONFIG AUTOMATION"]["LANDING_ZONE_USER"]
    _landing_zone_password: str = _config["CONFIG AUTOMATION"]["LANDING_ZONE_PASSWORD"]

    @classmethod
    def print_config(cls):
        print("CORE_HOST: " + str(cls.get_core_host()))
        print("CORE_PORT: " + str(cls.get_core_port()))
        print("CORE_DATABASE: " + str(cls.get_core_database()))
        print("CORE_USER: " + str(cls.get_core_user()))
        print("CORE_PASSWORD: " + str(cls.get_core_password()))
        print("LANDING_ZONE_HOST: " + str(cls.get_landing_zone_host()))
        print("LANDING_ZONE_PORT: " + str(cls.get_landing_zone_port()))
        print("LANDING_ZONE_DATABASE: " + str(cls.get_landing_zone_database()))
        print("LANDING_ZONE_USER: " + str(cls.get_landing_zone_user()))
        print("LANDING_ZONE_PASSWORD: " + str(cls.get_landing_zone_password()))

    @classmethod
    def get_core_host(cls) -> str:
        return str(cls._core_host)

    @classmethod
    def get_core_port(cls) -> str:
        return str(cls._core_port)

    @classmethod
    def get_core_database(cls) -> str:
        return str(cls._core_database)

    @classmethod
    def get_core_user(cls) -> str:
        return str(cls._core_user)

    @classmethod
    def get_core_password(cls) -> str:
        return str(cls._core_password)

    @classmethod
    def get_landing_zone_host(cls) -> str:
        return str(cls._landing_zone_host)

    @classmethod
    def get_landing_zone_port(cls) -> str:
        return str(cls._landing_zone_port)

    @classmethod
    def get_landing_zone_database(cls) -> str:
        return str(cls._landing_zone_database)

    @classmethod
    def get_landing_zone_user(cls) -> str:
        return str(cls._landing_zone_user)

    @classmethod
    def get_landing_zone_password(cls) -> str:
        return str(cls._landing_zone_password)