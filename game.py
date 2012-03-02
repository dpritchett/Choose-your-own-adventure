from textwrap import dedent
from lexicon import verb_list, noun_list, actions

class Game(object):
    def __init__(self):
        self.position = 'origin' # Should load map via a flat file w/YAML maybe
        self.health = 3
        self.move = ''
        self.flash_text = ''

#       while 'quit' not in self.move:
#           self.loop()

    def generate_prompt(self):
        prompt_string =  """
    {0}
    Location:   {1}.
    Health:     {2}.
    Exits:      Front door, side door, back door.

What will you do?
>""".format(
                self.flash(),
                self.position.title(),
                self.health)

        return prompt_string

    def loop(self):
        print self.generate_prompt(),
        self.move = raw_input()

        self.evaluate_move()

        if self.move != 'quit':
            self.loop()

    def flash(self):
        output = self.flash_text
        self.flash_text = ''
        return output

    def parse_input(self):
        words = self.move.split()

        verbs = [word for word in actions if word in words]

        for verb in verbs:
            return  [actions[verb][noun] for noun in actions[verb] if noun in words]

    def evaluate_move(self):
        flavor = { 'hack': 'HACK THE PLANET!!!!!',
                }

        for phrase in flavor:
            if phrase in self.move:
                self.flash_text = flavor[phrase] + '\n'
                return

        return
