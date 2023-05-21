import re


def find_all_emails(text):
    result = re.findall(r"\S\S+@\w+\.\w\w+", text)
    return result


print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org \
                      first_last@iana.org \
                first.middle.last@iana.or a@test.com abc111@test.com.net'))

['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org',
    'first.middle.last@iana.or', 'abc111@test.com']
['Ima.Fool@iana.org', '1Fool@iana.org', 'first_last@iana.org',
 'first.middle.last@iana.or', 'abc111@test.com']
