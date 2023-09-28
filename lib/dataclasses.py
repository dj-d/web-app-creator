from dataclasses import dataclass

@dataclass
class RunConfig:
    url: str
    startup_class: str

@dataclass
class DesktopConfig:
    working_dir: str
    name: str
    startup_class: str
    icon_path: str
    exec_path: str
    path: str = '/usr/bin'
    comment: str = 'WebApp'
    type: str = 'Application'
    categories: str = 'Network;WebBrowser;'

@dataclass
class LinkConfig:
    run_path: str
    desktop_path: str
    startup_class: str
