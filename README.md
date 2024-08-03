
<h1>Fungus</h1>

<p>
General purpose Discord bot, focused on bringing functionality to your server. Ask about anything, let it remind you about scheduled tasks or check currency exchanges.
</p>
<p></p>

<img src="screenshots/avatar.png">

<!-- TOC -->

- [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Customization](#customization)
  - [Commands](#commands)
    - [help](#help)
    - [shitpost](#shitpost)
    - [whether](#whether)
    - [or](#or)
    - [exchange](#exchange)
    - [tarot](#tarot)
    - [stats](#stats)
    - [comment on](#comment_on)
- [Contributors](#contributors)

<!-- /TOC -->

## Installation

### Configuration

First, you need to obtain [Discord API](https://discord.com/developers/applications) token and [ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) of main (or #random, etc.) channel in your Discord server. You will also need to add a bot to your application and get its Application ID.

Then click `Download` and `Download ZIP` at the top of this page, or type `git clone https://github.com/TheMiczal/Fungus.git` in terminal.

Now you can copy Discord API token and channel ID to `bot.py`:

```yaml
#TOKEN
token = "token" #ENTER TOKEN HERE

#CHANNEL
main_channel = 1234567890 #ENTER MAIN CHANNEL HERE
```

Next, to add your bot to server go to <a href="https://discord.com/oauth2/authorize?client_id=APPLICATION-ID&scope=bot&permissions=8">https://discord.com/oauth2/authorize?client_id=APPLICATION-ID&scope=bot&permissions=8</a> address in your browser, substituting APPLICATION-ID with your bot's Application ID.

You probably want to further edit `bot.py` and `quotes/quotes.txt` to configure the bot to your liking.

## Usage

### Customization

Bot reacts on every chat it sees and have write access to, if message begins with `prefix` Default prefix is just `fungus`.

Configuration in `bot.py`:

Every configuration change needs a bot restart.

### Commands

Currently available commands:

- `help` - writes a brief help message
- `shitpost` - generates a random shitpost
- `whether` - tell you if its good idea
- `or` - chooses from avalible options
- `exchange` - converts between currencies
- `tarot` - draws tarot cards
- `stats` - rolls six stats for dnd
- `wait` - reminds you about something after a specified amount of time
- `comment on` - generates random words

#### help

Usage example:

```
fungus help
```

```yml
    >fungus whether X - Fungus will tell you if its good idea
    >fungus X or Y or ... - Fungus will choose
    >fungus wait X sec/min/hours text - Fungus will ping you after the time entered
    >fungus comment on X - Fungus will generate random sentence
    >fungus shitpost - Fungus will generate shitpost
    >fungus tarot X - Fungus will draw 1-6 cards
    >fungus exchange Xeur to usd - Fungus will show you current money rate. Note: Fungus uses polish api, so it converts to PLN by default.
    >fungus stats - Fungus will roll stats for your DnD character
```

#### shitpost

Usage example:

```
fungus shitpost
```

```yml
  I want to tell you that americans who cant digest lactose steal from us in order to destabilize our society and this is why our country is dying
```

Table of String tables. From each table one random element is picked, space is glued and next one is added.
Configuration in `quotes/quotes.txt`:

#### whether

Usage example:

```
fungus whether should i do something
```

```yml
  Yes
```

Configuration in `bot.py`:

```yml
responses:
    "Yes"
    "No"
    "Maybe"
    "Sometimes"
    "I don't know"
    "Try again"
    "Nah"
    "Ye"
    "idk"
    "Go away"
    fungus
```

Table of Strings. One random element is choosen as the answer.

#### or

Usage example:

```
fungus dogs or cats
```

```yml
  cats
```

#### exchange

Usage example:

```
fungus exchange 10eur to gbp 
```

```yml
  10 EUR = 8.42 GBP
```

#### tarot

Usage example:

```
fungus tarot 3
```

```yml
  Cards: The Hermit, The Moon, The Lovers
  Looks Good
```

#### stats

Usage example:

```
fungus stats
```

```yml
  [5, 4, 6, ~~2~~] = 15
  [~~1~~, 3, 6, 4] = 13
  [5, ~~3~~, 6, 3] = 14
  [~~2~~, 6, 5, 5] = 16
  [2, 6, ~~1~~, 2] = 10
  [5, ~~2~~, 3, 4] = 12
  Total: 80
```

#### wait

Usage example:

```
fungus wait 5 min do something
```

```yml
  @user do something
```


#### comment on

Usage example:

```
fungus comment on something
```

```yml
  duties presumed bathing atrociously allow colouring calling superstitious
```

## Contributors

- [Miczal](https://github.com/TheMiczal) - creator and maintainer
