#%%
from old import dblp
from collections import defaultdict
from functools import partial
import numpy as np
import matplotlib.pyplot as plt

#%%
venues = dblp.load_venues()
print("data loaded")

#%% venues

venue_ids = {i: venue_id for i, venue_id in enumerate(venues.keys())}
probabilities = np.array([venues[k]['p'] for k in venues.keys()], dtype='float32')
prob_mat = np.outer(probabilities, probabilities)
prob_mat *= ((np.ones_like(prob_mat, dtype='float32') - np.eye(prob_mat.shape[0], dtype='float32')) * 2)

#%%
plt.matshow(prob_mat)
plt.show()