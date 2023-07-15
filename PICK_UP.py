import numpy as np
from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
from random import random as random
from warnings import filterwarnings as message
from time import sleep
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import normalize
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.tree import DecisionTreeRegressor
message('ignore')
print('______====______')

df=read_csv('data/pick_data.csv')
df=df.drop('Unnamed: 0',axis=1)
IN=DataFrame([df[column] for column in df.columns]).T
yes='yes'
no='no'
IN.columns=['_fun_', '_flirt_', '_eye_', '_dirty_', '_self_', '_original_void_',
            '_not_define_','_last_partner_', '_rapport_', '_prioritets_',
            '_positive_slide_','_magic_eye_', '_money_dealer_','_pick_production_', '_expert_neuron_',
            '_local_person_','_friend_zone_']
_weight_=np.array([140,75,50,100,50,50,69,190,100,160,200,80,122,130,70,40,347]) 
def weight_learning():
    weight_data=DataFrame(_weight_).T
    weight_data.columns=IN.columns
    normalize_data=DataFrame([int ((weight_data/sum(_weight_))[column][0]*100) for column in weight_data.columns]).T
    normalize_data.columns=weight_data.columns
    weights=DataFrame([str(normalize_data[column][0])+'%' for column in normalize_data.columns]).T
    weights.columns=weight_data.columns
    return weights

def weight_now():
    index=-1
    for column in weight_learning():
        index+=1
        print(column,'___',_weight_[index])

def money_spammer(random_state=no):
    if random_state==yes:
        return random()
    cap_money=1
    ask=input('gift method ? ->')
    
    if ask==yes:
        cap_money-=0.25
        ask=input(' hot future ?  ->')
        if ask==yes:
            cap_money-=0.25
        ask=input(' women unlock for you?  ->')
        if ask==no:
            cap_money-=0.25
            ask=input('Double loser !? ->')
            if ask==yes:
                cap_money-=0.25          
    
    else:
        ask=input(' gift idea  ->')
        if ask==yes:
            cap_money-=0.41
        else:
            print(' > Money_dealer < !!! ')
    return cap_money

def pop_hour(value):
    return value if value<100 else 100

class Pick_Up:
    def __init__(self):
        self.weight=_weight_
        self.IN=IN
        self.OUT=None
        self.eps=np.random.random()
        self.limited=['low','median','high', 'very high']
        self.column_working=['_fun_','_flirt_','_eye_',
                             '_dirty_','_self_','_original_void_',
                             '_rapport_','_money_dealer_']
    def try_me(self,IN):
        _if_=input('(yes/no) ?~~~->')
        if _if_==yes:
            IN['_fun_'][0]=int(input('Fun  ->'))/100
            IN['_flirt_'][0]=int(input('Flirt  ->'))/100
            IN['_eye_'][0]=int(input('Eye_contact  ->'))/100
            IN['_dirty_'][0]=int(input('Dirty  ->'))/100
            IN['_self_'][0]=int(input('Self -> '))/100
            IN['_original_void_'][0]=int(input('Original  ->'))/100
            IN['_not_define_'][0]=int(input('NOT_Define ->'))/100
            IN['_last_partner_'][0]=int(input('Last_partner  ->'))/100
            IN['_rapport_'][0]=int(input('Rapport  ->'))/100
            IN['_prioritets_'][0]=int(input('Prioritets to women  ->'))/100
            IN['_money_dealer_'][0]=money_spammer()
            IN['_positive_slide_'][0]=int(input('Negative balans for women  ->'))/100
            return IN
        
        elif _if_=='random':
            IN['_fun_'][0]=random()
            IN['_flirt_'][0]=random()
            IN['_eye_'][0]=random()
            IN['_dirty_'][0]=random()
            IN['_self_'][0]=random()
            IN['_original_void_'][0]=random()
            IN['_not_define_'][0]=random()
            IN['_last_partner_'][0]=random()
            IN['_rapport_'][0]=random()
            IN['_prioritets_'][0]=random()
            IN['_money_dealer_'][0]=money_spammer(random_state=yes)
            IN['_positive_slide_'][0]=random()
            IN['_local_person_'][0]=True if random()>0.5 else False
            IN['_friend_zone_'][0]=True if random()>0.5 else False
            IN['_expert_neuron_'][0]=True if random()>0.5 else False 
            IN['_pick_production_'][0]=True if random()>0.5 else False
            return IN
        else:
            return IN
        
    
    def data_processor(self,importing):
        
        
        importing['_last_partner_']=[False if self.ReLu_millie (config) else True for config in importing['_last_partner_']]

        
        importing['_prioritets_']=[False if self.ReLu_quarter (config) else True 
                                          for config in importing['_prioritets_']]
        
                                          
                       
        
        importing['_not_define_']=[True if self.ReLu_magic (importing['_not_define_'][index]) == True
                               
                                         else False
                                         for index in range(len(importing['_self_']))]
        
        
        importing['_positive_slide_']=[True if 
                                      self.ReLu_original( importing['_fun_'][index])==True and
                                      self.ReLu_quarter( importing['_positive_slide_'][index])==False
                                      
                                           else False
                                           for index in range(len(importing['_pick_production_']))]
        
                                   
                                   
        importing['_magic_eye_']=[True if self.ReLu_success (config) else False for config in importing['_eye_']]
        
        
        
        importing['_pick_production_']=[True if 
                                      self.ReLu_magic( importing['_flirt_'][index] )==True and 
                                      self.ReLu_magic( importing['_dirty_'][index] )==True and 
                                      importing['_prioritets_'][index]==True and 
                                      importing['_last_partner_'][index]==True and 
                                      self.ReLu_magic(importing['_money_dealer_'][index])==True
                                           else False 
                                           for index in range(len(importing['_pick_production_']))]
        
        importing['_expert_neuron_']=[True if
                                     importing['_magic_eye_'][index]==True and
                                     self.ReLu_magic(importing['_original_void_'][index])==True and
                                     importing['_pick_production_'][index]==True and 
                                     importing['_not_define_'][index]==True
                                     
                                          else False 
                                          for index in range(len(importing['_original_void_']))]
                                     
        
        
        
        
        
        
        importing['_local_person_']=[False if
                                    self.ReLu_magic(importing['_fun_'][index])==False and
                                    self.ReLu_magic(importing['_eye_'][index])==False and
                                    self.ReLu_magic(importing['_rapport_'][index])==False and
                                    self.ReLu_minimals(importing['_original_void_'][index])==False and 
                                    self.ReLu_minimals(importing['_self_'][index])==True
                                        
                                         else True
                                         for index in range(len(importing['_self_']))]
        
        importing['_friend_zone_']=[False if
                                    self.ReLu_minimals(importing['_rapport_'][index])==False and
                                    self.ReLu_minimals(importing['_flirt_'][index])==True and 
                                    importing['_last_partner_'][index]==False and
                                    importing['_prioritets_'][index]==False
                                    
                                    
                                         else True
                                         for index in range(len(importing['_self_']))]
        
        
        
        
        
        
        return importing
    
    
    
    
    
    def online(self):
        return DataFrame(self.aktivate_function( self.prediction(self.weight)))
        
    def information(self):
        return DataFrame(self.data_preprocessor(self.online())).T
    
    def prediction(self,weight):
        return np.dot(self.IN,weight)+np.random.random()
    
    def aktivate_function(self,history):
        return (history/sum(self.weight))*100
    
    def confidence_working(self,anchor,question,element_num=0):
        if question==self.limited[element_num]:
            anchor*=0.7
        element_num+=2
        if question==self.limited[element_num]:
            anchor*=1.13
        element_num+=1
        if question==self.limited[element_num]:
            anchor*=1.21
        return anchor
    
    def preprocessing_number (self,numbers):
        return [int((number*10000)/100)/100 for number in numbers]
    
    def data_preprocessor(self,local_data):
        return [self.preprocessing_number(local_data[column]) for column in local_data.columns]
               
    def normalize_float(self,items):
        normal=[item if item>0 else 0 for item in items]
        return normal
    
    def agregation(self,frame,zero=0,text='low'):
        for column in self.column_working:
            element_num=0
            if frame[column][zero]<0.40:
                text=self.limited[element_num]
            element_num+=1
                
            if frame[column][zero]>0.40:
                text=self.limited[element_num]
            element_num+=1
                
            if frame[column][zero]>0.60:
                text=self.limited[element_num]
            element_num+=1
            
            if frame[column][zero]>0.85:
                text=self.limited[element_num]
            
            frame[column][zero]=text
                
        return frame
    
    

    def ReLu_magic(self,item):
        return True if item > 0.60 else False
    
    
    def ReLu_original(self,item):
        return True if item > 0.50 else False
    
    def ReLu_minimals(self,item):
        return True if item < 0.40 else False
    
    def ReLu_millie(self,item):
        return True if item > 0.13 else False
    
    def ReLu_quarter(self,item):
        return True if item > 0.25 else False
    
    def ReLu_success(self,item):
        return True if item > 0.85 else False
    
    def ReLu_normal(self,item):
        return True if item > 0.40 else False
    
    def ReLu_unquarter(self,item):
        return True if item > 0.75 else False

def head_processing(IN):
    
    #model_starting
    
    model=Pick_Up()
    IN=model.try_me(IN)

    #model preprocession and reading
    
    preprocess_in=DataFrame(model.data_preprocessor(IN))
    preprocess_in=preprocess_in.T
    preprocess_in.columns=IN.columns
    process_in=model.data_processor(preprocess_in)
    return process_in

def _start_(IN):
    name=input('Typing girl name  -->')
    pick=Pick_Up()
    pick.IN=head_processing(IN)
    question=input('your configuration-->')
    pick.OUT=DataFrame([pop_hour(int(pick.confidence_working(int(inf),question))) for inf in pick.information()[0]])
    pick.OUT.columns=[name]
    return pick.IN, pick.OUT, name

def _finish_(inputing , outputing, name):
    inputing=[inputing[column][0] for column in inputing]
    inputing=DataFrame(inputing).T
    inputing.columns=IN.columns
    inputing=DataFrame(Pick_Up().agregation(frame=inputing))
    inputing=inputing.T
    score=outputing[name][0]
    print('&&&&&&&&&&_______~~~>||| ', str(score)+'%' ,' |||<~~~_______&&&&&&&&&&&&')
    inputing.columns=[name]
    return inputing

def pick_processors():   
    In,Out,name =_start_(IN)
    how_you =_finish_(In,Out,name)
    return how_you
    

