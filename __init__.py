from mycroft import MycroftSkill, intent_file_handler


class GoodMorning(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('morning.good.intent')
    def handle_morning_good(self, message):
        self.speak_dialog('morning.good')


def create_skill():
    return GoodMorning()

