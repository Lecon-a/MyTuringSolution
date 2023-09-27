import numpy as np

encoder_hidden_state = np.array([0.2, 0.5, -0.3])

decoder_state = np.array([0.4, 0.1, -0.2])

attention_score = np.dot(encoder_hidden_state, decoder_state)

# this gives a scalar value
attention_weights = np.exp(attention_score) / np.exp(attention_score)


context_vector = attention_weights * encoder_hidden_state

print(context_vector)
