##############3
# It's all about the people....
# Wed 07 Sep 2016 17:24:37 AEST
import re

class UserManager():
        OPS = list()
        OWNERS = list()
        def __init__(self, dbconn, sc, bot):
                self.dbconn = dbconn
                self.error = 0
                self.sc = sc
                self.bot = bot
        def add_owner(self, op):
                self.OWNERS.append(op)
                self.set_op(op)

        def get_owners(self):
                return self.OWNERS
        
        def set_ops(self, ops):
                for k,v in ops.items():
                        self.set_op(v['id'])

        def set_op(self, op):
                self.OPS.append(op)

        def is_op(self, id):
                return (id in self.OPS)

        def list_users(self):
                self.error = self.dbconn.query("SELECT * FROM `users`", [])
                return self.error
                    
        def update_users(self):
                users = self.dbconn.query("SELECT `userID` FROM `users`", [])
                for user in users:
                    #print("Updating {}".format(user[0])) 
                    self.update_user(user[0])

                return self.error
        def build_user_from_id(self,userID):
                user = dict()
                self.error = self.dbconn.query("SELECT userID,name FROM users WHERE `userID` = %s", [userID,] )
                user["id"] = self.error[0][0]
                user["name"] = self.error[0][1]
                return user
                    
        def get_user_opts(self, userID, opt):
                opts = self.dbconn.query("SELECT * FROM useropts WHERE `userID` = %s AND optionID = (SELECT optionID from options where name = %s)" , [userID,opt] )
                self.bot.log.warning("opts results {} len {} ".format(opts,len(opts)))
                return len(opts)
                
        def get_user_level(self,userID):
                levels = self.dbconn.query("SELECT level FROM users WHERE `userID` = %s", [userID,] )
                #print(levels)
                return levels[0][0]

        def update_user(self, userID):
                try:
                    user_info = self.sc.api_call("users.info", user=userID)
                    #print("Updating {0}\n".format(user_info))
                    self.error = self.dbconn.query("UPDATE `users` SET `name` = %s WHERE `userID` = %s", [user_info["user"]["name"], userID,] )
                except: 
                    self.error = "Could not get user info"
                return self.error

        def check_user(self, userID):
                self.error = self.dbconn.query("SELECT `userID` FROM `users` WHERE `userID` = %s", [userID,] )
                return self.error

        # We'll get a user structure
        def check_and_add(self, user):
                
                exists = self.check_user(user["user"]["id"])

                if not exists:
                        self.error = self.dbconn.query("INSERT INTO `users`(`userID`,  `name`) VALUES(%s, %s)", [user["user"]["id"], user["user"]["name"],] )
                        #print(self.error)
                return self.error       

        #def removeop(self, id):
        def user_id_by_name(self, name):
            self.error = list()
            self.error = self.dbconn.query("SELECT `userID` FROM `users` WHERE `name` = %s", [name,] )
            #print("User ID from name")
            #print(self.error)
            return self.error[0]

        def user_by_name(self, name):
                self.error = list()
                if re.match('<@', name):
                    #print("Tokenizing {}".format(name))
                    uid = self.detokenize(name)
                    #print("Searching for {}".format(uid))
                
                    self.error = self.dbconn.query("SELECT `name` FROM `users` WHERE `userID` = %s", [uid,] )
                else:
                    self.error = self.dbconn.query("SELECT `name` FROM `users` WHERE `name` = %s", [name,] )
                return self.error 

        def detokenize(self, text):
            #print(text)
            text = re.sub("<@", "", text)
            #print(text)
            text = re.sub(">", "", text)
            #print(text)
            return text
