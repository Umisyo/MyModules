#const type for Python3
import sys

class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError('この名前の定数はすでに定義されています。 (%s)' % name)
        self.__dict__[name] = value

sys.modules[__name__]=_const()