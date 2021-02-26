from app.domains.event_room.models import EventRoom
from database.mysql_db.connect import DatabaseMySQL
from database.mysql_db.tables import Tables


class EventRoomActionMySQL:

    def __init__(self):
        self.db = DatabaseMySQL()
        self.db.start_connector()

    def create(self, data: dict):
        eventRoom = EventRoom(name=data["name"],
                              capacity=data["capacity"])
        if not self.db.get_id(table=Tables.names[1], id=eventRoom.getId()):
            self.db.create_data(table=Tables.names[1], data=eventRoom.serialize())
            return eventRoom.serialize()
        else:
            return f"{str(eventRoom)}" \
                    "Unsaved record."

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id: int = None):
        if id:
            eventRoom = EventRoom(id=id)
            eventRooms = self.db.get_id(table=Tables.names[1], id=eventRoom.getId())
        else:
            eventRooms = self.db.get_all(table=Tables.names[1])
        print(f"{len(eventRooms)} found.")
        return eventRooms
