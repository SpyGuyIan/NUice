from pysm import StateMachine, State, Event

class Carosel(StateMachine):

    def __init__(self, name):
        super().__init__(name)
        
        # Clindren state machines
        self.drilling = Drill("drilling")
        self.melting = Melt("melting")
        
        # Main states
        init = State("init")
        manual = State("manual")
        repos = State("repos")
        steady = State("steady")
        
        # Sub-States
        self.add_state(init, initial=True)
        self.add_state(manual)
        self.add_state(repos)
        self.add_state(steady)

        # Sub-state transitions
        self.add_transition(self.init, self.manual, event='manual')
        self.add_transition(self.repos, self.manual, event='manual')
        self.add_transition(self.steady, self.manual, event='manual')
        self.add_transition(self.manual, self.repos, event='reposition')
        self.add_transition(self.steady, self.repos, event='reposition')
        self.add_transition(self.init, self.repos, event='initialized')
        self.add_transition(self.repos, self.steady, event='steady')

        self.init.handlers = {'enter': self.initOnEnter}
        self.repos.handlers = {'turn': self.turn,
                               'exit': self.reposExit}
        self.steady.handlers = {'exit': self.exitSteady}

class Drill(StateMachine):

    def __init__(self, name):
        super().__init__(name)

        idle = State("idle")
        descending = State("descending")
        retracting = State("retracting")
        stopped = State("descending")

        self.add_state(idle)
        self.add_state(descending)
        self.add_state(retracting)
        self.add_state(stopped)

        self.add_transition(self.descending, self.idle, event='idle')
        self.add_transition(self.retracting, self.idle, event='idle')
        self.add_transition(self.stopped, self.idle, event='idle')
        self.add_transition(self.idle, self.descending, event='descend')
        self.add_transition(self.retracting, self.descending, event='descend')
        self.add_transition(self.stopped, self.descending, event='descend')
        self.add_transition(self.descending, self.retracting, event='retracting')
        self.add_transition(self.stopped, self.retracting, event='retracting')
        self.add_transition(self.idle, self.stopped, event='stopped')
        self.add_transition(self.descending, self.stopped, event='stopped')
        self.add_transition(self.retracting, self.stopped, event='stopped')
        
        


        

#### Top level state machines
carousel = StateMachine("carousel")
drill = StateMachine("drill")
melt = StateMachine("melt")
filtration = StateMachine("filtration")
cat = StateMachine("cat")

#### Drill
drill_idle = State("drill_idle")
drill_drilling = State("drill_drilling")
drill_retracting = State("drill_retracting")
drill_stopped = State("drill_stopped")
drill.add_state(drill_idle, initial=True)
drill.add_state(drill_drilling)
drill.add_state(drill_retracting)
drill.add_state(drill_stopped)

drill.add_transition(drill_idle, drill_drilling, event='start_drill')
drill.add_transition(drill_idle, drill_stopped, event='stop')
drill.add_transition(drill_drilling, drill_stopped, event='stop')
drill.add_transition(drill_retracting, drill_stopped, event='stop')
drill.add_transition(drill_drilling, drill_retracting, event='retract_drill')
drill.add_transition(drill_retracting, drill_drilling, event='start_drill')
drill.add_transition(drill_stopped, drill_drilling, event='start_drill')
drill.add_transition(drill_stopped, drill_retracting, event='retract_drill')
drill.add_transition(drill_stopped, drill_idle, event='idle')
drill.add_transition(drill_drilling, drill_idle, event='idle')
drill.add_transition(drill_retracting, drill_idle, event='idle')

#### Melt
melt_idle = State("met_idle")
melt_descending = State("melt_descending")
melt_rockwell = State("melt_rockwell")
melt_bowl = State("melt_bowl")
melt_retracting = State("retracting")
melt_stopped = State("stopped")
melt.add_state(melt_idle, initial=True)
melt.add_state(melt_descending, initial=True)
melt.add_state(melt_rockwell, initial=True)
melt.add_state(melt_bowl, initial=True)
melt.add_state(melt_retracting, initial=True)
melt.add_state(melt_stopped, initial=True)

melt.add_transition(melt_idle, melt_descending, event='melt_descend')
melt.add_transition(melt_retracting, melt_descending, event='melt_descend')
melt.add_transition(melt_stopped, melt_descending, event='melt_descend')
melt.add_transition(melt_rockwell, melt_descending, event='melt_descend')
melt.add_transition(melt_bowl, melt_descending, event='melt_descend')
melt.add_transition(melt_idle, melt_stopped, event='stop')
melt.add_transition(melt_descending, melt_stopped, event='stop')
melt.add_transition(melt_retracting, melt_stopped, event='stop')
melt.add_transition(melt_rockwell, melt_stopped, event='stop')
melt.add_transition(melt_bowl, melt_stopped, event='stop')
melt.add_transition(melt_descending, melt_retracting, event='retract_melt')
melt.add_transition(melt_stopped, melt_retracting, event='retract_melt')
melt.add_transition(melt_rockwell, melt_retracting, event='retract_melt')
melt.add_transition(melt_bowl, melt_retracting, event='retract_melt')
melt.add_transition(melt_stopped, melt_idle, event='idle')
melt.add_transition(melt_drilling, melt_idle, event='idle')
melt.add_transition(melt_retracting, melt_idle, event='idle')
melt.add_transition(melt_rockwell, melt_idle, event='idle')
melt.add_transition(melt_bowl, melt_idle, event='idle')
melt.add_transition(melt_descending, melt_rockwell, event='rockwell')
melt.add_transition(melt_retracting, melt_rockwell, event='rockwell')
melt.add_transition(melt_stopped, melt_rockwell, event='rockwell')
melt.add_transition(melt_bowl, melt_rockwell, event='rockwell')
melt.add_transition(melt_descending, melt_bowl, event='bowl')
melt.add_transition(melt_retracting, melt_bowl, event='bowl')
melt.add_transition(melt_stopped, melt_bowl, event='bowl')
melt.add_transition(melt_rockwell, melt_bowl, event='bowl')

#### Filtration
filtration_idle = State("filtration_idle")
filtration_filter = State("filtration_filter")
filtration_bypass = State("filtration_bypass")
filtration_backwash = State("filtration_backwash")
filtration.add_state(filtration_idle, initial=True)
filtration.add_state(filtration_filter)
filtration.add_state(filtration_bypass)
filtration.add_state(filtration_backwash)

filtration.add_transition(filtration_filter, filtration_idle, event='idle')
filtration.add_transition(filtration_bypass, filtration_idle, event='idle')
filtration.add_transition(filtration_backwash, filtration_idle, event='idle')
filtration.add_transition(filtration_idle, filtration_filter, event='filter')
filtration.add_transition(filtration_bypass, filtration_filter, event='filter')
filtration.add_transition(filtration_backwash, filtration_filter, event='filter')
filtration.add_transition(filtration_idle, filtration_bypass, event='bypass')
filtration.add_transition(filtration_filter, filtration_bypass, event='bypass')
filtration.add_transition(filtration_backwash, filtration_bypass, event='bypass')
filtration.add_transition(filtration_idle, filtration_backwash, event='backwash')
filtration.add_transition(filtration_filter, filtration_backwash, event='backwash')
filtration.add_transition(filtration_bypass, filtration_backwash, event='backwash')

#### Cat
cat_idle = State("cat_idle")
cat_descending = State("cat_descending")
cat_retracting = State("cat_retracting")
cat_scan = State("cat_scan")
cat_stopped = State("cat_stopped")
cat.add_state(cat_idle, initial=True)
cat.add_state(cat_descending)
cat.add_state(cat_retracting)
cat.add_state(cat_scan)



if __name__ == '__main__':
    pass