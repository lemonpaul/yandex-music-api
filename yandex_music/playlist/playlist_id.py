from typing import TYPE_CHECKING, Optional, List

from yandex_music import YandexMusicObject

if TYPE_CHECKING:
    from yandex_music import Client


class PlaylistId(YandexMusicObject):
    """Класс, представляющий уникальный идентификатор плейлиста.

    Attributes:
        uid (:obj:`int`): Уникальный идентификатор пользователя владеющим плейлистом.
        kind (:obj:`int`): Уникальный идентификатор плейлиста.
        client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

    Args:
        uid (:obj:`int`): Уникальный идентификатор пользователя владеющим плейлистом.
        kind (:obj:`int`): Уникальный идентификатор плейлиста.
        client (:obj:`yandex_music.Client`, optional): Объект класса :class:`yandex_music.Client`, представляющий клиент
            Yandex Music.
        **kwargs: Произвольные ключевые аргументы полученные от API.
    """

    def __init__(self,
                 uid: int,
                 kind: int,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.uid = uid
        self.kind = kind

        self.client = client
        self._id_attrs = (self.uid, self.kind)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['PlaylistId']:
        """Десериализация объекта.

        Args:
            data (:obj:`dict`): Поля и значения десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`yandex_music.PlaylistId`: Объект класса :class:`yandex_music.PlaylistId`.
        """
        if not data:
            return None

        data = super(PlaylistId, cls).de_json(data, client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data: dict, client: 'Client') -> List['PlaylistId']:
        """Десериализация списка объектов.

        Args:
            data (:obj:`list`): Список словарей с полями и значениями десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`list` из :obj:`yandex_music.PlaylistId`: Список объектов класса :class:`yandex_music.PlaylistId`.
        """
        if not data:
            return []

        playlist_ids = list()
        for playlist_id in data:
            playlist_ids.append(cls.de_json(playlist_id, client))

        return playlist_ids
