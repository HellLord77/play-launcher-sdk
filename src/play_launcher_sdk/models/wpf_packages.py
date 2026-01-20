from .base import Base
from .wpf_package import WpfPackage


class WpfPackages(Base):
    wpf_packages: list[WpfPackage]
