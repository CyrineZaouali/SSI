class Singleton:
    hostname: str
    user: str
    password: str
    database: str

    def __init__(self, cls):
        self._instance = None
        self._cls = cls

    def Instance(self, hostname: str, user: str, password: str, database: str):
        if self._instance == None:
            self._instance = self._cls(hostname, user, password, database)
        return self._instance

    def __call__(self):
        raise TypeError("Singletons must be accessed through `Instance()`.")

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)
