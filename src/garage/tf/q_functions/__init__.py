"""Q-Functions for TensorFlow-based algorithms."""
# noqa: I100

from garage.tf.q_functions.continuous_cnn_q_function import \
    ContinuousCNNQFunction  # noqa: I100
from garage.tf.q_functions.continuous_mlp_q_function import \
    ContinuousMLPQFunction
from garage.tf.q_functions.discrete_cnn_q_function import DiscreteCNNQFunction
from garage.tf.q_functions.discrete_mlp_q_function import DiscreteMLPQFunction
from garage.tf.q_functions.q_function import QFunction

__all__ = [
    'QFunction', 'ContinuousMLPQFunction', 'DiscreteCNNQFunction',
    'DiscreteMLPQFunction', 'ContinuousCNNQFunction'
]
