from typing import List, Mapping, Set, Tuple, Any


def get_source(config: List[Mapping[str, Any]]) -> Set[int]:
    return {int(chat["source"]) for chat in config}




#def get_destenation(source: int, config: List[Mapping[str, Any]]) -> Set[int]:
#    dest = set()
#    for chat in config:
#        if chat["source"] == source:
#            dest.update(chat["destination"])
#    return dest


def get_destenation(source: int, config: List[Mapping[str, Any]]) -> dict[int, str]:
    dest = {}
    for chat in config:
        if chat["source"] == source:
            dest_id = chat["destination"]
            if isinstance(dest_id, int):
                dest_id = [dest_id]
            for chat_id in dest_id:
                dest[chat_id] = chat.get("name", str(chat_id))
    return dest

