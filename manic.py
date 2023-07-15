import numpy as np
from pandas import DataFrame
from pandas import read_csv

from random import random as random
from warnings import filterwarnings as message
from time import sleep

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import normalize

from sklearn.preprocessing import StandardScaler
message('ignore')
print('______====______')



from PICK_UP import *




class ManicProjection:
    
    
    def __init__(self):
        self.gender=None
        self.god=None
        self.bank=None
        self.love=None
        self.not_hurtless=None
        self.fun=None
        self.flirt=None
        self.hand_slide=None
        self.original=None
        self.not_define=None
        self.speak=None
        self.local_person=None
        self.friend=None
    
    def random_low(self,rangers):
        return np.array([np.random.randint(7,21)/100 for ranger in range(rangers)])
    
    def random_median(self,rangers):
        return np.array([np.random.randint(24,76)/100 for ranger in range(rangers)])
    
    def random_example(self,rangers):
        return np.array(np.random.random(rangers))
    
    def space(self):
        print('#################################')
        print('#################################')
        print('  ')
        
    def changer(self, intercept):
        if intercept=='low':
            return 0.25
        elif intercept=='median':
            return 0.5
        elif intercept=='high':
            return 0.75
        else:
            return 1
    
    def _name_(self):
        _name_=input("Ваше имя  -> ")
        return _name_ 

    
    def _gender_(self):
        _gender_=input("Какой пол ? ->  ")
        return True if _gender_=='парень' or _gender_=='чувак' or _gender_=='мужской' or _gender_=='мужчина' else False
    
    
    def _old_(self):
        if self.gender==True:
            print('Чел сколько тебе лет ?')
        else:
            print('Дорогая ', self.name, ' сколько тебе лет ? ')
            
        _old_=int(input())
        if _old_>19 and _old_<30:
            _old_= '1961'
            return _old_


        elif _old_>30 and _old_<45:
            _old_='high'
            return _old_


        elif _old_ >45:
            _old_='median'
            return _old_

        else:
            _old_='low'
            return _old_
    
    def _god_(self):
        _god_=input("Ты веришь в бога ? " )
        return False if _god_=='да' else True

    
    def _changer_sigmoid_(self, ask='нет'):
        return True if ask=='нет' else False
            
    def changer_sigmoid(self, ask='да'):
        return True if ask=='да' else False
    
    def _final_fantasy_(self):
        self.final_fantasy=1
        _fantasy_=input("Замечал ли ты фантастику на своем пути ? -->")  
        _history_=input("Будет ли потеря если удалить и забыть прошлые тёплые воспоминания и фото ?  -> ")
        _mifologia_=input("Можем ли мы верить в мифологию например в то что наши предки это обезьяны ?")
        _lucky_=input("У каждого своя судьба ? ")
        _horoscope_=input('Знаешь ли ты свой гороскоп... Находил ли ты интересным правду гороскопа ? -> ')
        _other_force_=input('Есть ли в мире другие силы которые не видны человеку ?')
        
        _fantasy_=self.changer_sigmoid(ask=_fantasy_)
        _history_=self.changer_sigmoid(ask=_history_)
        _mifologia_=self.changer_sigmoid(ask=_mifologia_)
        _lucky_=self.changer_sigmoid(ask=_lucky_)
        _horoscope_=self.changer_sigmoid(ask=_horoscope_)
        _other_force_=self.changer_sigmoid(ask=_other_force_)
        
        self.space()
        
        if _fantasy_ or _mifologia_:
            if self.gender:
                print('Фантазер блин ', self.name, '!')
            else:
                print(self.name, 'а ты фантазерка ')
            self.final_fantasy-=0.15
            sleep(5)
            
        else:
            if self.gender:
                print('Нормально у тебя с фантазиями чувак')
            else:
                print('Я думаю ты нормальная это в плюс ')
            sleep(5)
                
        if _lucky_ and _other_force_:
            if self.gender:
                print('Хватит искать виноватых теряешь счастье ')
            else:
                print('Не правильно думала ', self.name) 
                print('что во всем виноваты другие в поисках счастья !')
            self.final_fantasy-=0.35
            sleep(5)
            
        else:
            if self.gender:
                print('Думаю с тобой можно побазарить в хорошем смысле чел')
            else:
                print('Насколько нам ясно наркотики не употребляла в детстве' )
            sleep(5)
            
        
        if _mifologia_ and _history_ and _horoscope_:
            if self.gender:
                print('Бой с самим собой (Паша Техник)!')
            else:
                print("Выграть себя можно если не знала ")
            
            self.final_fantasy-=0.20
            sleep(5)
        
        else:
            if self.gender:
                print('Думаю хренью не занимаешься ')
            else:
                print('Оригинально в твоем случае ', self.name)
            sleep(5)
                
        if _history_ or _lucky_:
            print('Семейный человек не самое лучшее о тебе....  есть и другая сторона ->')
            self.final_fantasy-=0.15
            
        else:
            if self.gender:
                print('Нам нужны такие реалисты как ты парень ')
            else:
                print('Реалиситка если что проверенно ')
            sleep(5)
            
        
        if _horoscope_:
            if self.gender:
                print('Что решил что гороскоп тоже правду говорит ? ')
                print('Тупой чувак')
            else:
                print(' Да конечно ты проверила на себе что ')
                print('гороскоп правду говорит ', self.name)
            self.final_fantasy-=0.15
            sleep(5)
        else:
            if self.gender:
                print('Молодец ', self.name, ' за то что не увлекаешься гороскопами ')
            else:
                print('Для девушки скажу не плохо ')
            sleep(5)
                
        self.space() 
        return self.final_fantasy if self.final_fantasy>0.30 else 0
        
    def _bank_(self):
        
        money_dealer=1
        
        _bank_=self.changer_sigmoid(input('Ecть ли у тебя долг в банке -> '))
        if _bank_:
            if self.gender:
                _money_=int(input(' Сколько готов взять  ?'))
            else:
                _money_=int(input(' Сколько готова  взять ?'))
            
            if _money_>300000:
                money_dealer-=0.30
        else:
            print('Неплохо')
            
        _help_=self.changer_sigmoid(input('Хочешь помочь ближнему  ?'))
        if _help_:
            money_dealer-=0.35
        
        if self.gender:
            _money_legale_=int(input(' Сколько заработал  ?'))
        else:
            _money_legale_=int(input(' Сколько заработалa  ?'))
        if _money_legale_>self.old*19000:
            money_dealer+=0.25
        else:
            money_dealer-=0.15
            
        if self.gender:
            _money_out_=int(input('Сколько потратил не сам ?'))
        else:
            _money_out_=int(input('Сколько потратилa не самa ?'))
            
        if _money_out_<_money_legale_:
            money_dealer-=0.20
        
        self.space()
        return money_dealer if money_dealer>0.25 else False
        
        
    def _love_(self):
        if self.gender:
            _love_=self._changer_sigmoid_(input(' Влюблен ли ты ? '))
        else:
            _love_=self._changer_sigmoid_(input(' Влюбленa ли ты ? '))
        
        return _love_
    
    
    
    def _not_hurtless_(self):
        _not_hurtless_=1
        
        world_success=self.changer_sigmoid(input('Хочешь ли ты изменить мир к лучшему ? '))
        if world_success:
            if self.gender:
                print('Готов ли ты к этому ? ')
            else:
                print('Готовa ли ты к этому ? ')
            world_success=self.changer_sigmoid(input())
            if world_success:
                print('Не лезь в бассейн там пираньи ')
                _not_hurtless_-=0.19
            else:
                if self.gender:
                    print('Хорошо что ты попробовал посмотреть на это с другой стороны !')
                else:
                    print('Хорошо что ты попробовалa посмотреть на это с другой стороны !')
        else:
            print('Если бы сказал да я бы не доверял тебе ')
            print(' ')
            
        print('На сколько ты ценишь человеческую жизнь ? ')
        if self.gender:
            print('Готов ли ты пожертвовать ради нее чем либо? ')
        else:
            print('Готовa ли ты пожертвовать ради нее чем либо? ')
                
        world_success=self.changer_sigmoid(input())  
        if world_success:
            _not_hurtless_-=0.19
            
        else:
            print('Правильное рассуждение цени свое ')
            _not_hurtless_+=0.15
             
            
        world_at_war=self.changer_sigmoid(input('Хочешь ли ты прекратить все войны ?'))
        if world_at_war:
            _not_hurtless_-=0.12
            print('Суеверный ответ...')
            world_at_war=self.changer_sigmoid(input("Пожертвуешь своей жизнью для этого ?" ))
            if world_at_war:
                if self.gender:
                    print("Получается терять тебе не чего!" )
                else:
                    print('Кажется ты потеряла интерес к жизни  ')
                _not_hurtless_-=0.22
            else:
                print('Хорошо что жизнь пока осталась ценной для тебя ', self.name)
            
        else:
            print('Мои почтения и уважение ', self.name)
        
        
        return _not_hurtless_ if _not_hurtless_>0.65 else 0
            
            
    def self_crasher(self, ten=10, learning_rate=0.5):
        ask=self.changer_sigmoid(input('Будешь только правду говорить'))
        if ask:
            print('Продолжаем')
            return True
        else:
            while(True):
                ten-=learning_rate
                print('Соморазрушение через ',ten)
                sleep(learning_rate)
                if ten<1:
                    print('Пока')
                    sleep(learning_rate)
                    print('Пока')
                    sleep(learning_rate)
                    if self.gender:
                        print('Дорогой ', self.name)
                        print('Идите')
                        sleep(1)
                        print('на')
                        sleep(3)
                        print('улицу жить в матрице ')
                    else:
                        print('Дорогая  ', self.name)
                        sleep(2)
                        print('Вы были успешно посланы ')
                        sleep(2)
                        print('Пудрить носик')
                        print('Пока, Пока !!!')
                    return False   
                else:
                    continue
        
    def _your_score_(self):
        
        if self.self_crasher():
            print(' ')
        else:
            self.your_score=-10
            return self.your_score
        
        print(' ')
        sleep(2)
        print('Вариант (А) ')
        print('Мой выбор в основном совпадает с моими друзьями и я им доверяю...')
        sleep(1)
        
        print(' ')
        print('Вариант (Б) ')
        print('Готов потерять близкого человека за свое мнение...')
        sleep(1)
        
        print(' ')
        print('Вариант (В) ')
        print('Мое мнение может быть изменчиво если вопрос о счастье родных мне людей... ')
        sleep(1)
        
        print(' ')
        print('Вариант (Г) ')
        print('На деле выбор это не главное, так как главное результат успеха... ')
        print(' ')
        sleep(1)
        
        
        print('Читай и думай ')
        sleep(4)
        ask=input('Какой из вариантов про тебя ?')
        
        if ask=='Б':
            point= '1961'
        
        elif ask=='В':
            point= 'median'
        
        elif ask=='А':
            point= 'low'
        
        elif ask=='Г':
            point= 'low'
            
        else:
            point='zero_value'
            print(point)
            
        _your_score_= 0 if point=='zero_value' else self.changer(point)
        
        sleep(2)
        print('На этот раз у тебя есть шанс выбрать 2 варианта из 6-и')
        sleep(4)
        
        print('Начнём ?')
        ask=self.changer_sigmoid(input())
        
        if ask:
            sleep(2)
            print('Вариант (А) ')
            print('В этом мире есть люди без которых нету смысла жить...')
            sleep(1)
        
            print(' ')
            print('Вариант (Б) ')
            print('Нельзя быть уверенным  дело тут в везении ')
            sleep(1)

        
            print(' ')
            print('Вариант (В) ')
            print('Люди это проекции подсознания на реальность осущиствлять сознанием...')
            sleep(1)
        
            print(' ')
            print('Вариант (Г) ')
            if self.gender:
                print('Что то хуйня что это хуйня эти обе хуйни такие')
                print('что я ебал ее маму рот ?')
                
            else:
                print('Что то (..) что это (..) эти трое (..) такие что я не выберу ничего')
            
            print(' ')
            print('Вариант (Д) ')
            print('Есть в этом мире плохие и хорошие люди...')
            sleep(1)
            
            print(' ')
            print('Вариант (Е) ')
            if self.gender:
                print('Радость в деньгах и это я понял в своей жизни очень довно...')
            else:
                print('Радость в деньгах и это я поняла в своей жизни очень довно...')

            sleep(2)
            print('Напиши два варианта например АЕ ?')
            
            ask=input('--> ')
            
            

            
            if ask[0]=='А':
                point='high'
                _your_score_-=self.changer(point)
                if ask[1]=='Д':
                    if self.gender:
                        print(print('MMM...'))
                        sleep(4)
                        print('Как то женственно парень')
                        point='median'
                        _your_score_-=self.changer(point)
                    else:
                        print('Думаю разговор с какой то милой девушкой')
                        point='median'
                        _your_score_+=self.changer(point)
                        
                elif ask[1]=='Б':
                    point='low'
                    _your_score_-=self.changer(point)
                
                else:
                    point='median'
                    _your_score_-=self.changer(point)
                    
                    
            
            elif ask[0]=='Б':
                point='median'
                _your_score_-=self.changer(point)
                if ask[1]=='Д':
                    if self.gender:
                        print(print('MMM...'))
                        sleep(4)
                        print('Как то женственно парень')
                        point='median'
                        _your_score_-=self.changer(point)
                    else:
                        print('Думаю разговор с какой то милой девушкой')
                        point='median'
                        _your_score_-=self.changer(point)
                        
                        
                elif ask[1]=='Е':
                    point='high'
                    _your_score_-=self.changer(point)
                
                else:
                    point='median'
                    _your_score_-=self.changer(point)
                    
            
            elif ask[0]=='В':
                point='median'
                print('Неплохо на счет (В)')
                _your_score_+=self.changer(point)
                if ask[1]=='Е':
                    point='median'
                    if self.gender:
                        print('Есть у тебя шанс бери его пока не поздно парень хороший ответ !! ')
                        _your_score_+=self.changer(point)
                    else:
                        print('Есть у тебя шанс бери его пока не поздно детка  хороший ответ !! ')
                        _your_score_+=self.changer(point)
                        
                elif ask[1]=='Г':
                    point='1961'
                    _your_score_+=self.changer(point)
                
                else:
                    point='median'
                    _your_score_-=self.changer(point)
            
            
            
            
           
                
            
                 
                
            elif ask[0]=='В':
                point='low'
                _your_score_+=self.changer(point)
                if ask[1]=='Е':
                    print('Вижу стимул стать лучше есть у тебя')
                    sleep(1)
                    print('Но ...')
                    sleep(2)
                    if self.gender:
                        print('Есть девушка которая что то испортила в тебе')
                        point='high'
                        _your_score_-=self.changer(point)

                    else:
                        print('Смотри не разыграйся в чувствах  ')
                        point='low'
                        _your_score_+=self.changer(point)
                
                else:
                    point='median'
                    _your_score_-=self.changer(point)
                    
                    
                
            else:
                if self.gender:
                    point='median'
                    _your_score_-=self.changer(point)
                else:
                    point='low'
                    _your_score_-=self.changer(point)
            
            
            return _your_score_
        
        
        
    
       
    
    def Who_you(self):
        self.name=self._name_()
        self.gender=self._gender_()
        ask=self.changer_sigmoid(input('Напиши что нибудь -> ')) 
        if ask:
            self.old=self.random_median(rangers=1)[0]
            self.god=self.random_median(rangers=1)[0]
            self.final_fantasy=self.random_median(rangers=1)[0]
            self.bank=self.random_median(rangers=1)[0]
            self.love=True if random()>0.5 else False
            self.not_hurtless=self.random_median(rangers=1)[0]
            self.your_score=self.random_median(rangers=1)[0]
        else:
            self.old=self.changer(self._old_())
            self.god=self._god_()
            self.final_fantasy=self._final_fantasy_()
            self.bank=self._bank_()
            self.love=self._love_()
            self.not_hurtless=self._not_hurtless_()
            self.your_score=self._your_score_()


        data=DataFrame([self.gender, self.old,self.final_fantasy,
                    self.bank, self.love, self.not_hurtless, self.your_score]).T
        data.columns=['Gender','Old', 'final_fantasy', 'bank_and_money', 'love', 'not_hurtless', 'your_score_to_all']
        data.index=[self.name]
            
        return data

    
    
    def dataminer(self,pick_arguments):
        
        speak=1 if self.changer(pick_arguments.T['_rapport_'][0])>0.7 else 0
        speak=True if pick_arguments.T['_last_partner_'][0] else False
        self.speak=speak
        return [self.changer(pick_arguments.T['fun'][0]),self.changer(pick_arguments.T['_flirt_'][0]),
                self.changer(pick_arguments.T['_self_'][0]),self.changer(pick_arguments.T['_original_void_'][0]),
                pick_arguments.T['_not_define_'][0],pick_arguments.T['_local_person_'][0],
                pick_arguments.T['_friend_zone_'][0], self.speak ]

    def np_1961_predict(self,gender):
        select_columns=['fun', 'flirt','hand_slide', 'original',
            'not_define', 'speak', 'local_person','friend']
        
        if gender:
            ask=self.changer_sigmoid(input('from np_prediction__.ipynb import Pick_up ###### Импортируем _?_   '))
            if ask:
                pick_up=pick_processors()
                select_data=DataFrame(ManicProjection().dataminer(pick_up))
            else:
                select_data= DataFrame( self.random_example(rangers=len(select_columns)))
                
        else:
            print(' ')
            print(' ')
            print('Генерация данных по противоположному полу ')
            select_data= DataFrame(self.random_median(rangers=len(select_columns))) 
        
        select_data=select_data
        select_data.columns=select_columns
        if gender:
            select_data.index=['girls_config']
        else:
            select_data.index=['men_config']
        return select_data

    
    def np_1961_predict(self,pick_up=None):
        if pick_up:
            pass
        else:
            pick_up=pick_processors().T
        pick_up.values[0]=[values if type(values)==bool else ManicProjection().changer(values
                                                                    ) for values in pick_up.values[0]]
        
        
        
        
        select_columns=['fun', 'flirt','hand_slide', 'original',
            'not_define', 'speak', 'local_person','friend']

        columns=[pick_up.columns[index] for index in [0,2,4,5,6,8,-2,-1]]
        select_data=pick_up[columns]
        select_data.columns=select_columns
        return select_data
    
    
    
    def main(self, select_columns=8):
        if __name__ == "__main__":
            who_you=DataFrame(ManicProjection().Who_you())
            select_data=DataFrame(ManicProjection().np_1961_predict())
            
            return who_you,select_data


        
def df_load():
	manic=DataFrame(ManicProjection().Who_you()).values[0]
	pick_up=list(ManicProjection().np_1961_predict().values[0])
	[pick_up.append(element) for element in manic]
	df=DataFrame(pick_up).T
	
	columns=read_csv('data/learning_data.csv').drop(columns=['Unnamed: 0', 'y'], axis=1).columns
	df.columns=columns
	return df.astype('float16')



           
            
            
            
            
            
            
