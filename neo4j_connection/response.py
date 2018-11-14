from py2neo.ogm import GraphObject, Property, RelatedTo
from .user import UserMixin
from .guild import GuildMixin
from .ticket import TicketMixin


class ResponseMixin(GraphObject):
    __primarylabel__ = "Response"
    __primarykey__ = "uuid"

    uuid = Property()
    id = Property()

    content = Property()
    deleted = Property()
    updated = Property()

    located_on = RelatedTo(GuildMixin, "RESPONSE_LOCATED_ON")
    created_by = RelatedTo(UserMixin, "RESPONSE_CREATED_BY")
    deleted_by = RelatedTo(UserMixin, "RESPONSE_DELETED_BY")
    refers_to = RelatedTo(TicketMixin)

    @property
    def guild(self):
        return list(self.located_on)[0]

    @property
    def author(self):
        return list(self.created_by)[0]

    @property
    def ticket(self):
        return list(self.refers_to)[0]
