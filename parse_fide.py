import sys
from collections import Counter
import xml.etree.ElementTree as ET


"""Parse FIDE rating file and get some statistics for annual report

Get FIDE file from https://ratings.fide.com/download_lists.phtml - Combined list STD, BLZ, RPD - XML format

Usage: python parse_fide.py players_list_xml_foa.xml

Takes approx 20 sec to run"""

def display(node):
    for child in node:
        print(child.tag, child.text)

def count(iterable):
    return sum(1 for i in iterable)

def has_standard_rating(player):
    return player.find("rating").text is not None

def has_blitz_rating(player):
    return player.find("blitz_rating").text is not None

def has_rapid_rating(player):
    return player.find("rapid_rating").text is not None

def has_any_rating(player):
    return has_standard_rating(player) or has_blitz_rating(player) or has_rapid_rating(player)

def is_active(player):
    flags = player.find("flag").text or ""
    return "i" not in flags

filename = sys.argv[1]
players = ET.parse(filename).getroot() # takes approx 20 sec
irish = [c for c in players if c.find("country").text == "IRL"]


print("Total FIDE players (expect approx 1,000,000)", len(players))
print("Total IRL players:", count(irish))
print("Total active IRL players:", count(p for p in irish if is_active(p)))
print("Total IRL players with standard rating", count(p for p in irish if has_standard_rating(p)))
print("Total active IRL players with standard rating", count(p for p in irish if is_active(p)
    and has_standard_rating(p)))
print("Total active IRL players with blitz rating", count(p for p in irish if is_active(p)
    and has_blitz_rating(p)))
print("Total active IRL players with rapid rating", count(p for p in irish if is_active(p)
    and has_rapid_rating(p)))
print("Total active IRL players with any rating", count(p for p in irish if is_active(p)
    and has_any_rating(p)))
print("Total active IRL players with blitz or rapid but not standard", count(p for p in irish if is_active(p)
    and has_any_rating(p) and not has_standard_rating(p)))

hist = Counter(100 * (int(p.find("rating").text) // 100) for p in irish if is_active(p)
        and has_standard_rating(p))
for k in range(700, 2700, 100):
    print("%4d\t%4d" % (k, hist.get(k, 0)))






