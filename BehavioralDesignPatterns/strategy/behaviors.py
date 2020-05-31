from abstract_behavior import AbstractBehavior
# Concrete Strategies

class AgressiveBehavior(AbstractBehavior):

    def move_command(self):
        print("\tAggresive behavior: if find another robot attack it.")


class DefensiveBehavior(AbstractBehavior):

    def move_command(self):
        print("\t Defensive behavior: if find another robot run from it.")


class NormalBehavior(AbstractBehavior):

    def move_command(self):
        print("\t Normal behavior: if find another robot ignore it.")