import os

from abc import ABCMeta, abstractmethod, abstractproperty
import typing


class ConfigProvider(metaclass=ABCMeta):
    @abstractproperty
    def provider_code(self) -> str:
        pass

    @abstractmethod
    def get_variable(self, name: str) -> typing.Union[typing.Any, None]:
        pass

    @abstractmethod
    def get_variables_list(self) -> typing.List[typing.Any]:
        pass


class SystemProvider(ConfigProvider):
    SYSTEM_PREFIX = "CHARYBDIS"

    @property
    def provider_code(self) -> str:
        return "system"

    def prefixize(self, varname: str) -> str:
        return f"{self.SYSTEM_PREFIX}_{varname.upper()}"

    def get_variable(self, name: str) -> typing.Union[str, None]:
        return os.getenv(self.prefixize(name), None)

    def get_variables_list(self) -> typing.List[str]:
        var_list = []

        for var in os.environ:
            if self.SYSTEM_PREFIX in var:
                var_list.append(var)
            
        return var_list

    
class ConfigProviderManager(object):
    @staticmethod
    def get_by_code(code: str) -> typing.Union[ConfigProvider, None]:
        for provider in ConfigProvider.__subclasses__():
            if provider().provider_code == code:
                return provider()
