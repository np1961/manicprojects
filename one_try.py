import numpy as np


class NeuralNetwork:
    
    def step_all( in_values, 
                _weights_,
                __weights__,
                ___weights___):
        hiddens_one = np.dot(in_values, _weights_) 
        hiddens_one_sigmoid = NeuralNetwork.sigmoid(hiddens_one) 
        
        hiddens_two = np.dot(hiddens_one_sigmoid,__weights__) 
        hiddens_two_sigmoid = NeuralNetwork.sigmoid(hiddens_two) 
        
        
        output = np.dot(hiddens_two_sigmoid, ___weights___) 
        output_sigmoid = NeuralNetwork.sigmoid(output)
        return output_sigmoid
        
    def sigmoid(values, deriv=False):
        return values * (1 - values) if deriv else np.exp(values)/(np.exp(values)+1)
    
    
