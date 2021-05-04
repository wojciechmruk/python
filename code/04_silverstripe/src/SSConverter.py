# Silverstripe # convert __ss_environment.php to .env
import re


class SSConverter:
    def __init__(self, text):
        self.text_comment = '';
        self.text = text
        self.php_start()
        self.base_url()
        self.comment()
        self.define()
        self.php_elements()

    def regex(self, regex_search_term, regex_replacement, args):
        self.text = re.sub(regex_search_term, regex_replacement, args)

        return self.text

    def base_url(self):
        base_url = input('Provide base url:')
        self.text = 'SS_BASE_URL="' + base_url + '"\n' + self.text

        return self.text

    def php_start(self):
        search_term = re.compile(r'^<\?php')
        self.text = self.regex(search_term, '', self.text)

        return self.text

    def comment(self):
        search_term = re.compile('\n//')
        replacement = '\n#'

        self.text = self.regex(search_term, replacement, self.text)

        return self.text

    def define(self):
        search_term = re.compile(r'define\(\'|"')
        replacement = ''
        self.text = self.regex(search_term, replacement, self.text)

        search_term = re.compile(r'(\', \')')
        replacement = '="'
        self.text = self.regex(search_term, replacement, self.text)

        search_term = re.compile(r'(\'|")\);')
        replacement = '"'
        self.text = self.regex(search_term, replacement, self.text)

        search_term = re.compile(r'(\'|\"), true\);')
        replacement = '=true'
        self.text = self.regex(search_term, replacement, self.text)

        search_term = re.compile(r'(\'|\"), false\);')
        replacement = '=false'
        self.text = self.regex(search_term, replacement, self.text)

        search_term = re.compile(r'(\'|\"), false\);')
        replacement = '=false'
        self.text = self.regex(search_term, replacement, self.text)

        return self.text

    def php_elements(self):
        search_term = re.compile(r'global ')
        replacement = '# global '
        self.text = self.regex(search_term, replacement, self.text)

        search_term = re.compile(r'._FILE_TO_URL_MAPPING')
        replacement = '\t# $_FILE_TO_URL_MAPPING'
        self.text = self.regex(search_term, replacement, self.text)

        return self.text

    def get_result(self):
        return self.text
