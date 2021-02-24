from app.domains.event_room.models import EventRoom
from database.text_db.process import read_id, read_all, append_model


class EventRoomAction:

    def create(self, data: dict):
        eventRoom = EventRoom(name=data["name"], capacity=data["capacity"])

        if not read_id(local_name="event_room", model=eventRoom):
            append_model(local_name="event_room", model=eventRoom)
            return eventRoom
        else:
            return f"Registro não salvo!\n"

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id: int = None):
        if id:
            eventRooms = read_id(local_name="event_room", model=EventRoom(id=id))
        else:
            eventRooms = read_all(local_name="event_room")
        return eventRooms
