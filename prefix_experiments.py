import numpy as np


def vec(x):
    return np.array(x,dtype =np.float64)
def inv(x):
    return np.linalg.inv(x)
    


prefixes ={
    #'Mol':'6.02214076e+23',
    'Q':1e30,
    'R':1e27,
    'Y':1e24,
    'Z':1e21,
    'E':1e18,
    'P':1e15,
    'T': '1000000000000',
    'G': '1000000000',
    'M': '1000000',
    'k': '1000',
    
    'c': '0.01',
    'm': '0.001',
    'μ': '0.000001',
    'n': '0.000000001',
    'p': '0.000000000001',
    'f':1e-15,
    'a':1e-18,
    'z':1e-21,
    'y': '0.000000000000000000000001',
    'r':1e-27,
    'q':1e-30,
    
    '':1,**{'*10^'+str(x)+' ':10**x  for x in range(-50,-33)}
}
superscript_map = {
    '-': "\u207b",
    '0': "\u2070",
    '1': "\u00b9",
    '2': "\u00b2",
    '3': "\u00b3",
    '4': "\u2074",
    '5': "\u2075",
    '6': "\u2076",
    '7': "\u2077",
    '8': "\u2078",
    '9': "\u2079",
    '.': "\u22C5"
}

def to_superscript(number):
    s = str(number)
    l = len(s)
    if s[l-2:l] == ".0":
        s = s[0:l-2]
    return ''.join([superscript_map[char] for char in s])

prefixes2 = {'': 1, **{'×10' + to_superscript(x) + ' ': 10**x for x in range(-46, 46)}}

prefixescon = {'':1, **{'e'+str(x)+' ':10**x  for x in range(-46,46)}}
superscript = {**{ x:to_superscript(x) for x in range(-46, 46)}}


for p in range(len(prefixes)):
    ind = list(prefixes)[p]
    prefixes[ind] = float(prefixes[ind])


#Base units are M L T A temp(K)

mlta = 5


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
    
    'm\u00b2':      vec([0,2,0,0,0]),
    'm\u00b3':      vec([0,3,0,0,0]),
    'liter':    vec([0,3,0,0,0]),
    'molarity': vec([0,-3,0,0,0]),
    'G_gravitational constant': vec([-1,3,-2,0,0]),
    
    
    'Pa':       vec([1,1-2,-2,0,0]),
    'g/m\u00b3':    vec([1,-3,0,0,0]),
    'kg/m\u00b3':   vec([1,-3,0,0,0]),
    'm/s\u00b2':    vec([0,1,-2,0,0]),
    # 's\u00b2':      vec([0,0,2,0,0]),
    'g_earth':  vec([0,1,-2,0,0]),
    'c_speed of light': vec([0,1,-1,0,0]),
    'atm' :     vec([1,1-2,-2,0,0]),
    'Density of Water':vec([1,-3,0,0,0]),
    'amu':      vec([1,0,0,0,0]),
    
    'kg/s':     vec([1,-1,0,0,0]),
    'hz':       vec([0,0,-1,0,0]),
    
    'W':        vec([1,2,-3,0,0]),
    'T_tesla': vec([1,0,-2,-1,0]),
    'C':        vec([0,0,1,1,0]),
    'V':        vec([1,2,-3,-1,0]),
    'J':        vec([1,2,-2,0,0]),
    'K':        vec([0,0,0,0,1]),
    'Ω':        vec([1,2,-3,-2,0]),
    
    'H':        vec([1,2,-2,-2,0]),
    'F':        vec([-1,-2,4,2,0]),
    'degrees':  vec([0,0,0,0,0]),
    'rotations':vec([0,0,0,0,0]),
    'pi':       vec([0,0,0,0,0]),
    'mole':     vec([0,0,0,0,0]),
    '°':        vec([0,0,0,0,0]),
    'pc':       vec([0,1,0,0,0]),
    'AU':       vec([0,1,0,0,0]),
    'earth_circumference':vec([0,1,0,0,0]),
    'R_earth':vec([0,1,0,0,0]),
    'acre':     vec([0,2,0,0,0]),
    
    'eV':       vec([1,2,-2,0,0]),
    'Å':        vec([0,1,0,0,0]),
    'Planck_length':vec([0,1,0,0,0]),
    'Planck_mass':vec([1,0,0,0,0]),
    'Planck_time':vec([0,0,1,0,0]),
    'Planck_temperature':vec([0,0,0,1,0]),
    
    
    'yard':     vec([0,1,0,0,0]),
    'Football Field':vec([0,1,0,0,0]),
    
    'lb_mass':  vec([1,0,0,0,0]),
    'mile':     vec([0,1,0,0,0]),
    'in':       vec([0,1,0,0,0]),
    'ft':       vec([0,1,0,0,0]),
    'lbf':      vec([1,1,-2,0,0]),
    'lb':       vec([1,1,-2,0,0]),
    's':        vec([0,0,1,0,0]),
    'minute':   vec([0,0,1,0,0]),
    'min':      vec([0,0,1,0,0]),
    'hour':     vec([0,0,1,0,0]),
    'hr':       vec([0,0,1,0,0]),
    'day':      vec([0,0,1,0,0]),
    'yr':       vec([0,0,1,0,0]),
    'year':     vec([0,0,1,0,0]),
    
    'Age_of_universe':vec([0,0,1,0,0]),
    
    'rpm':      vec([0,0,-1,0,0]),
    'RPM':      vec([0,0,-1,0,0]),
    'mph':      vec([0,1,-1,0,0]),
    'gallon':   vec([0,3,0,0,0]),
    'hp':       vec([1,2,-3,0,0]),
    'psi':      vec([1,1-2,-2,0,0]),
    ' ':        vec([0,0,0,0,0]),
    'Coulomb constant': vec([1,1+2,-2,0,0])-2*vec([0,0,1,1,0]),
    'ε_0':      vec([-1,-2-1,4,2,0]),
    'e':        vec([0,0,1,1,0]),
    'Btu':      vec([1,2,-2,0,0]),
    'cal':      vec([1,2,-2,0,0]),
    '°F':       vec([0,0,0,0,1]),
    'H_0':      vec([0,0,-1,0,0]),
    'mass_sun': vec([1,0,0,0,0]),
    'mass_earth': vec([1,0,0,0,0]),
    
    #'heatflux':vec([0,-1,0,0,-1])+vec([1,2,-3,0,0]),#w/m*kelvin
    #'conductivity':vec([0,-2,0,0,0])+vec([1,2,-3,0,0]),#watts/meter^2
    }




special_case_div_symbol = ['kg/s','m/s','g/m\u00b3','g/m^3','kg/m\u00b3','m/s\u00b2','m/s^2']

special_case_exponents = ['g/m\u00b3','g/m^3','kg/m\u00b3','m/s\u00b2','m/s^2']


special_case_grams = ['g','g/m\u00b3']


special_cases = {
    'g':            .001,
    'g/m\u00b3':        .001,
    'lbf':          4.44822,
    'lb':           4.44822,
    'hp':           745.7,
    'ft':           .3048,
    'lb_mass':      0.453592,
    'g_earth':      9.80665,
    'mph':          0.44704,
    'mile':         1609.34,
    'minute':       60,
    'min':          60,
    'hour':         60*60,
    'hr':           60*60,
    'day':          60*60*24,
    'year':         3.154e7,
    'yr':           3.154e7,
    'c_speed of light':299792458,
    'liter':        0.001,
    'gallon':       0.00378541,
    'Density of Water':999.8395,
    'atm':          101325,
    'psi':          6894.76,
    'degrees':      np.pi*2/360,
    '°':            np.pi*2/360,
    'rotations':    np.pi*2,
    'AU':           1.495978e11,
    'RPM':          2*np.pi/60,
    'rpm':          2*np.pi/60,
    'in':           .3048/12,
    'pi':           np.pi,
    'pc':           3.0857e16,
    'molarity':     1000*6.02214076e+23,
    'mole':         1000*6.02214076e+23,
    'eV':           1.602176634e-19,
    'G_gravitational constant': 6.67430e-11,
    'yard':         .3048*3,
    'Football Field':.3048*3*100,
    'amu':          1.66053906660e-27,
    'Coulomb constant': 8.987551e9,
    'ε_0':          8.8541878128e-12,
    'e':            1.602176634e-19,
    'Btu':          1.0551e3,
    'cal':          4.184,
    '°F':           5/9,
    'Å':            1e-10,
    'Planck_length':1.6162553e-35,
    'Planck_mass':2.176434e-8,
    'Planck_time':5.391247e-44,
    'Planck_temperature':1.416784e32,
    'acre'         :4046.8564224,
    'earth_circumference':40075000,
    'R_earth':6.37813e6,
    'H_0':1/(4.55e17),
    'Age_of_universe':4.34842e17,
    'mass_sun':1.9891e30,
    'mass_earth':5.97219e24,
    
}


imp_units = units.copy()



def addvalue(name,pre_existing_unit,value):
    for [n,p,v] in zip(name,pre_existing_unit,value):
        #print(n,p,v)
        mltav  = units[p]
        
        special_cases[n] = v
        
        units[n] = mltav
        #print(units)

addvalue(
    ['orbit_moon','slug','mass_moon'
        ],
    ['m','kg','kg'
        ],
    [384400000,14.59390,7.3476730e22
        ]
    )


badunitsforimperialdisplay = ['rotations','degrees','°', 'pi','eV','G_gravitational constant','mole','acre','m\u00b2','H_0','mass_sun','mass_earth','Age_of_universe']
for x in badunitsforimperialdisplay:
    del imp_units[x]


synonyms = {'rotations':'rot','rot':'rotation','°':'degrees','degrees':'deg','hour':'hours','yr':'years','gallon':'gallons','mile':'miles','lb_mass':'lbm','day':'days','pi':'π','s':'sec','sec':'second','liter':'L','amu':'Atomic Mass Unit','Coulomb constant':'k_e','cal':'kcal','G_gravitational constant':'G','m\u00b3':'m^3','m\u00b2':'m^2','m/s\u00b2':'m/s^2','Btu':'BTU','hour':'h'}




for s in synonyms:
    #print(s)
    
    s2 = synonyms[s]
    if s in special_cases:
        special_cases[s2] = special_cases[s]
    units[s2] = units[s]

def interms_str_imp(a,b):
    X = b
    # a = ['g','m','s','A','K']
    num = ''
    for x in range(mlta):
        if X[x] == 1:
            num += (' '+a[x]+' ×')
        elif X[x] != 0:
            num += (' '+a[x]+to_superscript(X[x])+' ×')
    if num != '':
        if num[-1]=='×':
            num = num[0:-1]

    return num

def interms_str_con(a,b):
    X = b
    # a = ['g','m','s','A','K']
    
    
    num = ''
    for x in range(mlta):
        if X[x] == 1:
            num += (''+a[x]+'⋅')
        elif X[x] != 0:
            #print(x)
            num += (''+a[x]+to_superscript(X[x])+'⋅')
    if num != '':
        if num[-1]=='⋅':
            num = num[0:-1]

    return num

unitslist = list(units.items())


unitslistsort = sorted(unitslist, key=lambda unit_: np.dot(100000+vec([1,2,3,4,5]),np.sqrt(abs(unit_[1]))-unit_[1]/10000))

for u in unitslistsort:
    u = u[0]
    mlta_ = units[u]
    st = interms_str_imp(['kg','m','s','A','K'],mlta_)
    v = 1
    if u in special_cases:
        v = special_cases[u]
    
    spacing1 = ''
    for x in range(30 - len(u)):
        spacing1 += ' '
    spacing = ''
    for x in range(30 - len(st)):
        spacing += ' '
    
    print(u+spacing1+' '+ st +' '+spacing+ str(v))







imp_unitslist = list(imp_units.items())

imp_units = {us[0].replace(' ',''):us[1] for us in imp_unitslist}




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
    
    best = 100000000000000
    prefix = ''
    # v = round(v,6)
    
    
    if v > .01 and v < 10000:
        return ''
    for p in list(prefixes2):
    
        c = prefixes2[p]
        vc = v/c
        
        
        if vc<best and vc>=.99:
            prefix = p
            best = vc+0
    return prefix

def find_p_con(v):
    
    best = 100000000000000
    prefix = ''
    # v = round(v,6)
    
    
    if v > .01 and v < 10000:
        return ''
    for p in list(prefixescon):
    
        c = prefixescon[p]
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
            num += (a[x]+'×')*int(X[x])
    if num != '':
        if num[-1]=='×':
            num = num[0:-1]
    den = ''
    for x in range(mlta):
        if X[x] < 0:
            den += (a[x]+'×')*int(-X[x])
    if den != '':
        if den[-1]=='×':
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
            return num+'/'+'('+den+')'
    

class Value:
    def __init__(self):
        
        self.original_unit = ''
        
        self.mlta_vector = vec([0,0,0,0,0])
        
        self.value = 1
        
        self.prefix = ''
    
    def set_unit(self,u_string,exponent = 1):
        
        self.original_unit = u_string
        
        self.mlta_vector = units[u_string]*exponent
        
        if u_string in special_cases:
            self.value *= special_cases[u_string]**exponent
        
        # if u_string == 'm\u00b3':
        #     self.value = self.value**(1/3)
    
    def set_prefix(self,p_string,exponent=1):
        self.prefix = p_string
        
        
        
        self.value *= prefixes[p_string]**exponent
        
        if self.original_unit == 'm\u00b3':
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
        
        # if u_string == 'm\u00b3':
        #     v = v ** (3)
        return v
    
    def in_terms_imperial(self):
        unit = ''
        
        
        
        for u in reversed(list(imp_units)):
            if (self.mlta_vector == units[u]).all():
                
                unit = u
                break
            
        return (unit)
    
    def show_in_terms_imp(self):
        u = self.in_terms_imperial()
        v = self.get_value_in_terms(u)
        if u == '':
            u = interms_str_imp(['slug','ft','s','A','K'],self.mlta_vector)
            v *= np.prod(1/vec([14.59390,0.3048,1,1,5/9])**self.mlta_vector)
            
        p = find_p_imp(v)
        v /= prefixes2[p]
        
        return str(round(v,5))+p+u
    
    def show_in_terms_con(self):
        
        #print(self.mlta_vector)
        u = interms_str_con(['kg','m','s','A','K'],self.mlta_vector+0)
        v = self.get_value_in_terms(u)
        
        
        
        p = find_p_con(v)
        
        v/= prefixescon[p]
        return str(round(v,5))+ p+' '+u
    
    def show_in_terms(self):
        
       
        u = self.in_terms_metric()
        
        v = self.get_value_in_terms(u)

        if u == '':
            u = interms_str(['kg','m','s','A','K'],self.mlta_vector)
        #print(u[0:2])
        if u[0:2] == "kg":
            #print('yes')
            u = u[1:len(u)]
            v *= 1000
        
        if u == 'm\u00b3':
            p = find_p(v**(1/3))
        elif u == 'm\u00b2':
            p = find_p(v**(1/2))
        else:
            p = find_p(v)
        
        
        v /= prefixes[p]
        
        if u == 'm\u00b3':
            v/=prefixes[p]
            v/=prefixes[p]
        elif u == 'm\u00b2':
            v/=prefixes[p]
        
        #print(round(v,5),p+u)
        return str(round(v,5))+p+u
    

import re




def break_into_terms(a):
    
    
    
    for x in units:
        if len(x) > 2 and not('/' in x) and not('^' in x):
            
            # print(x)
            # print(a)
            a = a.replace(x,' '+x+' ')
            # print(a)
    
    for x in special_case_exponents:
        a = a.replace(x,x.replace('^','exp'))
    
    for x in special_case_div_symbol:
        a = a.replace(x,x.replace('/','per'))
        
    
    #print(a)
    a = a.replace('×','*')
    a = a.replace('⋅','*')
    a = a.replace('÷','/')
    a = a.replace('to','/')
    
    
    if '/(' in a:
        #print('found grouping')
        if ')' in a:
            ap = a.split('/(')[1]
            app = ap.split(')')[0]
            
            app2 = app.replace('/','÷')
            app2 = app2.replace('*','/')
            app2 = app2.replace('÷','*')
            a = a.replace(app,app2)
            a = a.replace('/(','/')
            a = a.replace(')','')
    
    # if '[' in a:
    #     if ']^' in a:
            
    
            
    
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
        
        exponent = 1
        value_exp = 1
        
        if '^' in t:
            exp_str = t.split('^')[1]
            
            if len(exp_str)>0:
                exponent = float(exp_str)
                if ']^' in t:
                    t = t.replace(']','')
                    t = t.replace('[','')
                    value_exp = exponent
                t = t.split('^')[0]
        
        
        
        
        t = t.replace('exp','^')
        
        
        #EXTRACT NUMBER VALUE
        
        val = ''
        numstart=False
        for i in range(len(t)):
            if t[i] == '^' or t[i] == '_':
                break
            if t[i].isdigit() or t[i] == '.' or t[i] == '-' or t[i] == 'e':
                val+=t[i]
                numstart = True
            
            else:
                if numstart:
                    break
            
        if val == '':
            val = '1'
        
        terms_values[c].value = float(val)**value_exp
        
        
        
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
        
        terms_values[c].set_unit(un,exponent)
        
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
        
        terms_values[c].set_prefix(pref,exponent)
        
        
        # Invert if division
        
        if t[0] == '/':
            terms_values[c].value = 1/terms_values[c].value
            terms_values[c].mlta_vector = - terms_values[c].mlta_vector
        
        #terms_values[c].mlta_vector  *= exponent
        
        
    return terms_values
    

def mult(values):
    
    
    res = Value()
    
    for v in values:
        res.value *= v.value
        
        res.mlta_vector += v.mlta_vector
    return res
