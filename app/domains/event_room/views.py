from app.domains.event_room.actions import EventRoomAction


class EventRoomView:

    def post(self):
        name = input("Digite o nome da sala de eventos:")
        capacity = int(input("Digite a capacidade maxima da sala de eventos:"))
        eventRoom = EventRoomAction().create({"name": name, "capacity": capacity})
        return eventRoom

    def get_id(self):
        id = int(input("Digite o id(0,9999) da sala de eventos:"))
        eventRoom = EventRoomAction().get(id)
        return eventRoom

    def get_all(self):
        eventRooms = EventRoomAction().get()
        return eventRooms

    def put(self):
        pass

    def delete(self):
        pass
