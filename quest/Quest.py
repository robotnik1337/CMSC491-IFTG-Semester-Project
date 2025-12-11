class Quest:
    """

    """
        
    # default constructor
    def __init__(self):
        """Initializes the Quest class"""
        self.name = ""
        self.objective = ""
        self.first_tasks = []
        self.first_task_locations = []
        self.guest_giver = {}
        self.items = []
        self.reward = []
        self.characters = []
        self.enemies = []
        self.goal = ""

    def setName(self, given_name):
        self.name = given_name

    def setObjective(self, given_obj):
        self.objective = given_obj

    def setFirstTasks(self, given_tasks):
        self.first_tasks = given_tasks

    def setTaskLocations(self, given_loc):
        self.first_task_locations = given_loc

    def setGiver(self, giver):
        self.quest_giver = giver

    def setItems(self, given_items):
        self.items = given_items
    
    def setReward(self, rewards):
        self.reward = rewards

    def setCharacters(self, chars):
        self.characters = chars

    def setEnemies(self, enemy):
        self.enemies = enemy
    
    def setGoal(self, goals):
        self.goal = goals
