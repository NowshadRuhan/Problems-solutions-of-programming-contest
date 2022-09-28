class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password)<8:
            return False
        lowercase = 0
        uppercase = 0
        digit = 0
        special_character = 0
        sp = '!@#$%^&*()-+'
        checker1 = '-1'
        checker2 = '-1'
        for i in password:
            if i.isupper():
                uppercase = 1
            elif i.islower():
                lowercase = 1
            elif i in sp:
                special_character = 1
            elif i.isdigit():
                digit = 1
            elif i :
                digit = 1
            
            
            if i != checker1 and checker1 != 1:
                checker2 = i
                checker1 = 1
                continue
            elif checker1 == 1:
                if i == checker2:
                    checker2 = i
                    return False
                checker2 = i
                
            
        if uppercase ==1 and lowercase == 1 and special_character == 1 and digit == 1:
            return True
        else:
            return False
            
        