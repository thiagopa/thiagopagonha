from google.appengine.api import memcache

from suds.cache import Cache


# create a new Cache implementation using app engines MemCache()
class MemCache(Cache):
    '''
    attempt to implement a memcache cache in suds
    '''
    def __init__(self, duration=3600):
        self.duration = duration
        self.client = memcache.Client()
    
    def get(self, id):
        """
        Get a object from the cache by ID.
        @param id: The object ID.
        @type id: str
        @return: The object, else None
        @rtype: any
        """
        string_id = str(id)
        thing = self.client.get(string_id)
        return thing


    def getf(self, id):
        """
        Get a object from the cache by ID.
        @param id: The object ID.
        @type id: str
        @return: The object, else None
        @rtype: any
        """
        return self.get(id)
    
    
    def put(self, id, object):
        """
        Put a object into the cache.
        @param id: The object ID.
        @type id: str
        @param object: The object to add.
        @type object: any
        """
        string_id = str(id)
        self.client.set(string_id, object, self.duration)
    
    
    def putf(self, id, fp):
        """
        Write a fp into the cache.
        @param id: The object ID.
        @type id: str
        @param fp: File pointer.
        @type fp: file-like object.
        """
        self.put(id, fp)
    
    def purge(self, id):
        """
        Purge a object from the cache by id.
        @param id: A object ID.
        @type id: str        
        """
        self.client.delete(str(id))
    
    def clear(self):
        """
        Clear all objects from the cache.
        """
        # I know I could implement this with memcache.Client().flush_all()
        # but I didn't want to mess with App Engine's cache because I'm
        # pretty sure it's global.
        # self.client.flush_all()
        pass    