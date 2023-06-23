
import requests
from bs4 import BeautifulSoup
from flask import jsonify

@app.route('/api/collect_data', methods=['GET'])
def collect_data():
    #global_dict est un object global contient toutes les infos sur les trois sites
    try :
        URLs=["https://www.creditmutuel.fr/fr/particuliers/epargne/livret-de-developpement-durable.html","https://www.monabanq.com/fr/produits-bancaires/livret-developpement-durable/en-resume.html","https://www.banquepopulaire.fr/bpaura/epargner/livret-transition-energetique/"]
        global_dict = {}
        for url in URLs :
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            
            ####################Scrape du premier site##########################
            if url=="https://www.creditmutuel.fr/fr/particuliers/epargne/livret-de-developpement-durable.html":
                LDDS = {}
                keys = ['Taux', 'niveau de rémuniration', 'montant de versements', "disponibilté d'épargne"]
                all_li = soup.find('ul', {'class': 'summary__list'}).find_all('li')
                for ctr in range(len(all_li)):
                    LDDS[keys[ctr]] = all_li[ctr].find('p').text
                info_table = [{i.find('th').text : {i.find_all('td')[0].text : i.find_all('td')[1].text}} for i in soup.find('table',{'class':'noslider list'}).find_all('tr')]
                LDDS['plusieurs taux de rémunération'] = info_table
                LDDS_creditmutuel = {}
                for key, value in LDDS.items():
                    if key != 'plusieurs taux de rémunération':
                        LDDS_creditmutuel[key] = value.replace('\xa0',' ')
                    else:
                        taux_remuneration = {key: str(value).replace('\\xa0', ' ').replace(' :','') for item in LDDS['plusieurs taux de rémunération'] for key, value in item.items()}
                LDDS_creditmutuel['plusieurs taux de rémunération'] = taux_remuneration
                global_dict['LDDS_creditmutuel'] = LDDS_creditmutuel
                
            ####################Scrape du deuxième site##########################
            elif  url=="https://www.monabanq.com/fr/produits-bancaires/livret-developpement-durable/en-resume.html":
                mentions_legales = soup.find('div', class_='contain_mentions')
                strong_tag = mentions_legales.find('strong')
                liste=soup.find('section',{'class':"section-container"}).find_all('li')
                LDDR_monabanq = {}
                paragraphs = []
                for item in liste:
                    soup = BeautifulSoup(str(item), 'html.parser')
                    key = soup.find('strong').text.strip().rstrip(' :')
                    value = soup.text.replace(key, '').strip().replace('\n', ' ').replace('  ','').replace(': ','').replace('\r','')
                    LDDR_monabanq[key] = value
                next_element = strong_tag.find_next()
                while next_element and next_element.name == 'p':
                    paragraphs.append(next_element.get_text(strip=True))
                    next_element = next_element.find_next_sibling('p')
                key = strong_tag.get_text(strip=True)
                LDDR_monabanq[key]=str(paragraphs)
                LDDR_monabanq = {key: value.replace('\xa0',' ').replace('\\r\\n  ','').replace('\"','') for key, value in LDDR_monabanq.items()}
                global_dict['LDDR_monabanq'] = LDDR_monabanq

            ####################Scrape du dernier site##########################
            else:    
                LTE_banquepopulaire = {}
                for i,j in zip(soup.find('dl',{'class':'accordion-list'}).find_all('h3'),soup.find('dl',{'class':'accordion-list'}).find_all('p')):
                    LTE_banquepopulaire[i.text] = j.text
                for i in soup.find('ul',{'class':'columns is-mobile is-multiline'}).find_all('li'):
                    LTE_banquepopulaire[i.find("h3").text] = i.find("p").text
                LTE_banquepopulaire = {key: value.replace('\r\n', ' ').replace('\n',' ') for key, value in LTE_banquepopulaire.items()}
                global_dict['LTE_banquepopulaire'] = LTE_banquepopulaire

        return jsonify(global_dict),200
    except:
        return jsonify({'msg' : "Données non collectées"}),404