"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='http://localhost:5000/hello'>go to hello page</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <label for="compliment">Choose a compliment to yourself:</label>
          <select name="compliment-selected" id="compliment">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="fantastic">Fantastic</option>
            <option value="neato">Neato</option>
            <option value="fantabulous">Fantabulous</option>
            <option value="wowza">Wowza</option>
            <option value="oh-so-not-meh">Oh-so-not-meh</option>
            <option value="brilliant">Brilliant</option>
            <option value="ducky">Ducky</option>
            <option value="coolio">Coolio</option>
            <option value="incredible">Incredible</option>
            <option value="wonderful">Wonderful</option>
            <option value="smashing">Smashing</option>
            <option value="lovely">Lovely</option>
          </select>          
          <input type="submit" value="Submit">
        </form>

        <form action="/diss">
          <lable for="generate-quote">Click on the button bellow to generate a sarcastic quote</lable>
          <button type="submit">Click me</button>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment-selected")    

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route("/diss")
def insult():
    """Display user insults"""

    quotes = ["I’m sorry I hurt your feelings when I called you stupid. I really thought you already knew.", "I’m not insulting you. I’m describing you.", "It’s ok if you disagree with me. I can’t force you to be right.", "I’m actually not funny. I’m just mean and people think I’m joking.", "If you don’t want a sarcastic answer, don’t ask a stupid question.", "I’m busy right now, can I ignore you some other time?", "I was wondering how you comb your hair so the horns don’t show.", "I love rumors. I always find out amazing things about myself I never knew."]
    
    
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        {choice(quotes)}        
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
