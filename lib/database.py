###########
# Database handling for lioness
####
import MySQLdb


class DataBase():
        conn = ''
        def __init__(self, dbname, username, mypass):
                self.conn = MySQLdb.connect(user=username, passwd=mypass, db=dbname )

        def show_tables(self):
                return self.query("""SHOW TABLES;""", ())
                

        def query(self, query, holders):
                #print("qing {}".format(query))

                if (len(holders) == 0):
                        self.conn.query(query)
                        result = self.conn.use_result()
                        r = result.fetch_row(0)
                        #print(r)
                        return r
                else:
                        #print("++++++++++++\n")
                        #print(query)
                        #print(holders)
                        #print("++++++++++++\n")
                        
                        c = self.conn.cursor()
                        try:
                                r = c.execute(query, holders)
                        #print("++++++++++++ \n {}\n".format(r))
                                r =  c.fetchall()
                                self.conn.commit()
                        except MySQLdb.Error as e:
                                #print(e)
                                r = repr(e)
                        return r

                
