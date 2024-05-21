import re

class Converter:
    @staticmethod
    def conversion1(test_text):
        data = test_text.split(',')
        working = {}
        value = []
        keys = []
        for d in data:
            if 'r' in d:
                a = int(d[:-2])
                if a in keys:
                    working[a].extend(value)
                    value = []
                else:
                    working[a] = value
                    keys.append(a)
                    value = []
            else:
                value.append(int(d))
        return working

    @staticmethod
    def conversion2(input_string):
        pattern = r'(\d+(?:/\d+)*)\s+rs\s+(\d+)'
        matches = re.findall(pattern, input_string)
        result_dict = {}

        for match in matches:
            before_rs = match[0].split('/')
            after_rs = match[1]
            result_dict[after_rs] = before_rs

        return result_dict

    @staticmethod
    def conversion3(input_string):
        list1 = input_string.split(',,')
        dictionary = {}
        keys = []
        for value in list1:
            number = []
            list2 = value.split(',')
            for data in list2:
                if data == 'ru':
                    continue
                if data == list2[-1]:
                    if data in keys:
                        dictionary[data].extend(number)
                    else:
                        dictionary[data] = number
                        keys.append(data)
                else:
                    number.append(data)
                        
        return dictionary

    @staticmethod
    def conversion4(input_string):
        list1 = input_string.split(' ')
        dixtionary = {}
        keys = []

        for data in list1:
            vals = data.split('/')
            if vals[1] in keys:
                dixtionary[vals[1]].append(vals[0])
            else:
                dixtionary[vals[1]] = [vals[0]]
                keys.append(vals[1])
        return dixtionary

    @staticmethod
    def conversion6(input_string):
        list1 = input_string.split(' ')
        working = {}
        keys = []
        for data in list1:
            lis = []
            list2 = data.split('.')
            for val in list2:
                if '₹' in val:
                    key = val[:-1]
                    if key in keys: 
                        working[key].extend(lis)
                        lis = []
                    else:
                        working[key] = lis
                        lis = []
                        keys.append(key)
                else:
                    lis.append(val)

        return working

    @staticmethod
    def conversion7(input_string):
        list1 = input_string.split(' ')
        working = {}
        keys = []
        for data in list1:
            lis = []
            list2 = data.split('.')
            for val in list2:
                if '@' in val:
                    key = val[1:]
                    if key in keys: 
                        working[key].extend(lis)
                        lis = []
                    else:
                        working[key] = lis
                        lis = []
                        keys.append(key)
                else:
                    lis.append(val)

        return working

    @staticmethod
    def conversion8(input_string):
        list1 = input_string.split(' ')
        working = {}
        keys = []
        for data in list1:
            list2 = data.split(',')
            lis = []
            key = list2[1][1:]
            lis.append(list2[0])
            if key in keys:
                working[key].extend(lis)
            else:
                working[key] = lis
                keys.append(key)
        return working    

    @staticmethod
    def conversion9(input_string):
        list1 = input_string.split('_')
        list1 = list1[:-1]
        working = {}
        keys = []
        for data in list1:
            list2 = data.split('/')
            key = list2[1]
            values = list2[0].split('.')
            if key in keys:
                working[key].extend(values)
            else:
                working[key] = values
                keys.append(key)
        return working            

    @staticmethod
    def conversion10(input_string):
        list1 = input_string.split('_')
        list1 = list1[:-1]
        working = {}
        keys = []
        for data in list1:
            list2 = data.split('/')
            key = list2[1][:-2]
            values = list2[0].split('.')
            if key in keys:
                working[key].extend(values)
            else:
                working[key] = values
                keys.append(key)
        return working

    @staticmethod
    def convert(input_string):
        # Check the input string for patterns to determine which conversion function to call
        if re.match(r'\d+(?:/\d+)*\s+rs\s+\d+', input_string):
            return Converter.conversion2(input_string)
        elif '.' in input_string:
            return Converter.conversion3(input_string)
        elif '₹' in input_string:
            return Converter.conversion6(input_string)
        elif '@' in input_string:
            return Converter.conversion7(input_string)
            
        elif '/' in input_string:
            return Converter.conversion4(input_string)
        elif '_' in input_string:
            if '.' in input_string:
                return Converter.conversion9(input_string)
            else:
                return Converter.conversion10(input_string)
        else:
            return "Unsupported input format"
