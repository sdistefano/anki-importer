import sys, os
sys.path.append(os.path.join(os.getcwd(), 'anki_upstream'))

from ankisync.apkg import Apkg


file = 'ARTH200 exam.apkg'



with Apkg(file) as ankiFile:
    def add_note(front, back):
        ankiFile.add_note({
            'modelName': 'Basic',
            # 'deckId': ankiFile.deck_names_and_ids()['ARTH200 exam'],
            'deckId': 1, #default
            'order': 'H',
            'tags': 'AUTO',
            'template': 'T',
            'fields': {
                'Front': front,
                'Back': back
            }
        })
    all_cards = list(ankiFile.iter_cards())
    with open('vocab.txt') as vocab:
        vocab = vocab.read().splitlines()
        for word in vocab:
            missing = True
            for card in all_cards:
                if card['Front'].lower() == word.lower():
                    missing = False
                    break
            if missing:
                print(word)
                add_note(word, 'FILLME')

    with open('dates.txt') as dates:
        dates = dates.read().splitlines()
        for d in dates:
            date, event = filter(lambda x: x, d.split('\t'))
            print(event)
            add_note('DATE: ' + event, date)

    with open('period_dates.txt') as period_dates:
        period_dates = period_dates.read().splitlines()
        for d in period_dates:
            event, date = filter(lambda x: x, d.split('\t'))
            add_note('PERIOD: '+ event, date)

    with open('artworks.txt') as artworks:
        artworks = artworks.read().splitlines()
        for a in artworks:
            add_note('FILLME', a)
            print(a)
