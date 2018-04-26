import re

index_words = {
    'de' : [
        (r'maßgebliche(?:r|n)?\s+und\s+begründete(?:r|n)\s+(?:einspruch|einsprüche)', 'maßgeblicher-und-begründeter-einspruch'),
        (r'verbindliche(?:n)?\s+interne(?:n)?\s+datenschutzvorschriften', 'verbindliche-interne-datenschutzvorschriften'),
        (r'dienst(?:e|en)?\s+der\s+informationsgesellschaft', 'dienst-der-informationsgesellschaft'),
        (r'technische(?:n)?\s+und\s+organisatorische(?:n)?\s+maßnahme(?:n)?', 'technische-und-organisatorische-maßnahmen'),
        (r'verletzung\s+des\s+schutzes\s+personenbezogene(?:n|r)?\s+daten', 'verletzung-des-schutzes-personenbezogener-daten'),
        (r'personenbezogene(?:n|r)?\s+daten', 'personenbezogene-daten'),
        (r'internationale\s+organisation(?:en)?', 'internationale-organisation'),
        (r'betroffene(?:n|r)?\s+person(?:en)?', 'betroffene-person'),
        (r'natürliche(?:n|r)?\s+person(?:en)?', 'natürliche-person'),
        (r'teilautomatisierte(?:r|n)?\s+Verarbeitung', 'teilautomatisierte-verarbeitung'),
        (r'automatisierte(?:r|n)\s+Verarbeitung', 'automatisierte-verarbeitung'),
        (r'grenzüberschreitende(?:r|n)\s+Verarbeitung(?:en)?', 'grenzüberschreitende-verarbeitung'),
        (r'einschränkung\s+der\s+verarbeitung', 'einschränkung-der-verarbeitung'),
        (r'verarbeitung', 'verarbeitung'),
        (r'verordnung', 'verordnung'),
        (r'aufsichtsbehörde(?:n)?', 'aufsichtsbehörde'),
        (r'teilautomatisierte(?:r|n)?\s+Verfahren', 'teilautomatisiertes-verfahren'),
        (r'automatisierte(?:r|n)\s+Verfahren', 'automatisiertes-verfahren'),
        (r'verfahren', 'verfahren'),
        (r'vertreter', 'vertreter'),
        (r'unternehmen', 'unternehmen'),
        (r'unternehmensgruppe', 'unternehmensgruppe'),
        (r'auftragsverarbeiter(?:s)?', 'auftragsverarbeiter'),
        (r'identifizierte(?:n|r)?', 'identifiziert'),
        (r'verarbeitungstätigkeit(?:en)?', 'verarbeitungstätigkeit'),
        (r'empfänger', 'empfänger'),
        (r'dritte(?:r|n)?', 'dritter'),
        (r'einwilligung(?:en)?', 'einwilligung'),
        (r'genetische\s+daten', 'genetische-daten'),
        (r'biometrische\s+daten', 'biometrische-daten'),
        (r'gesundheitsdaten', 'gesundheitsdaten'),
        (r'dateisystem(?:en|e)?', 'dateisystem'),
        (r'identifizierbar(?:en|er|e)?', 'identifizierbar'),
        (r'Profiling(?:s)?', 'profiling'),
        (r'verantwortliche(?:r|n)?', 'verantwortlicher'),
        (r'natürliche(?:n|r)?\s+Person(?:en)?', 'natuerliche-person'),
        (r'pseudonymisierung', 'pseudonymisierung'),
        (r'pseudonymisierte(?:n|r)?', 'pseudonymisierung'),
        (r'pseudonymisieren', 'pseudonymisierung'),
        (r'anonymisierung', 'anonymisierung'),
        (r'anonymisierte(?:n|r)?', 'anonymisierung'),
        (r'anonymisieren', 'anonymisierung'),
    ],
    'en' : [
        (r'personal\s+data', 'personal-data'),
        (r'restriction\s+of\s+processing', 'restriction-of-processing'),
        (r'cross-border\s+processing', 'cross-border-processing'),
        (r'processing', 'processing'),

        (r'pseudonymisation', 'pseudonymisation'),
        (r'pseudonymised(?:n|r)?', 'pseudonymisation'),
        (r'pseudonymise', 'pseudonymisation'),
        (r'anonymisation', 'anonymisation'),
        (r'anonymised?', 'anonymisation'),
        (r'anonymise', 'anonymisation'),
        (r'filing\s+system', 'filing-system'),
        (r'controller', 'controller'),
        (r'processor', 'processor'),
        (r'recipient', 'recipient'),
        (r'third\s+party', 'third-party'),
        (r'consent', 'consent'),
        (r'personal\s+data\s+breach', 'personal-data-breach'),
        (r'genetic\s+data', 'genetic-data'),
        (r'biometric\s+data', 'biometric-data'),
        (r'data\s+concerning\s+health', 'data-concerning-health'),
        (r'representative', 'representative'),
        (r'enterprise', 'enterprise'),
        (r'group\s+of\s+undertakings', 'group-of-undertakings'),
        (r'binding\s+corporate\s+rules', 'binding-corporate-rules'),
        (r'supervisory\s+authority', 'supervisory-authority'),
        (r'cross\s+border\s+processing', 'cross-border-processing'),
        (r'relevant\s+and\s+reasoned\s+objection', 'relevant-and-reasoned-objection'),
        (r'information\s+society\s+service', 'information-society-service'),
        (r'international\s+organisation', 'international-organisation'),
        (r'natural\s+person(?:s)?', 'natural-person'),
        (r'regulation', 'regulation'),
        (r'automated\s+means', 'automated-means'),
        (r'data\s+subject', 'data-subject'),
        (r'identifiable', 'identifiable'),
        (r'identified', 'identified'),
        (r'profiling', 'profiling'),
        (r'technical\s+and\s+organisational\s+measures', 'technical-and-organisational-measures'),
    ]
}

def crawl_result(result, keys=None):
    if keys is None:
        keys = []
    for key, value in list(result.items()):
        if isinstance(value, str):
            yield keys, key, value, result
        elif isinstance(value, dict):
            for res in crawl_result(value, keys + [key]):
                yield res

def build_index(result, language):

    def sub(match, keys, index, index_value):
        index.add(index_value)
        return r'{{{}|index:{}}}'.format(match.group(0), index_value)

    compiled_index_words = {}
    global_index = {}
    for (key, values) in index_words[language]:
        regex_str = r'(?<![\{{a-z])({}(?=[\.\n\s\;\,\„\“\‘\’]|$))'.format(key)
        compiled_index_words[re.compile(regex_str, re.I | re.S)] = values
    for keys, key, value, parent in crawl_result(result):
        local_index = set()
        for index_word, index_value in compiled_index_words.items():
            value = index_word.sub(lambda x: sub(x, keys=keys, index=local_index, index_value=index_value), value)
        parent[key] = value
        if local_index:
            parent['index'] = list(local_index)
            full_key = [k for k in keys]+[key]
            for index_word in local_index:
                if not index_word in global_index:
                    global_index[index_word] = []
                global_index[index_word].append(full_key)
    return global_index
