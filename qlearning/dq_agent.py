import random
import numpy as np

from keras.models import Sequential 
from keras.layers import Dense, Activation, Flatten, Conv2D

from collections import deque

NBACTIONS = 3
IMGHEIGHT = 40
IMGWIDTH = 40
IMGHISTORY = 4

OBSERVEPERIOD = 250
GAMMA = 0.975
BATCH_SIZE = 64

ExReplay_CAPACITY = 2000

class Agent:
     def __init__(self):
          self.model = self.createModel()
          self.ExReplay = deque()
          self.steps = 0
          self.epsilon = 1
         
     def createModel(self):
          model = Sequential()
          model.add(Conv2D(32, kernel_size = 4, strides = (2,2), input_shape = (IMGWIDTH,IMGHEIGHT,IMGHISTORY), padding="same"))
          model.add(Activation("relu"))
          model.add(Conv2D(64, kernel_size = 4, strides = (2,2), padding="same"))
          model.add(Activation("relu"))
          model.add(Conv2D(64, kernel_size = 3, strides = (1,1), padding="same"))
          model.add(Activation("relu"))
          model.add(Flatten())
          model.add(Dense(512))
          model.add(Activation("relu"))
          model.add(Dense(units = NBACTIONS, activation="linear"))

          model.compile(loss="mse", optimizer = "adam")

          return model

     def  FindBestAct(self, s):
          if random.random() < self.epsilon or self.steps < OBSERVEPERIOD:
               return random.randint(0, NBACTIONS -1)
          else:
               qvalue = self.model.predict(s)
               best_action = np.argmax(qvalue)

               return best_action
          
     def CaptureSample(self, sample):
            self.ExReplay.append(sample) 
            if len(self.ExReplay) > ExReplay_CAPACITY:
               self.ExReplay.popleft()
            self.steps += 1
            self.epsilon = 1.0

            if self.steps > OBSERVEPERIOD:
                self.epsilon = 0.75 
                if self.steps > 7000:
                    self.epsilon = 0.5
                if self.steps > 14000:
                    self.epsilon = 0.25
                if self.steps > 30000:
                    self.epsilon = 0.15
                if self.steps > 45000:
                    self.epsilon = 0.1
                if self.steps > 70000:
                    self.epsilon = 0.05

     def Process(self):
        if self.steps > OBSERVEPERIOD:
            mini_batch = random.sample(self.ExReplay, BATCH_SIZE)
            batchlen = len(mini_batch)

            inputs = np.zeros((BATCH_SIZE, IMGHEIGHT, IMGWIDTH, IMGHISTORY))
            targets = np.zeros((inputs.shape[0], NBACTIONS))

            Q_sa = 0
            for i in range(batchlen):
                state_t = mini_batch[i][0]
                action_t = mini_batch[i][0]
                reward_t = mini_batch[i][0]
                state_t1 = mini_batch[i][0]

                inputs[i:i+1] = state_t
                targets[i] = self.model.predict(state_t)
                Q_sa = self.model.predict(state_t1)

                if state_t1 is None:
                    targets[i, action_t] = reward_t
                else:
                    targets[i, action_t] = reward_t + GAMMA * np.max(Q_sa)
                
            
            self.model.fit(inputs, targets, batch_size = BATCH_SIZE, epochs = 1, verbose = 0)

          
     

