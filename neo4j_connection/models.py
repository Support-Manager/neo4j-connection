from py2neo.ogm import *


class UserMixin(GraphObject):
    __primarylabel__ = "User"
    __primarykey__ = "id"

    id = Property()

    tickets = RelatedFrom("TicketMixin", "TICKET_CREATED_BY")
    responses = RelatedFrom("ResponseMixin", "RESPONSE_CREATED_BY")

    closed_tickets = RelatedFrom("TicketMixin", "CLOSED_BY")
    reopened_tickets = RelatedFrom("TicketMixin", "REOPENED_BY")

    has_reported = RelatedFrom("UserMixin", "REPORTED_BY")
    reported_by = RelatedTo("UserMixin")

    has_warned = RelatedFrom("UserMixin", "WARNED_BY")
    warned_by = RelatedTo("UserMixin")

    has_kicked = RelatedFrom("UserMixin", "KICKED_BY")
    kicked_by = RelatedTo("UserMixin")

    has_banned = RelatedFrom("UserMixin", "BANNED_BY")
    banned_by = RelatedTo("UserMixin")

    deleted_responses = RelatedFrom("ResponseMixin", "RESPONSE_DELETED_BY")
    deleted_tickets = RelatedFrom("TicketMixin", "TICKET_DELETED_BY")


class GuildMixin(GraphObject):
    __primarylabel__ = "Guild"
    __primarykey__ = "id"

    id = Property()
    channel = Property()
    support_role = Property()
    prefix = Property()
    default_scope = Property()
    language = Property()
    ticket_category = Property()
    voice_category = Property()
    log_channel = Property()

    tickets = RelatedFrom("TicketMixin", "TICKET_LOCATED_ON")
    responses = RelatedFrom("ResponseMixin", "RESPONSE_LOCATED_ON")


class TicketMixin(GraphObject):
    __primarylabel__ = "Ticket"
    __primarykey__ = "id"

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


class ResponseMixin(GraphObject):
    __primarylabel__ = "Response"
    __primarykey__ = "id"

    id = Property()

    content = Property()
    deleted = Property()

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
