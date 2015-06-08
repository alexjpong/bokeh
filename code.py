import web
import requests, json

render = web.template.render('templates/')

urls = (
    '/', 'index'
)

class index:
    def GET(self):
      url = "http://deckofcardsapi.com/api/deck/new/"
      new_deck = requests.get(url).json()
      deck_id = new_deck.get('deck_id')

      url_shuffle = "http://deckofcardsapi.com/api/deck/" + deck_id + "/shuffle/"
      shuffled = requests.get(url_shuffle).json().get('success')
      if shuffled:
        url_draw = "http://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=3"
        card = requests.get(url_draw).json()
        card_img = card.get('cards')[0]["image"]
        card_img2 = card.get('cards')[1]["image"]
        card_img3 = card.get('cards')[2]["image"]

        return render.index(deck_id, card_img, card_img2, card_img3)
      else:
        return render.index(deck_id)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()