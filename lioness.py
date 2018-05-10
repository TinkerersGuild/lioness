#!/usr/bin/env python3 

import argparse
import time
import os
import sys
from slackclient import SlackClient
import re
import yaml
import logging
from logging.handlers import TimedRotatingFileHandler
import datetime


def load_configs(cfile):
    """Load the config from the given absolute path file name"""
    try:
        with open(cfile, "r") as conf_file:
            conf = yaml.load(conf_file)
    except :
        e = sys.exc_info()[0]

        print("Could not load: {}".format(e))
        conf = dict()
    return conf



class Lioness():
    """ Lioness is the main class for loading the configs and handling connections

        __init__(self, config, log) takes a dictionary of configs and a logger object

        """
    def __init__(self, config, log):
        """Takes config dict and logger object to initialise """
        self.verbose = 1
        self.log = log
        self.status = "ok"        
        try:
            token = config['APIKEY'].strip()
            os.environ["BOT_TOKEN"] = token
            self.sc = SlackClient(token)
        except:
            self.status = "BAD TOKEN"

        self.dbconn = DataBase(config['dbname'], config['username'], config['passwd'])
        self.log.critical("DBConn {}".format(self.dbconn))

        tables = self.dbconn.show_tables()
        self.log.info( tables)

        self.chanman = ChannelManager(dbconn=self.dbconn, log=self.log)
        self.channels = self.chanman.get_channels()


        self.scheduler = Scheduler(dbconn = self.dbconn, log = self.log)


        self.people = UserManager(self.dbconn, self.sc, self)
        self.people.set_ops(config['owners'])
        self.people.update_users()
        
        self.commander = Commander(self, config['prefix'], config['enable_plugins'])
        self.botname = config['botname']
        self.icon = config['icon']
        
        self.log.info("Channels to join:")
        self.log.info(self.channels['join'])
        self.job = dict()
        

    def connect_to_server(self):
      self.log.critical("Connecting")  
      if (self.sc.rtm_connect()):
        self.log.critical("Connected")  
        return 1
      return 0

    def disconnect(self):
        #sc.rtm_disconnect()
        return 1

    def chanpost(self,mychannel, message):
        self.log.debug("Chanpost: {} {}".format(mychannel, message))
        resp = self.sc.api_call(
        "chat.postMessage", channel=mychannel, text=message,
         username=self.botname, icon_url=self.icon)
        self.log.debug( resp)
        return resp

    def send_im(self, userID, message):
            self.log.debug("Opening IM for {}".format(userID))
            try: 
                resp = self.sc.api_call("im.open", user = userID)
                self.log.debug(resp)
                chat = resp['channel']['id']
                self.log.debug("sending to im chan {}".format(chat))
                resp = self.chanpost(chat, message)
                self.log.debug(resp)
                return True
            except:
                self.log.debug("Yeah, nah {}".format(sys.exc_info()[1]))
                return False

    def ping_owners(self,message):
        for op in self.people.get_owners():
            resp = self.sc.api_call("im.open", user = own['id'])
            own['chat'] = resp['channel']['id']
            self.log.debug( "Pinging owner {}".format(own))
            self.log.debug(sc.api_call("chat.postMessage", as_user="true:", channel=own['chat'], text=message))


    


    def get_timestamp(self,msg):
        if (msg.get('ts')):
            if (float(msg['ts']) > float(self.ts)):
                self.log.error( "Setting timestamp {} ".format(msg['ts']))
            return msg['ts']
        else:
            return self.ts

    



    def setup(self):
        chans = self.sc.api_call("channels.list")
        self.chanman.add_chans(chans)
        resp = self.chanpost("#bot_testing", "boop")
        
        for k,v in resp.items():
            self.log.debug("Key: {} Value: {} \n".format(k, v))
        
        self.ts = resp.get('ts')
        self.log.critical("Timestamp: {}".format(self.ts))

        self.log.critical( "Checking API")
        self.sc.api_call("api.test")
        #DEBUG_LEVEL = 0
    def parse_response(self, event):
        #print("parsing {}".format(event))
        self.ts = event["ts"]
        cname = event["channel"]
        userid = event.get("user", "bot")
        user = self.sc.api_call("users.info", user=userid)
        #print("User {}".format(user))
        #self.log.debug( "User object: {}".format(user))
        txt = event.get('text', '')
        subtype = event.get('subtype', '')
        if not "error" in user:
        # probably a bot
            self.people.check_and_add(user)
                        
            if (re.match("^<https?://", txt)):
                txt = '!store ' + txt 
            elif (subtype != ''):
                self.log.critical("FILE MESSAGE {}".format(event))
                file_data = event.get('file', '')
                if (file_data != ''):
                    url = file_data.get('url_private', "none")
                    fileID = file_data.get('id', "none")
                    txt = "!handle {0} {1} {2} {3}".format(subtype, url, txt, fileID)

            if (re.match('!', txt)):
                self.log.debug( "COMMAND MESSAGE {}".format(txt))
                txt = txt.split()

                commandargs = CommandArgs()
                        
                commandargs.chan = cname
                commandargs.user = user
                commandargs.command = txt[0][1:]
                commandargs.text = ' '
        
                if (len(txt) > 1):
                    commandargs.text = ' '.join(txt[1:])
                
                return(self.commander.handle(commandargs))


    def get_next_job(self):
        self.job = self.scheduler.get_next_job()

    def listen(self):
        _connect = 1
        self.get_next_job()
        while(_connect):
            # HUP received, reload the plugins, disconnect from the server and reconnect
            if (_connect == 2):
                self.log.critical( "++++++++++++ REBOOT OUT OF CHEESE +++++")
                self.disconnect()
                if (self.connect_to_server()):
                    #self.plugins = self.reload_plugins()

                    _connect = 1
                else:
                    _connect = 0
            
            # This might be done better with a queue to ensure rate
            # limiting, but even if you get faster "response" at the
            # bot end, we'd thriottle the response at the slack
            # server, so eh.
            time.sleep(1)
            # Ok, this is how this should work.
            # Get the next job, put the time here. When now() 
            # has past the job time, do the job, get the next job time, etc.
            # need to add jobs to the main list as well.
            if ("time" in self.job ):
                while( datetime.datetime.now() > self.job["time"]):
            # Do the job
                    #print("Oh, now we're doing the job\n" + str(self.job))
                    comm = CommandArgs()
                    comm.user = dict()
                    comm.user["user"] = self.people.build_user_from_id(self.job["userID"])
                    comm.chan = self.job["userID"]
                    comm.command=self.job["job"]
                    comm.text = " ".join((self.job["targetID"], self.job["args"]))
                    response = self.commander.handle(comm)
                    self.log.critical("JOB DONE: {}".format(response.getText()))
                    self.scheduler.job_done(self.job["id"])
                    self.get_next_job()
                    if not "time" in self.job:
                        break
            else:
                self.get_next_job()

           
            resp = self.sc.rtm_read()
            try:
                for event in resp:
                    if event["type"] == "message":
                        #print(resp)
                        reply = self.parse_response(event)
                        if reply and self.verbose:
                            #print(reply.getUser())
                            self.send_im(reply.getUser(), reply.getText())
                            self.chanpost("#bot_testing", self.people.build_user_from_id(reply.getUser())["name"] + " : " + reply.getText())
            except:
                self.log.critical("Something went wrong at 232: {}".format(sys.exc_info()[1]))
            #for chan in self.channels['watching']:
            #    try: 
            #        cname = "#"+ self.chanman.get_name(chan)
            #        resp = self.sc.api_call("channels.history", channel=chan, oldest = self.ts )
#
                    #if "messages" in resp:
                        #reply = self.parse_response(resp, cname)
                        #if reply and self.verbose:
                            #self.send_im(reply.getUser(), reply.getText())
                            #self.chanpost("#bot_testing", reply.getUser() + " : " + reply.getText())
                #except:
                    #self.log.critical("Something went wrong at 232: {}".format(sys.exc_info()[1]))
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prefix')
    parser.add_argument('-c', '--config')
    args = parser.parse_args()
    #print( args)
    PREFIX = args.prefix if args.prefix else "./"
    
    conf = args.config if args.config else "{0}/conf/conf.yaml".format(PREFIX)


    try:
        conf = load_configs(conf)
    except:
        e = sys.exc_info()[0]
        print("Can't load config - have you broken it? {}".format(e))

    sys.path.append(PREFIX+"/lib/")
    from database import DataBase
    from channel import ChannelManager
    from users import UserManager
    from commander import Commander, CommandArgs
    from schedule import Scheduler
    
    log = logging.getLogger("Rotating Log")
    log.setLevel(conf['debug_lvl'])
    handler = TimedRotatingFileHandler( conf['prefix']+ "/log/lioness_log", when="d", interval=1, backupCount=7)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler) 

    log.critical("\n-------------\n----------\nStarting bot...\n")  
    log.debug("CONFIGS: {}".format(conf))  
    
    lioness = Lioness(conf, log)  
    print("Connecting")
    if (lioness.connect_to_server()):    
        print("Upsetting")
        lioness.setup() 
        print("Listening")
        lioness.listen()
    else:
        print("Could not connect")




    
