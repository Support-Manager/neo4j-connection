from py2neo.ogm import *


class User(GraphObject):
    __primarykey__ = "id"

    id = Property()

    tickets = RelatedFrom("Ticket", "TICKET_CREATED_BY")
    responses = RelatedFrom("Response", "RESPONSE_CREATED_BY")
    closed = RelatedFrom("Ticket", "CLOSED_BY")
    reopened = RelatedFrom("Ticket", "REOPENED_BY")


class Guild(GraphObject):
    __primarykey__ = "id"

    id = Property()
    channel = Property()
    support_role = Property()
    prefix = Property()
    default_scope = Property()

    tickets = RelatedFrom("Ticket", "LOCATED_ON")


class Ticket(GraphObject):
    __primarykey__ = "id"

    id = Property()
    title = Property()
    description = Property()
    priority = Property()
    scope = Property()
    state = Property()
    updated = Property()

    located_on = RelatedTo(Guild)
    created_by = RelatedTo(User, "TICKET_CREATED_BY")
    closed_by = RelatedTo(User)
    reopened_by = RelatedTo(User)

    responses = RelatedFrom("Response", "REFERS_TO")

    @property
    def author(self):
        return list(self.created_by)[0]

    @property
    def guild(self):
        return list(self.located_on)[0]


class Response(GraphObject):
    __primarykey__ = "id"

    id = Property()

    located_on = RelatedTo(Guild)
    created_by = RelatedTo(User, "RESPONSE_CREATED_BY")
    refers_to = RelatedTo(Ticket)

    @property
    def guild(self):
        return list(self.located_on)[0]

    @property
    def author(self):
        return list(self.created_by)[0]

    @property
    def ticket(self):
        return list(self.refers_to)[0]
