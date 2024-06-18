class HunterBase:
    publishedVulnerabilities = 0

    @staticmethod
    def parse_docs(docs):
        """returns tuple of (name, docs)"""
        if not docs:
            return __name__, "<no documentation>"
        docs = docs.strip().split("\n", 1)
        name = docs[0].strip()
        documentation = docs[1].strip().replace("\n", " ") if len(docs) > 1 else "<no documentation>"
        return name, documentation

    @classmethod
    def get_name(cls):
        name, _ = cls.parse_docs(cls.__doc__)
        return name

    def publish_event(self, event):
        # Import here to avoid circular import from events package.
        # imports are cached in python so this should not affect runtime
        from ..events.event_handler import handler  # noqa

        handler.publish_event(event, caller=self)

    @staticmethod
    def parse_docs(docs):
        """returns tuple of (name, docs)"""
        if not docs:
            return __name__, "<no documentation>"
        docs = docs.strip().split("\n", 1)
        name = docs[0].strip()
        documentation = docs[1].strip().replace("\n", " ") if len(docs) > 1 else "<no documentation>"
        return name, documentation

    @classmethod
    def get_name(cls):
        name, _ = cls.parse_docs(cls.__doc__)
        return name


class ActiveHunter(HunterBase):
    pass


class Hunter(HunterBase):
    pass


class Discovery(HunterBase):
    pass
