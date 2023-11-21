from lib.audition import Audition


class Role:
    all=[]
    def __init__(self, character_name):
        self.character_name=character_name
        type(self).all.append(self)
    
    @property
    def character_name(self):
        return self._character_name
    
    @character_name.setter
    def character_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._character_name=name
        else:
            raise Exception("character_name must be a non-empty string")
    
    def auditions(self):
        return [audition for audition in Audition.all if audition.role == self]
    def actors(self):
        return [audition.actor for audition in Audition.all if audition.role == self]
    def locations(self):
        return [audition.location for audition in Audition.all if audition.role == self]
    
    def lead(self):
        lst = [audition.actor for audition in self.auditions() if audition.hired]
        if len(lst)>0:
            return lst[0]
        else:
            return 'no actor has been hired for this role'
    def understudy(self):
        lst = [audition.actor for audition in self.auditions() if audition.hired]
        if len(lst)>1:
            return lst[1]
        else:
            return 'no actor has been hired for understudy for this role'
    
    @classmethod
    def not_cast(cls):
        return [ role for role in cls.all if role.lead() == 'no actor has been hired for this role']
    
    def create_audition(self, actor, location, phone):
        audition = Audition(self, actor, location, phone)
        return audition