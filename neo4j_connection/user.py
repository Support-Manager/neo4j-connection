from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo


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
