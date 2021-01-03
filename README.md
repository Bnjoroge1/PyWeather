<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="Bot logo"></a>
</p>

<h3 align="center">PyWeather</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 Terminal Application.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

PyWeather scrapes weaher data from various sources, in multiple timeline and presents them on the screen

## 💭 How it works <a name = "working"></a>

The scraper first extracts the word from the command line arguments and then checks to see if the arguments passed are optional or mandatory(e.g day is a mandatory argument while humidity is not). 
After the verification,  arguments are used a  key parameters in thethe request call to a specificied website. For instance for [weather.com](https://weather.com), the request arguments are used. The blocking scraper, a html parser, built using Beautiful soup scours the DOM Of the Website and searches for the weather of that day and that specified location. 
 
The data is then returned and string manipulation is perfomed on it to convert it to a stream of bytes, and convert the temperature to the appropriate uit(i.e Fahreneit or Celcius)
  part of speech, example and source from the Oxford Dictionary API.

If the arguments does not exist in the Oxford Dictionary, the scraper then returns a 404 response upon which it retries the request form the selected parser.

The bot uses the Pushshift API to fetch comments, PRAW module to reply to comments and Heroku as a server.

The entire bot is written in Python 3.6

## 🎈 Usage <a name = "usage"></a>

To use the scraper, run:

```
python3 -m PyWeatehr -u (insert preferred unit of measurment) -a (insert the specific area code of the location you want the weather from) -p (the parser that you are using to scrape the data) -td (timeframe for the data fetch)
```

We are running PyWeather as a module, so our __main__file is our entry point to the project. The other flags are necessary to be used as arguments in the request call. 

For a more complete guide on the arguments, especially the required ones and teh temporary ones, please run :

```
Python3 -m Pyweather --help
```


## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them.

```
> Python3.6
Beautiful Soup 
Selenium
PhantomJS
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
mkdir && cd {name of dir}
virtualenv {name of virtual env}

cd etc/path/to/virtualenv/bin && source activate
```
Once you've activated the virtualenv, and forked the project, run the below to clone ths repo. Use the appropriate command if using Github CLI
```
git clone https://github.com/Bnjorogedev/PyWeather-cli
pip install -r requirements.txt

python3 -m PyWeather --help
```
## ⛏️ Built Using <a name = "built_using"></a>

- [Beautiful Soup](https://praw.readthedocs.io/en/latest/) - Python Reddit API Wrapper
- [Selenium](https://www.heroku.com/) - SaaS hosting platform
- [Requests](https://requests.com)
- [PhantomJS](https://phantomjs.org)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
