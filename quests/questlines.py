'''Contains QuestLine and QuestNode classes for character quests'''

# QuestNode represents a single node in a quest line, with conditions and actions
class QuestNode:
    def __init__(self, conditions, actions):
        self.conditions = conditions
        self.actions = actions
        self.next = None
        self.visited = False
    
    def check_conditions(self):
        for condition in self.conditions:
            if condition() is False:
                return False
            return True
    
    def perform_actions(self):
        for action in self.actions:
            action()

# QuestLine represents a sequence of quest nodes
class QuestLine:
    def __init__(self):
        self.current_node = None

    # add a new quest node to the end of the list
    def add_checkpoint(self, conditions, actions):
        new_node = QuestNode(conditions, actions)

        if self.current_node is None:
            self.current_node = new_node
        else:
            # Go to the end of the list
            current_node = self.current_node
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    # check if the current node's conditions are met and progress to the next node if so
    def check_and_progress(self):
        if self.current_node is None:
            #print("No quests active.")
            return False
        
        # if node has not been visited yet, execute actions
        if not self.current_node.visited:
            self.current_node.perform_actions()

        # if all quest conditions are met, go to next quest node
        if self.current_node.check_conditions():
            self.current_node = self.current_node.next
            return True
