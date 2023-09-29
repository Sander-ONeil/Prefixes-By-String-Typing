import numpy as np


def vec(x):
    return np.array(x,dtype =np.float64)
def inv(x):
    return np.linalg.inv(x)

prefixes ={
    'Mol':'6.02214076e+23',
    'T': '1000000000000',
    'G': '1000000000',
    'M': '1000000',
    'k': '1000',
    
    'c': '0.01',
    'm': '0.001',
    'μ': '0.000001',
    'n': '0.000000001',
    'p': '0.000000000001',
    'y': '0.000000000000000000000001',
    '':1,
}

prefixes2 = {'':1, **{'*10^'+str(x)+' ':10**x  for x in range(-10,10)}}

for p in range(len(prefixes)):
    ind = list(prefixes)[p]
    prefixes[ind] = float(prefixes[ind])


#Base units are M L T A temp(K)

mlta = 5

special_case_div_symbol = ['kg/s','m/s','g/m^3','kg/m^3','m/s^2']

units =  {
    '':         vec([0,0,0,0,0]),
    'g':        vec([1,0,0,0,0]),
    'kg':       vec([1,0,0,0,0]),
    'm':        vec([0,1,0,0,0]),
    'N':        vec([1,1,-2,0,0]),
    's':        vec([0,0,1,0,0]),
    'A':        vec([0,0,0,1,0]),
    'K':        vec([0,0,0,0,1]),
    'm/s':      vec([0,1,-1,0,0]),
    'm^3':      vec([0,3,0,0,0]),
    'liter':    vec([0,3,0,0,0]),
    
    
    'Pa':       vec([1,1-2,-2,0,0]),
    'g/m^3':    vec([1,-3,0,0,0]),
    'kg/m^3':   vec([1,-3,0,0,0]),
    'm/s^2':    vec([0,1,-2,0,0]),
    's^2':      vec([0,0,2,0,0]),
    'g_earth':  vec([0,1,-2,0,0]),
    'c (speed of light)': vec([0,1,-1,0,0]),
    'atm' :     vec([1,1-2,-2,0,0]),
    'Density of Water':vec([1,-3,0,0,0]),
    
    'kg/s':     vec([1,-1,0,0,0]),
    'hz':       vec([0,0,-1,0,0]),
    
    'W':        vec([1,2,-3,0,0]),
    'T(tesla)': vec([1,0,-2,-1,0]),
    'C':        vec([0,0,1,1,0]),
    'V':        vec([1,2,-3,-1,0]),
    'J':        vec([1,2,-2,0,0]),
    'K':        vec([0,0,0,0,1]),
    'Ω':        vec([1,2,-3,-2,0]),
    
    'H':        vec([1,2,-2,-2,0]),
    'F':        vec([-1,-2,4,2,0]),
    'degrees':  vec([0,0,0,0,0]),
    'rotations':vec([0,0,0,0,0]),
    'AU':       vec([0,1,0,0,0]),
    
    'lb_mass':  vec([1,0,0,0,0]),
    'mile':     vec([0,1,0,0,0]),
    'in':       vec([0,1,0,0,0]),
    'ft':       vec([0,1,0,0,0]),
    'lbf':      vec([1,1,-2,0,0]),
    'lb':      vec([1,1,-2,0,0]),
    's':        vec([0,0,1,0,0]),
    'minute':   vec([0,0,1,0,0]),
    'hour':     vec([0,0,1,0,0]),
    'day':      vec([0,0,1,0,0]),
    'year':     vec([0,0,1,0,0]),
    'RPM':      vec([0,0,-1,0,0]),
    'mph':      vec([0,1,-1,0,0]),
    'gallon':   vec([0,3,0,0,0]),
    'hp':       vec([1,2,-3,0,0]),
    'psi':      vec([1,1-2,-2,0,0]),
    
    
    
    
    
    
    
    
    #'heatflux':vec([0,-1,0,0,-1])+vec([1,2,-3,0,0]),#w/m*kelvin
    #'conductivity':vec([0,-2,0,0,0])+vec([1,2,-3,0,0]),#watts/meter^2
    }

special_case_grams = ['g','g/m^3']


special_cases = {'g':.001,'g/m^3':.001,'lbf':4.44822,'lb':4.44822,
    'hp':745.7,'ft':.3048,'lb_mass':0.453592,'g_earth':9.80665,'mph':.44704,'mile':1609.34,
    'minute':60,'hour':60*60,'day':60*60*24,'year':3.154*10**7, 'c (speed of light)':299792458,'liter':0.001,'gallon':0.00378541,'Density of Water':999.8395,'atm':101325,'psi':6894.76,'degrees':0.0174533,'rotations':np.pi*2,'AU':1.495978*10**11,'RPM':0.15915,'in':.3048/12,
}

unitslist = list(units.items())

units = {us[0].replace(' ',''):us[1] for us in unitslist}
special_cases_list = list(special_cases.items())

special_cases = {us[0].replace(' ',''):us[1] for us in special_cases_list}

def get_len(key):
    return -len(key[0])
test_dict = units
 
# sorting using sort()
# external to render logic
test_dict_list = list(test_dict.items())
test_dict_list.sort(key = get_len)
 
# reordering to dictionary
res = {ele[0] : ele[1]  for ele in test_dict_list}

def find_p(v):
    
    best = 100000000000000
    prefix = ''
    
    if v > .01 and v < 1000:
        return ''
    for p in list(prefixes):
    
        c = prefixes[p]
        vc = v/c

        if vc<best and vc>=.99:
            prefix = p
            best = vc+0
    return prefix

def find_p_imp(v):
    print('***************',v)
    best = 100000000000000
    prefix = ''
    # v = round(v,6)
    
    
    if v > .01 and v < 10000:
        return ''
    for p in list(prefixes2):
    
        c = prefixes2[p]
        vc = v/c
        
        #print('v',v,'c',c,'vc',vc,'best',best,'p',p)
        if vc<best and vc>=.99:
            prefix = p
            best = vc+0
    return prefix

def interms_str(a,b):
    X = b
    # a = ['g','m','s','A','K']
    num = ''
    for x in range(mlta):
        if X[x] > 0:
            num += (a[x]+'*')*int(X[x])
    if num != '':
        if num[-1]=='*':
            num = num[0:-1]
    den = ''
    for x in range(mlta):
        if X[x] < 0:
            den += (a[x]+'*')*int(-X[x])
    if den != '':
        if den[-1]=='*':
            den = den[0:-1]
    if num == '':
        if den == '':
            return''
        else:
            return '1/'+den
    else:
        if den =='':
            return num
        else:
            return num+'/'+den
    
def interms_str_imp(a,b):
    X = b
    # a = ['g','m','s','A','K']
    num = ''
    for x in range(mlta):
        if X[x] == 1:
            num += (a[x]+' *')
        if X[x] != 0:
            num += (' '+a[x]+'^'+str(int(X[x]))+' *')
    if num != '':
        if num[-1]=='*':
            num = num[0:-1]

    return num

class Value:
    def __init__(self):
        
        self.original_unit = ''
        
        self.mlta_vector = vec([0,0,0,0,0])
        
        self.value = 1
        
        self.prefix = ''
    
    def set_unit(self,u_string):
        
        self.original_unit = u_string
        
        self.mlta_vector = units[u_string]
        
        if u_string in special_cases:
            self.value *= special_cases[u_string]
        
        # if u_string == 'm^3':
        #     self.value = self.value**(1/3)
    
    def set_prefix(self,p_string):
        self.prefix = p_string
        
        
        
        self.value *= prefixes[p_string]
        
        if self.original_unit == 'm^3':
            self.value *= prefixes[p_string]
            self.value *= prefixes[p_string]
        
    def show(self):
        
        print(self.value,self.prefix,self.original_unit,'     ',self.mlta_vector)

    def in_terms_metric(self):
        unit = ''
        for u in list(units):
           
            if (self.mlta_vector == units[u]).all():
                
                unit = u
                break
            
        return (unit)
        
    def get_value_in_terms(self,u_string):
        
        v = self.value+0
        
        if u_string in special_cases:
            v /= special_cases[u_string]
        
        # if u_string == 'm^3':
        #     v = v ** (3)
        return v
    
    def in_terms_imperial(self):
        unit = ''
        
        for u in reversed(list(units)):
           
            if (self.mlta_vector == units[u]).all():
                
                unit = u
                break
            
        return (unit)
    
    def show_in_terms_imp(self):
        u = self.in_terms_imperial()
        v = self.get_value_in_terms(u)
        if u == '':
            u = interms_str_imp(['slug','ft','s','A','K'],self.mlta_vector)
            v *= np.prod(vec([14.59390,0.3048,1,1,5/9])**self.mlta_vector)
            
        p = find_p_imp(v)
        v /= prefixes2[p]
        
        return str(round(v,5))+p+u
    
    def show_in_terms(self):
        
       
        u = self.in_terms_metric()
        
        v = self.get_value_in_terms(u)

        if u == '':
            u = interms_str(['g','m','s','A','K'],self.mlta_vector)
        
        if u == 'm^3':
            p = find_p(v**(1/3))
        else:
            p = find_p(v)
        
        
        v /= prefixes[p]
        
        if u == 'm^3':
            v/=prefixes[p]
            v/=prefixes[p]
        
        #print(round(v,5),p+u)
        return str(round(v,5))+p+u
    

import re

def break_into_terms(a):

    for x in special_case_div_symbol:
        a = a.replace(x,x.replace('/','per'))
        
    terms=[]
    for e in a.split('*'):
        if e:
            terms.append('*' + e.split('/')[0])
    
    spldiv = a.split('/')
    
    for e in spldiv[1:len(spldiv)]:
        if e:
            terms.append('/' + e.split('*')[0])
    
    for t in range(len(terms)):
        terms[t] = terms[t].replace(' ', '')
        terms[t] = terms[t].replace('per','/')
    return terms

def convert(terms):
    
    
    terms_values = ['']*len(terms)
    
    for c, t in enumerate(terms):
        
        terms_values[c] = Value()
        
        #EXTRACT NUMBER VALUE
        
        val = ''
        numstart=False
        for i in range(len(t)):
            if t[i] == '^':
                break
            if t[i].isdigit() or t[i] == '.':
                val+=t[i]
                numstart = True
            
            else:
                if numstart:
                    break
            
        if val == '':
            val = '1'
        
        terms_values[c].value = float(val)
        
        
        
        # UNITS
        
        un = ''
        for u in range(len(res)):
            
            key = list(res)[u]
            
            t_l = len(t)
            
            k_l = len(key)
            
            
            if t[t_l-k_l:t_l] == key and k_l >= 1:
                
                un = key
                t = t[0:t_l-k_l]
                break
        
        terms_values[c].set_unit(un)
        
        pref = ''
        
        #extract prefix
        
        for u in range(len(prefixes)):
            
            key = list(prefixes)[u]
            
            t_l = len(t)
            
            k_l = len(key)
            
            if t[t_l-k_l:t_l] == key:
                
                pref = key
                t = t[0:t_l]
                break
        
        terms_values[c].set_prefix(pref)
        
        
        # Invert if division
        
        if t[0] == '/':
            terms_values[c].value = 1/terms_values[c].value
            terms_values[c].mlta_vector = - terms_values[c].mlta_vector
        
    return terms_values
    

def mult(values):
    
    
    res = Value()
    
    for v in values:
        res.value *= v.value
        
        res.mlta_vector += v.mlta_vector
    return res



terms = break_into_terms('30 m/s * 40 ms * 50 g * 500lb')
terms_values = convert(terms)

for x in terms_values:
    x.show()


RESULT = mult(terms_values)
    
RESULT.show_in_terms()

