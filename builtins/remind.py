########
# Base URL storer
######
import sys
import time
import re
from pytz import timezone
import parsedatetime.parsedatetime as pdt
from datetime import datetime, timedelta
from plugins import PluginResponse, Plugin

#XXX TODO 
# This works ok, but the message is a bit mangled. What we should do
# is start with the full message, and remove bits until we fail the
# dateparse. Then add bits back one at a time until it passes.
# Whatever we took off is the message.
# We can't start at the start, because we want greedy matching for,
# say, "at 3 pm tomorrow". 

class remind(Plugin):
    def __init__(self, **kwargs):
        self.keyword = ("remind",)
        self.response = PluginResponse()
        self.error = ""
        self.bot = ""
        self.builtin = 1
        self.level = -1

        self.cal = pdt.Calendar()
        self.usage = """ remind <user> [time] to  <message>. Time defaults to "tomorrow"  """

    def add_job(self, args):
        self.bot.get_next_job()
        resp = self.bot.dbconn.query("""INSERT INTO reminders(`userID`, `targetID`, `job`, `jobtime`, `args`) VALUES(%s, %s, %s, %s, %s)""", args)
        self.bot.log.debug(resp)
          

    def command(self, args):
        self.response.setText(self.usage)
        params = ""
        if (re.search(" to " , args.text)): 
            params = args.text.split(" to ", 1)
        else:
            self.bot.log.debug("No separator found")
            return self.response
        
        if len(params) < 2: #username, message
            self.bot.log.debug("Bad params: \n{0}\n{1}".format(params[0], params[1]))
            return self.response

        target = "me"
        remindtime = "tomorrow"
        if (re.search(" ", params[0])): 
            target, remindtime = params[0].split(" ", 1)
        else: 
            target = params[0]
        reminder = " ".join(params[1:])


        try:
            maybetime = self.cal.parse(remindtime)
            self.bot.log.debug("Time from {0}: {1}".format(remindtime, maybetime))
        except:
            maybetime = self.cal.parse("tomorrow")
            
        remindtime = time.strftime('%Y-%m-%d %H:%M:%S', maybetime[0]) 
      
        if (target == "me"):
            target = self.bot.people.user_id_by_name(args.user["user"]["name"])
        else :
            tryuser = self.bot.people.user_id_by_name(target)

            if (tryuser):
                target = tryuser[0]
            
        self.add_job((args.user["user"]["id"], target, "tell", remindtime, reminder ))
        self.bot.get_next_job()
        self.response.setText("Reminding {} at {} : {}".format(target, remindtime, reminder))
        
        return self.response
