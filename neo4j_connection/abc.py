from py2neo.ogm import GraphObject, Property, RelatedTo


class OutlawMixin(GraphObject):
    """ Base class for different outlaw types. """

    __primarykey__ = "uuid"

    uuid = Property()
    utc = Property()
    reason = Property()

    executed_by = RelatedTo("UserMixin")
    executed_on = RelatedTo("GuildMixin")
    applies_to = RelatedTo("UserMixin")

    @property
    def author(self):
        return list(self.executed_by)[0]

    @property
    def guild(self):
        return list(self.executed_on)[0]

    @property
    def affected_user(self):
        return list(self.applies_to)[0]
