import builtins
from abc import ABCMeta
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from yandex_music import Client

ujson: bool = False
try:
    import ujson as json

    ujson = True
except ImportError:
    import json

reserved_names = [name.lower() for name in dir(builtins)]


class YandexMusicObject:
    __metaclass__ = ABCMeta
    _id_attrs: tuple = ()

    def __str__(self) -> str:
        return str(self.to_dict())

    def __repr__(self) -> str:
        return str(self)

    def __getitem__(self, item):
        return self.__dict__[item]

    @classmethod
    def de_json(cls, data: dict, client: Optional['Client']) -> Optional[dict]:
        """Десериализация объекта.

        Args:
            data (:obj:`dict`): Поля и значения десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`yandex_music.YandexMusicObject`: Объект класса :class:`yandex_music.YandexMusicObject`.
        """
        if not data:
            return None

        data = data.copy()

        return data

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=not ujson)

    def to_dict(self) -> dict:
        def parse(val):
            if hasattr(val, 'to_dict'):
                return val.to_dict()
            elif isinstance(val, list):
                return [parse(it) for it in val]
            elif isinstance(val, dict):
                return {key: parse(value) for key, value in val.items()}
            else:
                return val

        data = self.__dict__.copy()
        data.pop('client', None)
        data.pop('_id_attrs', None)

        for k, v in data.copy().items():
            if k.lower() in reserved_names:
                data.pop(k)
                data.update({f'{k}_': v})

        return parse(data)

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self._id_attrs == other._id_attrs
        return super(YandexMusicObject, self).__eq__(other)

    def __hash__(self):
        if self._id_attrs:
            frozen_attrs = tuple(frozenset(attr) if isinstance(attr, list) else attr for attr in self._id_attrs)
            return hash((self.__class__, frozen_attrs))
        return super(YandexMusicObject, self).__hash__()
