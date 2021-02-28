from app.domains.event_room.action_mysql import EventRoomActionMySQL


class EventRoomView:

    def __init__(self):
        self.action = EventRoomActionMySQL()

    def post(self):
        name = input("Digite o nome da sala de eventos:")
        capacity = int(input("Digite a capacidade maxima da sala de eventos:"))
        event_room = self.action.create({"name": name, "capacity": capacity})
        return event_room

    def get_id(self):
        id = int(input("Digite o id(0,9999) da sala de eventos:"))
        event_room = self.action.get(id)
        return event_room

    def get_all(self):
        event_rooms = self.action.get()
        return event_rooms

    def put_id(self):
        id = int(input("Digite o id(0,9999) da sala de eventos:"))
        name = input("Digite o novo nome da sala de eventos:")
        capacity = int(input("Digite a nova capacidade maxima da sala de eventos:"))
        event_room = self.action.update_id({"name": name, "capacity": capacity}, id)
        return event_room

    def delete_id(self):
        id = int(input("Digite o id(0,9999) da sala de eventos:"))
        event_room = self.action.delete_id(id)
        return event_room
