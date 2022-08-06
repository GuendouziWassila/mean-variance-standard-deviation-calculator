import numpy as np

def calculate(list):

    if len(list)!=9 :
      raise ValueError('List must contain nine numbers.')
    
    #trasform the list to an Numpy array
    a=np.array(list)
    #reshape the previous array to fit 3x3 dimensions
    a=a.reshape(3,3)
    
    #initialize the calculations dictionary
    calculations = {
    'mean': [],
    'variance': [],
    'standard deviation': [],
    'max': [],
    'min': [],
    'sum': []
    }

    # start calculations using Numpy functions
    ###### tolist is used to transform the Numpy array to a list
    calculations['mean'].append(np.mean(a,axis=0).tolist())
    calculations['mean'].append(np.mean(a,axis=1).tolist())
    calculations['mean'].append(np.mean(a))

    calculations['variance'].append(np.var(a,axis=0).tolist())
    calculations['variance'].append(np.var(a,axis=1).tolist())
    calculations['variance'].append(np.var(a))

    calculations['standard deviation'].append(np.std(a,axis=0).tolist())
    calculations['standard deviation'].append(np.std(a,axis=1).tolist())
    calculations['standard deviation'].append(np.std(a))

    calculations['max'].append(np.max(a,axis=0).tolist())
    calculations['max'].append(np.max(a,axis=1).tolist())
    calculations['max'].append(np.max(a))

    calculations['min'].append(np.min(a,axis=0).tolist())
    calculations['min'].append(np.min(a,axis=1).tolist())
    calculations['min'].append(np.min(a))

    calculations['sum'].append(np.sum(a,axis=0).tolist())
    calculations['sum'].append(np.sum(a,axis=1).tolist())
    calculations['sum'].append(np.sum(a))
    
    return calculations
    
  
  
  