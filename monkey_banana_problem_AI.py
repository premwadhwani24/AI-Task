class State:
    def __init__(self, monkey_on_box, box_position, bananas_position, has_bananas=False):
        self.monkey_on_box = monkey_on_box  # True if monkey is on the box
        self.box_position = box_position      # Position of the box
        self.bananas_position = bananas_position  # Position of the bananas
        self.has_bananas = has_bananas        # True if monkey has bananas

    def is_goal(self):
        return self.has_bananas

    def __str__(self):
        return (f"Monkey on box: {self.monkey_on_box}, "
                f"Box position: {self.box_position}, "
                f"Bananas position: {self.bananas_position}, "
                f"Has bananas: {self.has_bananas}")


def climb_box(state):
    """Action: Climb on the box."""
    if not state.monkey_on_box:
        return State(True, state.box_position, state.bananas_position, state.has_bananas)
    return None


def get_banana(state):
    """Action: Get the bananas."""
    if state.monkey_on_box and state.box_position == state.bananas_position:
        return State(state.monkey_on_box, state.box_position, state.bananas_position, True)
    return None


def move_box(state, new_position):
    """Action: Move the box to a new position."""
    if state.monkey_on_box:
        return State(state.monkey_on_box, new_position, state.bananas_position, state.has_bananas)
    return None


def climb_down(state):
    """Action: Climb down from the box."""
    if state.monkey_on_box:
        return State(False, state.box_position, state.bananas_position, state.has_bananas)
    return None


def plan_actions():
    """Plan the actions for the monkey to get the bananas."""
    initial_state = State(False, 'ground', 'ceiling', False)
    states = [initial_state]
    actions = []

    while states:
        current_state = states.pop(0)
        print(current_state)

        if current_state.is_goal():
            print("Goal reached!")
            return actions

        # Try climbing the box
        new_state = climb_box(current_state)
        if new_state and new_state not in states:
            states.append(new_state)
            actions.append("Climb box")

        # Try getting the bananas
        new_state = get_banana(current_state)
        if new_state and new_state not in states:
            states.append(new_state)
            actions.append("Get banana")

        # Try moving the box to a new position
        new_position = 'ceiling'  # Example of a new position
        new_state = move_box(current_state, new_position)
        if new_state and new_state not in states:
            states.append(new_state)
            actions.append("Move box to ceiling")

        # Try climbing down
        new_state = climb_down(current_state)
        if new_state and new_state not in states:
            states.append(new_state)
            actions.append("Climb down")

    print("No solution found.")
    return []


# Run the planner
actions_taken = plan_actions()
print("Actions taken to reach the goal:", actions_taken)
