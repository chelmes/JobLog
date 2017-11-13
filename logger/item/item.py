import datetime as dt

class Item:
    def __init__(self, name, net_time, date_start=None, date_end=None):
        self.name=name
        self.net_time=net_time
        if date_start is not None:
            self.date_start=date_start
        else:
            #get current date
            self.date_start=dt.date.today().isoformat()
        if date_end is not None:
            self.date_end=date_end
        else:
            self.date_end=self.date_start
        self.id=dt.date.today().isoformat()

    #TODO: Not sure if this is the most efficient way
    def get(self, key):
        if key == 'name':
            value = self.name
        if key == 'net_time':
            value = self.net_time
        if key == 'date_start':
            value = self.date_start
        if key == 'date_end':
            value = self.date_end
        if key == 'id':
            value = self.id
        return value

    def set(self, key, value):
        if self.get(key) is not None:
            print("In this item %s is already set!" %key)
        else:
            if key == 'name':
                self.name = value
            if key == 'net_time':
                self.net_time = value
            if key == 'date_start':
                self.date_start = value
            if key == 'date_end':
                self.date_end = value
            if key == 'id':
                self.id = value

if __name__=="main":
    pass
