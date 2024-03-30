import pickle

class MessageStructure:
    #Класс для упаковки данных в сообщении для сокетов (коды, картинки, сообщения)

    @staticmethod
    def SaveToBytes(parameter):
        result = pickle.dumps(parameter, pickle.HIGHEST_PROTOCOL)
        return result

    @staticmethod
    def RestoreFromBytes(parameterAsBytes):
        result = pickle.loads(parameterAsBytes)
        return result
