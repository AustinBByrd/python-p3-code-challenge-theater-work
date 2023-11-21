class Audition:
    all = []
    def __init__(self, role, actor, location, phone):
        self.role = role
        self.actor = actor
        self.location = location
        self.phone = phone
        self.hired = False
        type(self).all.append(self)

    @property
    def actor(self):
        return self._actor
    @actor.setter
    def actor(self, actor):
        if isinstance(actor, str) and 2< len(actor)<21:
            self._actor= actor
        else:
            raise Exception("Sorry, must be str and btwn 3-20 char")

    @property
    def role(self):
        return self._role
    @role.setter
    def role(self, role):
        from lib.role import Role
        if isinstance(role, Role):
            self._role = role
        else:
            raise Exception('not role')
   
    def call_back(self):
        self.hired = True
        return