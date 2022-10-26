def preprocess_fn(type_: str, x: str):
    if type_ == 'lower':
        return x.lower()
    if type_ == 'lower_clean':
        return x.lower().replace('.', '').replace(',', '').replace('(', ''). \
            replace(')', '').replace('"', ' ').replace('ltd', "").replace('ооо', '')
    if type_ == 'none':
        return x
