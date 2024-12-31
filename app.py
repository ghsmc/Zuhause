from flask import Flask, render_template
import pandas as pd
import jsonify 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/policies')
def policies():
    return render_template('policies.html')

@app.route('/history')
def history():
    return render_template('history.html')
    
@app.route('/api/housing_data')
def housing_data():
    data = pd.read_json('data/housing_data.json')
    return jsonify(data.to_dict(orient="records"))

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/directory')
def directory():
    return render_template('directory.html')

@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/research')
def research():
    return render_template('research.html')


@app.route('/publications')
def publications():
    publications = [
    {
        "title": "OPEC in Vienna: Rent-free headquarters for oil billionaires",
        "author": "Die Presse",
        "date": "February 11, 2008",
        "link": "https://www.diepresse.com/362111/opec-in-wien-mietfreier-hauptsitz-fuer-oelmilliardaere"
    },
    {
        "title": "‘Housing first’: 6.6 million euros for reform of homelessness policy",
        "author": "Julia Wenzel",
        "date": "November 13, 2023",
        "link": "https://www.diepresse.com/17818151/housing-first-66-mio-euro-fuer-reform-der-wohnungslosenpolitik"
    },
    {
        "title": "How the Corona pandemic has influenced Austria's real estate market",
        "author": "Anja Hahn, Sanela Omerovic, and Sofie Waltl",
        "date": "May 8, 2023",
        "link": "https://www.diepresse.com/6284722/wie-die-corona-pandemie-oesterreichs-immobilienmarkt-beeinflusst-hat"
    },
    {
        "title": "New Airbnb rules in Vienna: What applies from July",
        "author": "Der Standard",
        "date": "2024",
        "link": "https://www.derstandard.at/story/3000000213569/alles-neu-f252r-wiener-airbnb-wohnungen"
    },
    {
        "title": "Supreme Court confirms: Airbnb banned in Vienna residential zones",
        "author": "Der Standard",
        "date": "2023",
        "link": "https://www.derstandard.at/story/2000138244773/hoechstgericht-bestaetigt-airbnb-in-wiener-wohnzonen-verboten"
    },
    {
        "title": "Vienna’s co-housing model offers a key to keeping families in the city",
        "author": "Financial Times",
        "date": "August 2024",
        "link": "https://www.ft.com/content/79726eaf-e4dd-4432-8254-a69fdc6af6e2"
    },
    {
        "title": "Segregation in Vienna: Impacts of Market Barriers and Rent Regulations",
        "source": "JSTOR",
        "date": "2014",
        "link": "https://www.jstor.org/stable/43084114"
    },
    {
        "title": "Housing First in Vienna: a socially innovative initiative to foster social cohesion",
        "source": "JSTOR",
        "date": "2015",
        "link": "https://www.jstor.org/stable/43907393"
    },
    {
        "title": "Housing - Vienna Integration Council",
        "source": "Wiener Integrationsrat",
        "date": "2020",
        "link": "https://integrationsrat.wien.gv.at/erstes_statement/wohnen"
    },
    {
        "title": "Municipal Housing Development in Vienna",
        "source": "JSTOR",
        "link": "https://www.jstor.org/stable/1017077"
    },
    {
        "title": "WHAT KIND OF PRIVATIZATION? THE CASE OF SOCIAL HOUSING IN VIENNA, AUSTRIA",
        "source": "JSTOR",
        "date": "2014",
        "link": "https://www.jstor.org/stable/43928451"
    },
    {
        "title": "The remarkable stability of social housing in Vienna and Helsinki: a multi-dimensional analysis",
        "author": "Justin Kadi",
        "date": "2022",
        "link": "https://www.tandfonline.com/doi/full/10.1080/02673037.2022.2135170"
    },
    {
        "title": "Housing in Vienna: A Socialistic Experiment",
        "source": "JSTOR",
        "link": "https://www.jstor.org/stable/2766671"
    },
    {
        "title": "“Housing needs rules” - Free tenant assistance from the City of Vienna - expert Christian Bartok in an interview",
        "source": "Stadt Wien",
        "date": "2021",
        "link": "https://www.wien.gv.at/wohnen/miete/mieterhilfe-interview.html"
    },
    {
        "title": "Housing - Vienna Integration Council",
        "source": "Wiener Integrationsrat",
        "date": "2023",
        "link": "https://integrationsrat.wien.gv.at/erstes_statement/wohnen"
    },
    {
        "title": "Introduction - Housing - Integration Monitor 2023",
        "source": "Stadt Wien",
        "date": "2023",
        "link": "https://www.wien.gv.at/spezial/integrationsmonitor/wohnen/einleitung/"
    },
    {
        "title": "New in Vienna? Everything about Housing - StartWien",
        "source": "Stadt Wien",
        "date": "2023",
        "link": "https://start.wien.gv.at/wohnen-en"
    },
    {
        "title": "The Vienna Model: A Role Model for Social Housing?",
        "source": "BUWOG Blog",
        "date": "2023",
        "link": "https://blog.buwog.com/wiener-modell-ein-vorbild-fuer-sozialen-wohnungsbau/"
    },
    {
        "title": "Topic 'Housing for Migrants' - Sozialinfo Wien",
        "source": "Sozialinfo Wien",
        "date": "2023"
    },
    {
        "title": "Why Do We Have a Housing Problem?",
        "source": "Wiener Zeitung",
        "date": "August 2023",
        "link": "https://www.wienerzeitung.at/a/warum-haben-wir-ein-wohnungsproblem"
    },
    {
        "title": "Here Live the Most Migrants in Vienna",
        "source": "Heute.at",
        "date": "November 2023",
        "link": "https://www.heute.at/s/hier-wohnen-in-wien-die-meisten-migranten-120005467"
    },
    {
        "title": "57 Percent in Public Housing Not Born in Austria",
        "source": "Heute.at",
        "date": "November 2023",
        "link": "https://www.heute.at/s/57-prozent-im-gemeindebau-nicht-in-oesterreich-geboren-120005524"
    },
    {
        "title": "Substandard, Usury, and Segregation: The Housing Situation of Foreigners in Vienna",
        "source": "dérive – Zeitschrift für Stadtforschung",
        "date": "2023",
        "link": "https://derive.at/texte/substandard-mietwucher-und-segregation-die-wohnsituation-von-auslanderinnen-in-wien/"
    },
    {
        "title": "Housing Situation and Social Integration of Turkish Migrants in Vienna",
        "source": "TU Wien",
        "date": "2021",
        "link": "https://repositum.tuwien.at/bitstream/20.500.12708/16742/1/Coskun%20Elif%20-%202021%20-%20Die%20Entwicklung%20der%20Wohnsituation%20und%20der%20sozialen...pdf"
    },
    {
        "title": "Housing Conditions in Vienna: Requirements for a Socially Integrative Housing Policy",
        "source": "wohnbauforschung.at",
        "date": "2023",
        "link": "https://www.wohnbauforschung.at/index.php?id=349"
    },
    {
        "title": "Spatial Distribution - Housing - Integration Monitor 2023",
        "source": "Stadt Wien",
        "date": "2023",
        "link": "https://www.wien.gv.at/spezial/integrationsmonitor/wohnen/raumliche-verteilung/"
    },
    {
        "title": "What Role Do Investors Play in Vienna's Housing Construction?",
        "source": "Der Standard",
        "date": "December 2020",
        "link": "https://www.derstandard.at/story/2000122040730/welche-rolle-investoren-beim-wiener-wohnbau-spielen"
    },
    {
        "title": "Many Investors in Vienna's Housing Market",
        "source": "Der Standard",
        "date": "April 2021",
        "link": "https://www.derstandard.at/story/2000125682579/viele-investoren-am-wiener-wohnungsmarkt"
    },
    {
        "title": "AK Study: More and More Investors in Vienna's Housing Market",
        "source": "Der Standard",
        "date": "June 2022",
        "link": "https://www.derstandard.at/story/2000136835136/ak-studie-immer-mehr-investoren-am-wiener-wohnungsmarkt"
    },
    {
        "title": "Real Estate Speculators: Empty Apartments Drive Up Rents in Vienna",
        "source": "Kontrast.at",
        "date": "November 2021",
        "link": "https://kontrast.at/wohnungsmarkt-wien-analyse/"
    },
    {
        "title": "Vienna's Housing Market: Success Model or Misstep?",
        "source": "Finanzfluss",
        "date": "June 2024",
        "link": "https://www.finanzfluss.de/blog/wiener-wohnungsmarkt/"
    },
    {
        "title": "Signa unravelled: inside René Benko's debt-laden property empire",
        "source": "Financial Times",
        "date": "October 2024",
        "link": "https://www.ft.com/content/31884c4d-2da7-4b43-917e-3180e9eafa3d"
    },
    {
        "title": "Austrian property tycoon René Benko files for insolvency",
        "source": "Deutsche Welle",
        "date": "November 2024",
        "link": "https://www.dw.com/en/austrian-property-tycoon-rene-benko-files-for-insolvency/a-68464903"
    }
]
    return render_template('publications.html', publications=publications)


@app.route('/card')
def card():
    return render_template('card.html')

if __name__ == '__main__':
    app.run(port=8080)
