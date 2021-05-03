class SSShakiriser:
    def __init__(self, text):
        self.text = text
        self.text_comment = ''

    # Make it beautiful like Shakira
    @property
    def shakiriser(self):
        text_array = []
        for line in self.text.splitlines():
            if line.strip() != '' and not line.startswith('#'):
                text_array.append(line)
        text_array.sort()

        text = ''
        for row in text_array:


            map_file = open("src/map.txt", "r")
            for line in map_file.readlines():
                x = line.split(',')
                text += self.check_pattern(row, x[0], x[1])

            map_file.close()
            text += row + '\n'

        info = open("src/info.txt", "r")
        self.text = info.read() + text
        info.close()

        return self.text

    def check_pattern(self, row, pattern, comment=""):

        if row.startswith(pattern) and comment not in self.text_comment:
            self.text_comment = comment
            return '\n# ' + comment + '\n'
        return '';
