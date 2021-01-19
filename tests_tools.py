import unittest
from quick_tools import verify_room_type
from quick_tools import verify_user_password
import random
import string

class QuickToolsTester(unittest.TestCase):

  def test_verify_room_type(self):

    #room_type is ‘public’ or ‘private’

    ############### ASSERT FALSE ###############

    # non vide
    self.assertFalse(verify_room_type('')) 

    # pas de majuscule
    self.assertFalse(verify_room_type('Public')) 
    self.assertFalse(verify_room_type('Private')) 

    # pas d'espace
    self.assertFalse(verify_room_type('public private')) 
    self.assertFalse(verify_room_type(' public')) 
    self.assertFalse(verify_room_type('private ')) 

    # pas de chiffre
    self.assertFalse(verify_room_type('private123')) 

    # pas le bon nommage
    self.assertFalse(verify_room_type('priv')) 
    self.assertFalse(verify_room_type('pub'))  

    ############### ASSERT TRUE ###############

    # reponse correcte
    self.assertTrue(verify_room_type('public'))
    self.assertTrue(verify_room_type('private'))


  def test_verify_user_password(self):

    #user password is > 8 chars, includes numbers and at least a special character

    ############### ASSERT FALSE ###############

    # mot de passe sans de nombre, ni caracteres speciaux 
    self.assertFalse(verify_user_password('abcdefghe')) 
    self.assertFalse(verify_user_password('abcdef345'))
    self.assertFalse(verify_user_password('abcdef34'))

    # mot de passe sans caracteres speciaux
    self.assertFalse(verify_user_password('123456789'))

    # mot de passe trop court (<9)
    self.assertFalse(verify_user_password('abcdefgh'))
    self.assertFalse(verify_user_password('abc#[]()')) 
    self.assertFalse(verify_user_password('12345678')) 
    self.assertFalse(verify_user_password('@"[]!()#')) 
    self.assertFalse(verify_user_password('345#[]()')) 
    
    # mot de passe sans chiffres
    self.assertFalse(verify_user_password('@"[]!()#*;:~'))
    self.assertFalse(verify_user_password('abc#[@)"`')) 

    # mot de passe avec espace
    self.assertFalse(verify_user_password('!12ab cdef')) 
    self.assertFalse(verify_user_password(' !12abcdef ')) 


    ############### ASSERT TRUE ###############

    # mot de passe correcte
    self.assertTrue(verify_user_password('!12abcdef')) 
    self.assertTrue(verify_user_password('*87393jdnfef'))
    self.assertTrue(verify_user_password('|=7393JDNHFG')) 
    self.assertTrue(verify_user_password('#12345678_'))
    self.assertTrue(verify_user_password('345#[@)"`')) 



  

