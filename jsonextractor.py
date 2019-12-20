import json as jsonParser

def extract(jsonString, path):
    steps = path.split('/')
    try:
        result = jsonParser.loads(jsonString)
        for step in steps:
            if (step.isdigit()):
                step = int(step)
            result = result[step]
    except jsonParser.decoder.JSONDecodeError:
        print('JSON decoding failed. Probably invalid JSON.')
    except TypeError as e:
        print('JSON tree walk failed at key "' + str(step) + '" (Full path: "' + path + '").')
    except (KeyError, IndexError) as e:
        print('Requested key "' + str(step) + '" not found in JSON tree (Full path: "' + path + '").')
    except Exception as e:
        print('Exception thrown at key "' + str(step) + '" (Full path: "' + path + '").')
        print(e)
    else:
        return result