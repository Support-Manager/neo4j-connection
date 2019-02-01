from py2neo.ogm import GraphObject as _GraphObject, Property, RelatedTo, RelatedFrom
from .abc import OutlawMixin


class GraphObject(_GraphObject):
    def __eq__(self, other):
        return super().__eq__(other) or (
                (
                    issubclass(other.__class__, self.__class__) or issubclass(self.__class__, other.__class__)
                )
                and getattr(other, 'uuid', other.id) == getattr(self, 'uuid', self.id)
        )


class UserMixin(GraphObject):
    __primarylabel__ = "User"
    __primarykey__ = "id"

    id = Property()

    tickets = RelatedFrom("TicketMixin", "TICKET_CREATED_BY")
    responses = RelatedFrom("ResponseMixin", "RESPONSE_CREATED_BY")

    closed_tickets = RelatedFrom("TicketMixin", "CLOSED_BY")
    reopened_tickets = RelatedFrom("TicketMixin", "REOPENED_BY")

    issued_reports = RelatedFrom("ReportMixin", "REPORT_ISSUED_BY")
    reports = RelatedFrom("ReportMixin", "REPORT_APPLIES_TO")

    executed_warnings = RelatedFrom("WarningMixin", "WARNING_EXECUTED_BY")
    warnings = RelatedFrom("WarningMixin", "WARNING_APPLIES_TO")

    executed_kicks = RelatedFrom("KickMixin", "KICK_EXECUTED_BY")
    kicks = RelatedFrom("KickMixin", "KICK_APPLIES_TO")

    executed_bans = RelatedFrom("BanMixin", "BAN_EXECUTED_BY")
    bans = RelatedFrom("BanMixin", "BAN_APPLIES_TO")

    blacklisted_on = RelatedTo("GuildMixin")

    deleted_responses = RelatedFrom("ResponseMixin", "RESPONSE_DELETED_BY")
    deleted_tickets = RelatedFrom("TicketMixin", "TICKET_DELETED_BY")

    joined_guilds = RelatedTo("GuildMixin", "JOINED_GUILD")

    assigned_tickets = RelatedFrom("TicketMixin", "ASSIGNED_TO")


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
    auto_assigning = Property()

    tickets = RelatedFrom("TicketMixin", "TICKET_LOCATED_ON")
    responses = RelatedFrom("ResponseMixin", "RESPONSE_LOCATED_ON")

    joined_users = RelatedFrom(UserMixin, "JOINED_GUILD")

    warnings = RelatedFrom("WarningMixin", "WARNING_EXECUTED_ON")
    kicks = RelatedFrom("KickMixin", "KICK_EXECUTED_ON")
    bans = RelatedFrom("BanMixin", "BAN_EXECUTED_ON")

    blacklist = RelatedFrom(UserMixin, "BLACKLISTED_ON")

    reports = RelatedFrom("ReportMixin", "REPORT_ISSUED_ON")


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

    assigned_to = RelatedTo(UserMixin)

    responses = RelatedFrom("ResponseMixin", "REFERS_TO")

    @property
    def author(self):
        return list(self.created_by)[0]

    @property
    def guild(self):
        return list(self.located_on)[0]


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


class WarningMixin(OutlawMixin):
    __primarylabel__ = "Warning"

    executed_by = RelatedTo(UserMixin, "WARNING_EXECUTED_BY")
    executed_on = RelatedTo(GuildMixin, "WARNING_EXECUTED_ON")
    applies_to = RelatedTo(UserMixin, "WARNING_APPLIES_TO")


class KickMixin(OutlawMixin):
    __primarylabel__ = "Kick"

    executed_by = RelatedTo(UserMixin, "KICK_EXECUTED_BY")
    executed_on = RelatedTo(GuildMixin, "KICK_EXECUTED_ON")
    applies_to = RelatedTo(UserMixin, "KICK_APPLIES_TO")


class BanMixin(OutlawMixin):
    __primarylabel__ = "Ban"

    days = Property()

    executed_by = RelatedTo(UserMixin, "BAN_EXECUTED_BY")
    executed_on = RelatedTo(GuildMixin, "BAN_EXECUTED_ON")
    applies_to = RelatedTo(UserMixin, "BAN_APPLIES_TO")


class ReportMixin(GraphObject):
    __primarylabel__ = "Report"
    __primarykey__ = "uuid"

    uuid = Property()
    utc = Property()
    reason = Property()

    issued_by = RelatedTo("UserMixin", "REPORT_ISSUED_BY")
    issued_on = RelatedTo("GuildMixin", "REPORT_ISSUED_ON")
    applies_to = RelatedTo("UserMixin", "REPORT_APPLIES_TO")

    @property
    def author(self):
        return list(self.issued_by)[0]

    @property
    def guild(self):
        return list(self.issued_on)[0]

    @property
    def affected_user(self):
        return list(self.applies_to)[0]
