from py2neo.ogm import GraphObject, Property, RelatedTo
from .user import UserMixin
from .guild import GuildMixin


class OutlawMixin(GraphObject):
    """ Base class for different outlaw types. """

    __primarykey__ = "uuid"

    uuid = Property()
    utc = Property()
    reason = Property()

    executed_by = RelatedTo(UserMixin)
    executed_on = RelatedTo(GuildMixin)
    applies_to = RelatedTo(UserMixin)

    @property
    def author(self):
        return list(self.executed_by)[0]

    @property
    def guild(self):
        return list(self.executed_on)[0]

    @property
    def affected_user(self):
        return list(self.applies_to)[0]


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
