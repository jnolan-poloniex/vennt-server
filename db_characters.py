# Josh Aaron Miller 2021
# VenntDB methods for Characters

import venntdb
from constants import *

# VenntDB Methods


def character_exists(self, username, char_id):
    return self.get_character(username, char_id) is not None


def get_character(self, username, char_id):
    self.assert_valid("accounts", username, "characters")
    if self.is_valid("accounts", username, "characters", char_id):
        return self.db["accounts"][username]["characters"][char_id]
    return None


def create_character(self, username, character, is_enemy=False):
    self.assert_valid("accounts", username, "characters")
    for attr in ATTRIBUTES:
        if attr not in character:
            character[attr] = 0
    character["items"] = []
    character["abilities"] = []
    character["is_enemy"] = is_enemy
    self.db["accounts"][username]["characters"][character["id"]] = character
    self.save_db()


def get_characters(self, username):
    self.assert_valid("accounts", username, "characters")
    return self.db["accounts"][username]["characters"]


def get_attr(self, username, char_id, attr):
    self.assert_valid("accounts", username, "characters", char_id)
    return self.get_character(username, char_id)[attr]


def set_attr(self, username, char_id, attr, val):
    self.assert_valid("accounts", username, "characters", char_id)
    self.get_character(username, char_id)[attr] = val
    self.save_db()
