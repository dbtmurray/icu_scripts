import parsechessresults as parse
import bs4

def test_chessresults_individual_auto_1():
    """Parse an individual from a Chess-results saved html"""
    with open("data/belyaladya1.html") as f:
        data = f.read()
        soup = bs4.BeautifulSoup(data, 'html.parser')

        player = parse.parse_individual_auto(soup)

        assert player.name == "Dwyer,Daniel"
        assert len(player.results) == 9
        assert player.score == 4.5

def test_chessresults_individual_auto2():
    """Parse an individual from chess-results.com"""
    url = "http://chess-results.com/tnr367947.aspx?lan=1&art=9&fedb=IRL&fed=IRL&turdet=YES&flag=30&snr=42"
    event, players = parse.parse(url)
    
    assert len(players) == 1
    player = players[0]
    assert player.name == "Venkatesan,Kavin"
    assert player.score == 3.5

def test_chessresults_team1():
    """Parse many results from chess-results.com2"""
    url = "http://chess-results.com/tnr373918.aspx?lan=1&art=20&fed=IRL&flag=30"
    event, players = parse.parse(url)
    assert event == "34th European Club Cup"
    assert len(players) == 22
    assert players[0].name == "Mueller,Reinhold"
    assert players[0].score == 1.5
    assert players[-1].name == "Dunne,John P."
    assert players[-1].score == 1.0
    names = [player.name for player in players]
    assert "Kenny,William" in names

def test_chessresults_team_excel():
    """Parse many results from chess-results Excel format"""
    url = "http://chess-results.com/tnr385901.aspx?lan=1&zeilen=0&art=25&fedb=IRL&turdet=YES&flag=30&prt=4&excel=2010"
    event, players = parse.parse(url)
    assert "World Youth Chess Championships" in event
    assert len(players) == 8
    names = [player.name for player in players]
    assert "Plaza Reino,Mercedes" in names

def test_4ncl_1():
    """Parse 4ncl site"""
    url = "http://www.4nclresults.co.uk/2018-19/4ncl/1/2b/export/"
    rounds = "12"
    event, players = parse.parse(url, rounds)
    assert "4NCL" in event
    assert len(players) == 8
    assert players[0].name == "Jessel,Stephen"
    assert players[0].score == 1.0
    assert len(players[0].results) == 2




