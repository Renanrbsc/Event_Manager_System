from app.domains.event_room.action_mysql import EventRoomActionMySQL


class EventRoomView:

    def post(self):
        name = input("Digite o nome da sala de eventos:")
        capacity = int(input("Digite a capacidade maxima da sala de eventos:"))
        eventRoom = EventRoomActionMySQL().create({"name": name, "capacity": capacity})
        return eventRoom

    def get_id(self):
        id = int(input("Digite o id(0,9999) da sala de eventos:"))
        eventRoom = EventRoomActionMySQL().get(id)
        return eventRoom

    def get_all(self):
        eventRooms = EventRoomActionMySQL().get()
        return eventRooms

    def put(self):
        pass

    def delete(self):
        pass
