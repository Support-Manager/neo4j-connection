from py2neo.ogm import *


class User(GraphObject):
    __primarykey__ = "id"

    uid = Property("id")

    tickets = RelatedFrom("Ticket", "CREATED_BY")
    responses = RelatedFrom("Response", "CREATED_BY")


class Server(GraphObject):
    __primarykey__ = "id"

    sid = Property("id")
    channel = Property()
    support_role = Property()
    prefix = Property()
    default_scope = Property()

    tickets = RelatedFrom("Ticket", "CREATED_ON")


class Ticket(GraphObject):
    __primarykey__ = "id"

    tid = Property("id")
    title = Property()
    description = Property()
    priority = Property()
    scope = Property()
    closed = Property()

    created_on = RelatedTo(Server)
    created_by = RelatedTo(User)
    responses = RelatedFrom("Response", "ATTACHED_TO")

    @property
    def author(self):
        return list(self.created_by)[0]

    @property
    def server(self):
        return list(self.created_on)[0]


class Response(GraphObject):
    __primarykey__ = "id"

    rid = Property("id")

    created_on = RelatedTo(Server)
    created_by = RelatedTo(User)
    attached_to = RelatedTo(Ticket)

    @property
    def server(self):
        return list(self.created_on)[0]

    @property
    def author(self):
        return list(self.created_by)[0]

    @property
    def ticket(self):
        return list(self.attached_to)[0]
