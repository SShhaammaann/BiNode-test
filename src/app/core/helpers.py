# from dnd.character.lib import create_character, create_char_class, create_char_race
# from dnd.character.models import CharacterRace, CharacterClass, Character
# from dnd.game.lib import Dice
#
#
# def fill_db_with_sample_data():
#     if not Character.query.filter_by(name='Vasya Pupkin').first() and\
#        not CharacterRace.query.filter_by(name='Human').first() and\
#        not CharacterClass.query.filter_by(name='Warrior'):
#         race_dict = {
#             'name': 'Human',
#             'aging_rules': 'Regular',
#         }
#         class_dict = {
#             'name': 'Warrior',
#             'hit_die': '1d8',
#             'hit_points_lvl1': '1d20',
#             'hit_points_consequent': '1d8',
#             'proficiencies': 'Doing things',
#             'spellcasting': 'Casting spells is fun!',
#         }
#         create_char_race(race_dict)
#         create_char_class(class_dict)
#         race_id = CharacterRace.query.filter_by(name='Human').first().id
#         class_id = CharacterClass.query.filter_by(name='Warrior').first().id
#         char_dict = {
#             'name': 'Vasya Pupkin',
#             'age': '22',
#             'height': '160cm',
#             'weight': '60kg',
#             'eyes': 'red',
#             'skin': 'red',
#             'hair': 'red',
#             'backstory': "He's just a regular red-skinned man.",
#         }
#         stats_dict = {
#             # Saving throws
#             'strength': Dice.roll(8),
#             'dexterity': Dice.roll(8),
#             'constitution': Dice.roll(8),
#             'intelligence': Dice.roll(8),
#             'wisdom': Dice.roll(8),
#             # Skills
#             'acrobatics': Dice.roll(8),
#             'animal_handling': Dice.roll(8),
#             'arcana': Dice.roll(8),
#             'athletics': Dice.roll(8),
#             'deception': Dice.roll(8),
#             'history': Dice.roll(8),
#             'insight': Dice.roll(8),
#             'intimidation': Dice.roll(8),
#             'investigation': Dice.roll(8),
#             'medicine': Dice.roll(8),
#             'nature': Dice.roll(8),
#             'perception': Dice.roll(8),
#             'performance': Dice.roll(8),
#             'persuasion': Dice.roll(8),
#             'religion': Dice.roll(8),
#             'sleight_of_hand': Dice.roll(8),
#             'stealth': Dice.roll(8),
#             'survival': Dice.roll(8),
#             # Other stats
#             'proficiency_bonus': Dice.roll(8),
#             'inspiration': Dice.roll(8),
#             'initiative': Dice.roll(8),
#             'level': Dice.roll(8),
#             'experience': Dice.roll(8),
#             'encumbrance': Dice.roll(8),
#             'passive_perception': Dice.roll(8),
#         }
#         create_character(char_dict, stats_dict, race_id, class_id)
