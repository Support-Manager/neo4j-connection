from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo
from .user import UserMixin
from .guild import GuildMixin


class TicketMixin(GraphObject):
    __primarylabel__ = "Ticket"
    __primarykey__ = "uuid"

    uuid = Property()
    id = Property()
    title = Property()
    description = Property()
    priority = Property()
    scope = Property()
    state = Property()
    updated = Property()

    located_on = RelatedTo(GuildMixin, "TICKET_LOCATED_ON")
    created_by = RelatedTo(UserMixin, "TICKET_CREATED_BY")
    closed_by = RelatedTo(UserMixin)
    reopened_by = RelatedTo(UserMixin)
    deleted_by = RelatedTo(UserMixin, "TICKET_DELETED_BY")

    responses = RelatedFrom("ResponseMixin", "REFERS_TO")

    @property
    def author(self):
        return list(self.created_by)[0]

    @property
    def guild(self):
        return list(self.located_on)[0]
