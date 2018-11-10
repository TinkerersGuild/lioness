from plugins import PluginResponse, Plugin
import sys

from datetime import datetime


class lunch(Plugin):    

        seasons = (
                "Chaos",
                "Discord",
                "Confusion",
                "Bureaucracy",
                "The Aftermath",
                )

        days = (
                "Sweetmorn",
                "Boomtime",
                "Pungenday",
                "Prickle-Prickle",
                "Setting Orange"
                )



        def __init__(self, dbconn):
                self.keyword = ("date",)

        def command(self, args):
                response = PluginResponse()

                day_of_year = datetime.now().timetuple().tm_yday

                seaday = int(day_of_year % 73)
                season = self.seasons[int(day_of_year / 73)]
                day = self.days[int((day_of_year -1) % 5)]
                response.setText("Today is {}, day {}  of {} . Hail Eris, all Hail Discordia".format(day,seaday, season))
                

                return response


