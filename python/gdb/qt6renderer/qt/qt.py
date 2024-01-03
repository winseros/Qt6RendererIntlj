from gdb import parse_and_eval, lookup_symbol, Value
from enum import IntEnum
from typing import Union


class QtVersion(IntEnum):
    V6_0_0 = 0x060000
    V6_3_0 = 0x060300


class QtTiVersion(IntEnum):
    V22 = 22


class Qt:
    def __init__(self):
        self.fallbackQtVersion = 0x60200

    def namespace(self) -> str:
        # This function is replaced by handleQtCoreLoaded()
        return ''

    def version_string(self) -> Union[str, None]:
        try:
            return str(lookup_symbol('qVersion')[0].value()())
        except:
            pass
        try:
            ns = self.namespace()
            return str(parse_and_eval("((const char*(*)())'%sqVersion')()" % ns))
        except:
            pass
        return None

    def version(self) -> int:
        try:
            # Only available with Qt 5.3+
            qt_version = int(str(parse_and_eval('((void**)&qtHookData)[2]')), 16)
            self.qtVersion = lambda: qt_version
            return qt_version
        except:
            pass

        try:
            version = self.version_string()
            (major, minor, patch) = version[version.find('"') + 1:version.rfind('"')].split('.')
            qt_version = 0x10000 * int(major) + 0x100 * int(minor) + int(patch)
            self.qtVersion = lambda: qt_version
            return qt_version
        except:
            # Use fallback until we have a better answer.
            return self.fallbackQtVersion

    def symbolAddress(self, symbolName) -> Value:
        res = parse_and_eval('(qsizetype*)' + symbolName)
        return None if res is None else res

    def qtHookDataSymbolName(self) -> str:
        return 'qtHookData'

    def type_info_version(self) -> Union[int, None]:
        addr = self.symbolAddress(self.qtHookDataSymbolName())
        if addr:
            # Only available with Qt 5.3+
            hook_version = addr.dereference()
            if hook_version >= 3:
                ti_version = int((addr + 6).dereference())
                self.qtTypeInfoVersion = lambda: ti_version
                return ti_version
        return None


qt_instance__ = Qt()


def qt() -> Qt:
    return qt_instance__
