from trip import Trip

class PackageA(Trip):

    def do_coming_transport(self):
        print("The turists are comming by air ...")

    def do_day_a(self):
        print("The turists are visiting the aquarium ...")

    def do_day_b(self):
        print("The turists are going to the beach ...")

    def do_day_c(self):
        print("The turists are going to mountains ...")

    def do_returning_transport(self):
        print("The turists are going home by air ...")

class PackageB(Trip):

    def do_coming_transport(self):
        print("The turists are comming by train ...")

    def do_day_a(self):
        print("The turists are visiting the mountain ...")

    def do_day_b(self):
        print("The turists are going to the beach ...")

    def do_day_c(self):
        print("The turists are going to zoo ...")

    def do_returning_transport(self):
        print("The turists are going home by train ...")
