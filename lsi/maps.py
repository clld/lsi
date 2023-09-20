from clld.web.maps import ParameterMap


class WordMap(ParameterMap):
    def get_options(self):
        return {
            'show_labels': True,
            'hash': False,
        }


def includeme(config):
    config.register_map('parameter', WordMap)
