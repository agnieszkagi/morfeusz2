#! python3
import re
import morfeusz2


def Decline_Noun(keyword, case):
    ''' Decline nouns '''
    result = ""
    morf = morfeusz2.Morfeusz()
    list_of_morphosyntactic_forms = morf.generate(keyword)
    if case == 'nom':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:nom" in element:
                    result = tuple[0]
    elif case == 'gen':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:gen" in element:
                    result = tuple[0]
    elif case == 'dat':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:dat" in element:
                    result = tuple[0]
    elif case == 'acc':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:nom.acc" in element:
                    result = tuple[0]
                elif "subst:sg:acc" in element:
                    result = tuple[0]
    elif case == 'inst':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:inst" in element:
                    result = tuple[0]
    elif case == 'loc':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:loc" in element:
                    result = tuple[0]
    return result


def Get_Case(keyword):
    ''' Returns case '''
    morf = morfeusz2.Morfeusz()
    list_of_morphosyntactic_forms = morf.analyse(keyword)
    element = list_of_morphosyntactic_forms[0][2][2]
    case = element.split(':')[2].split('.')[0]
    return case

print(Decline_Noun("sonda", Get_Case("pływaka")))
