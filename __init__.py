from mycroft.skills.core import MycroftSkill, intent_handler, IntentBuilder
from mycroft.skills.intent_service import VocabularyIntentParser
from mycroft.util import create_daemon
from mycroft.util.log import LOG
import random
 
class GoodMorningSkill(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.parser = None
        self.affirmations = [
            "You are loved",
            "You are deserving of a happy, fulfilling life, and you have the power to create that for yourself",
            "You are capable of achieving your goals and dreams",
            "You are doing your best, and that is enough",
            "You are not defined by your mistakes, and you have the power to learn and grow from them"
        ]
        self.other_options = [
            "What's the weather like today?",
            "Tell me a joke",
            "Play kiss FM"
        ]
 
    def initialize(self):
        self.parser = VocabularyIntentParser(self.voc_dir)
        self.register_vocab_intent("AffirmationIntent", "en-us")
        self.register_vocab_intent("YesIntent", "en-us")
        self.register_vocab_intent("NoIntent", "en-us")
 
    @intent_handler('morning.good.intent')
    def handle_morning_good(self, message):
        self.speak_dialog('morning.good')
        self.speak("Good morning, would you like to hear some words of affirmation?")
 
    @intent_handler(IntentBuilder("AffirmationIntent").require("affirmation"))
    def handle_affirmation_intent(self, message):
        affirmation = random.choice(self.affirmations)
        self.speak_dialog("affirmation_response")
        self.speak(affirmation)
 
    @intent_handler(IntentBuilder("YesIntent").require("yes"))
    def handle_yes_intent(self, message):
        affirmation = random.choice(self.affirmations)
        self.speak(affirmation)
 
    @intent_handler(IntentBuilder("NoIntent").require("no"))
    def handle_no_intent(self, message):
        self.speak_dialog("no-response")
        for option in self.other_options:
            self.speak(option)
 
    @staticmethod
    def create_skill():
        return GoodMorningSkill()