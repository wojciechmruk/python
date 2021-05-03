from src.SSConverter import SSConverter
from src.SSShakiriser import SSShakiriser

text = open("_ss_environment.php", "r")
converter = SSConverter(text.read())
text.close()

shakiriser = SSShakiriser(converter.get_result())

f = open(".env", "w")
f.write(shakiriser.shakiriser)
f.close()

print('File .env has been created. Please check if everything is fine.')
