import json
from django.utils.html import escape


def sanitize(input_value):
    from lxml import etree
    from lxml.etree import XMLSyntaxError
    input_type = type(input_value)

    if input_type == list:
        clean_value = []
        for item in input_value:
            clean_value.append(sanitize(item))

        return clean_value
    elif input_type == dict:
        return {sanitize(key): sanitize(val) for key, val in list(input_value.items())}
    elif input_type == str or input_type == str:
        try:
            # XML cleaning
            xml_cleaner_parser = etree.XMLParser(remove_blank_text=True)
            xml_data = etree.fromstring(input_value, parser=xml_cleaner_parser)

            input_value = etree.tostring (xml_data).decode('utf-8')
        except XMLSyntaxError as e:
            pass
#             if e is not None and str(e) is not None:
#                 print 'Sanitizing XML (' + input_value + '): ' + str(e)
#             else:
#                 print 'Sanitizing XML (' + input_value + '): '
        finally:
            try:
                json_value = json.loads(input_value)
                sanitized_value = sanitize(json_value)

                clean_value = json.dumps(sanitized_value)
            except ValueError:
                clean_value = escape(input_value)

        return clean_value
    elif input_type == int or input_type == float:
        return input_value
    else:
        # Default sanitizing
        return escape(str(input_value))

