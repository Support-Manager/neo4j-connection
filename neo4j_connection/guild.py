from py2neo.ogm import GraphObject, Property, RelatedFrom
from .user import UserMixin


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

    joined_users = RelatedFrom(UserMixin, "JOINED_GUILD")

    warnings = RelatedFrom("WarningMixin", "WARNING_EXECUTED_ON")
    kicks = RelatedFrom("KickMixin", "KICK_EXECUTED_ON")
    bans = RelatedFrom("BanMixin", "BAN_EXECUTED_ON")

    blacklist = RelatedFrom(UserMixin, "BLACKLISTED_ON")
