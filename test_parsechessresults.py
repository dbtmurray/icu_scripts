import parsechessresults as parse
import bs4

with open("data/belyaladya1.html") as f:
    data = f.read()
    soup = bs4.BeautifulSoup(data, 'html.parser')

    player = parse.parse_individual_auto(soup)

    assert player.name == "Dwyer,Daniel"
    assert len(player.results) == 9
    assert player.score == 4.5

