from nose.tools import *
import game

class TestGame(object):
    @classmethod
    def setupClass(self):
        self.game = game.Game()

    def testPrompt(self):
        prompt_text = self.game.generate_prompt()

        assert_true("Location: " in prompt_text)
        assert_true("Health: " in prompt_text)
        assert_true("Exits: " in prompt_text)
        assert_true("What will you do?" in prompt_text)

    def testEvaluate(self):
        self.game.move = 'hack the planet'
        self.game.evaluate_move()
        assert_true("HACK THE PLANET" in self.game.flash_text)

    def testFlash(self):
        sample = 'HACK THE PLANET!!!!!'
        self.game.flash_text = sample

        assert_equal(sample, self.game.flash())
        assert_equal('', self.game.flash())
