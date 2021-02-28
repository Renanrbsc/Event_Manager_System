from app.domains.event_room.models import EventRoom
from app.domains.event_room.db_mysql import EventRoomMySQL


class EventRoomActionMySQL:

    def __init__(self):
        self.db = EventRoomMySQL()

    def create(self, data: dict):
        event_room = EventRoom(name=data["name"],
                               capacity=data["capacity"])
        if not self.db.get_by_id(id=event_room.getId()):
            row = self.db.post(data=event_room.serialize())
            return f"{event_room.serialize()}\n{row}"
        else:
            return f"{event_room.serialize()}\nRegistro não salvo."

    def update_id(self, data: dict, id: int):
        event_room = EventRoom(id=id,
                               name=data["name"],
                               capacity=data["capacity"])
        if self.db.get_by_id(id=event_room.getId()):
            row = self.db.put_id(data=event_room.serialize())
            return f"{event_room.serialize()}\n{row}"
        else:
            return f"{event_room.serialize()}\nRegistro não encontrado."

    def delete_id(self, id: int = None):
        event_room = EventRoom(id=id)
        if self.db.get_by_id(id=event_room.getId()):
            return self.db.remove_id(id=event_room.getId())
        else:
            return f"Registro não encontrado."

    def get(self, id: int = None):
        if id:
            event_room = EventRoom(id=id)
            event_rooms = self.db.get_by_id(id=event_room.getId())
        else:
            event_rooms = self.db.get_all()
        print(f"{len(event_rooms)} encontrado(s).")
        return event_rooms
