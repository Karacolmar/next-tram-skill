from mycroft import MycroftSkill, intent_file_handler


class NextTram(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tram.next.intent')
    def handle_tram_next(self, message):
        self.speak_dialog('tram.next')


def create_skill():
    return NextTram()

