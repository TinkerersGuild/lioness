#############
# Channel module for tracking which channels to listen in, and 
# channel ops etc.


class ChannelManager():
        lookup = dict()
        revlookup = dict()
        channels = { "join": list(),
                        "known": list(),
                        "watching": list()
        }

        def __init__(self, **kwargs):
                self.dbconn = kwargs["dbconn"] 
                self.log = kwargs["log"]
                chanjoin = self.dbconn.query("SELECT name FROM channels WHERE channels.listen=1", ())
                for chan in chanjoin:
                        self.channels["join"].append(chan[0])
                print(self.channels["join"])

        def get_channels(self):
                return self.channels;
        
        def set_lookup(self, cid, name):
                self.lookup[cid] = name
                self.revlookup[name] = cid

        def get_name(self, cid):
                return self.lookup.get(cid)



        def add_chans(self, chans):
                for chan in chans['channels']:
                        err = self.dbconn.query("INSERT IGNORE INTO channels(`name`, `channelID`) VALUES(%s, %s)", [chan['name'], chan['id']])
                        self.set_lookup(chan['id'], chan['name'])        
        
                        self.log.debug("{} : {}".format(chan['name'], chan['id']))
                        self.channels['known'].append(chan['name'])

                        if (chan['name'] in self.channels['join']):

                                self.log.debug( "Found watching channel {}".format(chan['name']))
                                self.channels['watching'].append(chan['id'])

                for chan in self.channels['watching']:
                        self.log.debug("Watching {}".format(chan))           
 
