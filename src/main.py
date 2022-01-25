import random
import matplotlib.pyplot as plt
import numpy as np

CELL_CAPACITY = 2.5
BOARD_ROWS = 2
BOARD_COLS = 2
counter = 0
class Environment:
    def __init__(self ):
        self.state = {}
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.state[(i,j)] = 0

    #function that gives reward for every state to agent
    def giveReward(self,action,weight):

        if action in self.state.keys():
            if weight > self.state[action]:
                return (weight-CELL_CAPACITY)

            else:
                return (CELL_CAPACITY-weight)
        else:
            if weight > self.state[action]:
                return (weight-CELL_CAPACITY)

            else:
                return (CELL_CAPACITY-weight)

    # def nextPosition(self,action,weight):
    #     #check if is legal action
    #     #action is tuple (x,y)
    #
    #     return (x,y) # as position





class Agent:
    def __init__(self,id,b,epsilon):
        self.id = id
        self.gamma = 0.9
        self.epsilon = epsilon
        self.lr = 0.2 #learning rate
        self.b = b
        self.actions = [(0,0), (0,1), (1,0),(1,1)]
        self.env = Environment()
        self.states = {}
        self.prevAction = ()
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.states[(i,j)] = self.b
        self.Q_values = {}
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.Q_values[(i, j)] = {}
                for a in self.actions:
                    self.Q_values[(i, j)][a] = 0



    def chooseAction(self):
            # choose action with most expected value
            max_next_reward = -100 #set to a big min value in order to choose always an action and not return null.
            action = ()

            if np.random.uniform(0, 1) <= self.epsilon:

                action = random.choice(self.actions)
                self.prevAction = action
                print("action random " +str(action)+ " for Agent "+str(self.id))
                # env.state[action] = self.b
            else:
                # greedy action
                # greedy action
                for a in self.actions:
                    current_position = self.prevAction

                    next_reward = self.Q_values[current_position][a]

                    if next_reward >= max_next_reward:
                        action = a
                        max_next_reward = next_reward


                # action = np.argmax(self.Q_values)
                print("action from greedy ",action, "from Agent ",self.id, " with weight ",self.b, " and reward ",max_next_reward)
                # self.env.state[action] = self.b
                self.prevAction = action
            return action


    def takeAction(self,env,action,w):
        # position = self.chooseAction()
        # update State
        env.state[action] = env.state[action] + w
        return env.state
    # def calculateQ(self, state, reward, q):
    #
    #         QvalOld = q[state][]
    #         #vgazoume koino paragwnta to alpha sthn gnwsti eksiswsi kai prokuptei to parakatw
    #         newQ = QvalOld + (self.alpha * (reward+ self.gamma*self.nashQtable[state]- QvalOld))
    #     return newQ

    def reset(self,env):
        # self.states = []
        env = Environment()
        return env



def play(agent1,agent2,agent3,agent4,agent5,agent6,agent7,agent8,agent9,agent10,agent11,
         agent12,agent13,agent14,agent15,env,rounds):
    i = 0
    listAgents = list()
    listAgents.append(agent1)
    listAgents.append(agent2)
    listAgents.append(agent3)
    listAgents.append(agent4)
    listAgents.append(agent5)
    listAgents.append(agent6)
    listAgents.append(agent7)
    listAgents.append(agent8)
    listAgents.append(agent9)
    listAgents.append(agent10)
    listAgents.append(agent11)
    listAgents.append(agent12)
    listAgents.append(agent13)
    listAgents.append(agent14)
    listAgents.append(agent15)

    #for stats
    listOfValuesPerEpoch = {}
    for ag in listAgents:
        listOfValuesPerEpoch[ag] = list()
    listOfQPerEpoch = {}
    for ag in listAgents:
        listOfQPerEpoch[ag] = list()
    while i < rounds:

        print("=========================== Epoch ",i," ======================================")
        listOfnewActions = {}
        listOfRewards = {}


        action1 = agent1.chooseAction()
        env.state = agent1.takeAction(env,action1,agent1.b)
        action2 = agent2.chooseAction()
        env.state = agent2.takeAction(env,action2,agent2.b)
        action3 = agent3.chooseAction()
        env.state = agent3.takeAction(env,action3,agent3.b)
        action4 = agent4.chooseAction()
        env.state = agent4.takeAction(env,action4,agent4.b)
        action5 = agent5.chooseAction()
        env.state = agent5.takeAction(env,action5,agent5.b)
        action6 = agent6.chooseAction()
        env.state = agent6.takeAction(env,action6,agent6.b)
        action7 = agent7.chooseAction()
        env.state = agent7.takeAction(env,action7,agent7.b)
        action8 = agent8.chooseAction()
        env.state = agent8.takeAction(env,action8,agent8.b)
        action9 = agent9.chooseAction()
        env.state = agent9.takeAction(env,action9,agent9.b)
        action10 = agent10.chooseAction()
        env.state = agent10.takeAction(env,action10,agent10.b)
        action11 = agent11.chooseAction()
        env.state = agent11.takeAction(env,action11,agent11.b)
        action12 = agent12.chooseAction()
        env.state = agent12.takeAction(env,action12,agent12.b)
        action13 = agent13.chooseAction()
        env.state = agent13.takeAction(env,action13,agent13.b)
        action14 = agent14.chooseAction()
        env.state = agent14.takeAction(env,action14,agent14.b)
        action15 = agent15.chooseAction()
        env.state = agent15.takeAction(env,action15,agent15.b)
        print("Current Env State ", env.state)
        listOfnewActions[agent1] = action1
        listOfnewActions[agent2] = action2
        listOfnewActions[agent3] = action3
        listOfnewActions[agent4] = action4
        listOfnewActions[agent5] = action5
        listOfnewActions[agent6] = action6
        listOfnewActions[agent7] = action7
        listOfnewActions[agent8] = action8
        listOfnewActions[agent9] = action9
        listOfnewActions[agent10] = action10
        listOfnewActions[agent11] = action11
        listOfnewActions[agent12] = action12
        listOfnewActions[agent13] = action13
        listOfnewActions[agent14] = action14
        listOfnewActions[agent15] = action15

        reward1 = agent1.env.giveReward(action1,agent1.b)
        reward2 = agent2.env.giveReward(action2,agent2.b)
        reward3 = agent3.env.giveReward(action3,agent3.b)
        reward4 = agent4.env.giveReward(action4,agent4.b)
        reward5 = agent5.env.giveReward(action5,agent5.b)
        reward6 = agent6.env.giveReward(action6,agent6.b)
        reward7 = agent7.env.giveReward(action7,agent7.b)
        reward8 = agent8.env.giveReward(action8,agent8.b)
        reward9 = agent9.env.giveReward(action9,agent9.b)
        reward10 = agent10.env.giveReward(action10,agent10.b)
        reward11 = agent11.env.giveReward(action11,agent11.b)
        reward12 = agent12.env.giveReward(action12,agent12.b)
        reward13 = agent13.env.giveReward(action13,agent13.b)
        reward14 = agent14.env.giveReward(action14,agent14.b)
        reward15 = agent15.env.giveReward(action15,agent15.b)

        listOfRewards[agent1] = reward1
        listOfRewards[agent2] = reward2
        listOfRewards[agent3] = reward3
        listOfRewards[agent4] = reward4
        listOfRewards[agent5] = reward5
        listOfRewards[agent6] = reward6
        listOfRewards[agent7] = reward7
        listOfRewards[agent8] = reward8
        listOfRewards[agent9] = reward9
        listOfRewards[agent10] = reward10
        listOfRewards[agent11] = reward11
        listOfRewards[agent12] = reward12
        listOfRewards[agent13] = reward13
        listOfRewards[agent14] = reward14
        listOfRewards[agent15] = reward15

        agent1.states[action1] = agent1.b
        agent2.states[action2] = agent2.b
        agent3.states[action3] = agent3.b
        agent4.states[action4] = agent4.b
        agent5.states[action5] = agent5.b
        agent6.states[action6] = agent6.b
        agent7.states[action7] = agent7.b
        agent8.states[action8] = agent8.b
        agent9.states[action9] = agent9.b
        agent10.states[action10] = agent10.b
        agent11.states[action11] = agent11.b
        agent12.states[action12] = agent12.b
        agent13.states[action13] = agent13.b
        agent14.states[action14] = agent14.b
        agent15.states[action15] = agent15.b





        for a in agent1.actions:

                # print("env state ",self.env.state)
                # print("action ",a)
                # print("prev action ",self.prevAction)
            agent1.Q_values[agent1.prevAction][a] = reward1
            agent2.Q_values[agent2.prevAction][a] = reward2
            agent3.Q_values[agent3.prevAction][a] = reward3
            agent4.Q_values[agent4.prevAction][a] = reward4
            agent5.Q_values[agent5.prevAction][a] = reward5
            agent6.Q_values[agent6.prevAction][a] = reward6
            agent7.Q_values[agent7.prevAction][a] = reward7
            agent8.Q_values[agent8.prevAction][a] = reward8
            agent9.Q_values[agent9.prevAction][a] = reward9
            agent10.Q_values[agent10.prevAction][a] = reward10
            agent11.Q_values[agent11.prevAction][a] = reward11
            agent12.Q_values[agent12.prevAction][a] = reward12
            agent13.Q_values[agent13.prevAction][a] = reward13
            agent14.Q_values[agent14.prevAction][a] = reward14
            agent15.Q_values[agent15.prevAction][a] = reward15
        for ag in listAgents:
            listOfValuesPerEpoch[ag].append(env.state[ag.prevAction])
            for s in reversed(ag.states):


                current_q_value = ag.Q_values[s][ag.prevAction]
                reward = current_q_value +  ag.lr *(ag.gamma *  - current_q_value)
                ag.Q_values[s][listOfnewActions[ag]] = round(reward, 3)
            # player1.observe(reward=r1,opReward=r2,opAction=player2.prevAction)
            # player2.observe(reward=r2,opReward=r1,opAction=player1.prevAction)
            print("======================For Agent ", ag.id, " ===========================")
            print(ag.Q_values)
            print("=======================================================================")
        i = i + 1
        agent1.epsilon = agent1.epsilon - 0.01
        agent2.epsilon = agent2.epsilon - 0.01
        agent3.epsilon = agent3.epsilon - 0.01
        agent4.epsilon = agent4.epsilon - 0.01
        agent5.epsilon = agent5.epsilon - 0.01
        agent6.epsilon = agent6.epsilon - 0.01
        agent7.epsilon = agent7.epsilon - 0.01
        agent8.epsilon = agent8.epsilon - 0.01
        agent9.epsilon = agent9.epsilon - 0.01
        agent10.epsilon = agent10.epsilon - 0.01
        agent11.epsilon = agent11.epsilon - 0.01
        agent12.epsilon = agent12.epsilon - 0.01
        agent13.epsilon = agent13.epsilon - 0.01
        agent14.epsilon = agent14.epsilon - 0.01
        agent15.epsilon = agent15.epsilon - 0.01

        env = agent1.reset(env)
        for ag in listAgents:
            for act in ag.actions:
                sumOfQ = 0
                for actj in ag.actions:
                    sumOfQ = sumOfQ + ag.Q_values[act][actj]
            meanQ = sumOfQ/len(ag.actions)
            listOfQPerEpoch[ag].append(meanQ)

    plt.plot(range(rounds),listOfValuesPerEpoch[agent1],label="Agent 1")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent2],label="Agent 2")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent3],label="Agent 3")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent4],label="Agent 4")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent5],label="Agent 5")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent6],label="Agent 6")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent7],label="Agent 7")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent8],label="Agent 8")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent9],label="Agent 9")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent10],label="Agent 10")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent11],label="Agent 11")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent12],label="Agent 12")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent13],label="Agent 13")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent14],label="Agent 14")
    plt.plot(range(rounds),listOfValuesPerEpoch[agent15],label="Agent 15")
    # plt.plot(data[:,1],label="Player 2")
    plt.xlabel("Iterations")
    plt.ylabel("Value per Action per State")
    plt.legend(loc="upper right")

    plt.show()

    plt.plot(range(rounds),listOfQPerEpoch[agent1],label="Agent 1")
    plt.plot(range(rounds),listOfQPerEpoch[agent2],label="Agent 2")
    plt.plot(range(rounds),listOfQPerEpoch[agent3],label="Agent 3")
    plt.plot(range(rounds),listOfQPerEpoch[agent4],label="Agent 4")
    plt.plot(range(rounds),listOfQPerEpoch[agent5],label="Agent 5")
    plt.plot(range(rounds),listOfQPerEpoch[agent6],label="Agent 6")
    plt.plot(range(rounds),listOfQPerEpoch[agent7],label="Agent 7")
    plt.plot(range(rounds),listOfQPerEpoch[agent8],label="Agent 8")
    plt.plot(range(rounds),listOfQPerEpoch[agent9],label="Agent 9")
    plt.plot(range(rounds),listOfQPerEpoch[agent10],label="Agent 10")
    plt.plot(range(rounds),listOfQPerEpoch[agent11],label="Agent 11")
    plt.plot(range(rounds),listOfQPerEpoch[agent12],label="Agent 12")
    plt.plot(range(rounds),listOfQPerEpoch[agent13],label="Agent 13")
    plt.plot(range(rounds),listOfQPerEpoch[agent14],label="Agent 14")
    plt.plot(range(rounds),listOfQPerEpoch[agent15],label="Agent 15")
    # plt.plot(data[:,1],label="Player 2")
    plt.xlabel("Iterations")
    plt.ylabel("Mean Q Value")
    plt.legend(loc="upper right")

    plt.show()

if __name__ == "__main__":
    env = Environment()
    ag1 = Agent(1,0.6,1)
    ag2 = Agent(2,0.6,1)
    ag3 = Agent(3,0.4,1)
    ag4 = Agent(4,0.4,1)
    ag5 = Agent(5,0.4,1)
    ag6 = Agent(6,0.4,1)
    ag7 = Agent(7,0.4,1)
    ag8 = Agent(8,0.2,1)
    ag9 = Agent(9,0.2,1)
    ag10 = Agent(10,0.2,1)
    ag11 = Agent(11,0.2,1)
    ag12 = Agent(12,0.2,1)
    ag13 = Agent(13,0.2,1)
    ag14 = Agent(14,0.2,1)
    ag15 = Agent(15,0.2,1)

    play(ag1,ag2,ag3,ag4,ag5,ag6,ag7,ag8,ag9,ag10,ag11,ag12,ag13,ag14,ag15,env,200) # try also with 200