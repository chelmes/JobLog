import datetime as dt

class Item:
    """One entry for the DataFrame of the Log. It is able to store time
    information names and ids for each entered activity
    """
    def __init__(self, name, net_time, date_start=None, date_end=None):
        """Constructor of the class 

        Inputs
        ------
        name: string, how is the activity called that is entered?
        net_time: int, how many minutes have you spend doing it?
        date_start: optional,datetime.today(), on which day did the activity
                    start? If not provided gets set to current date
        date_end: optional,datetime.today(), when did it end?
                  If not provided gets set to current date
        """
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
        self.id=dt.datetime.today().isoformat()

    #TODO: Not sure if this is the most efficient way
    def get(self, key):
        """Getter for the attributes

        Looks for attribute named key and returns its value

        Inputs
        ------
        key: string, the attribute's name

        Returns
        -------
        value: string, datetime object, int the attributes value
        """
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
        """Set attribute key of instance as value

        Inputs
        -----
        key: string, determining which attribute gets modified
        value: string, datetime object or int the value for the atrribute

        Returns
        -------
        None
        """
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

    def dataframe_entry(self):
        """ Generate a data entry for the dataframe from an instance of Item

        The relevant data get returned as a list in a specific order
        Inputs
        ------
        None
        
        Returns
        -------
        List of start date, end date, net time and name of item instance
        """
        return [self.date_start, self.date_end, self.net_time, self.name]

if __name__=="main":
    pass
