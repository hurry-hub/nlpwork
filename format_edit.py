def txt2json():
    filename_1 = "w2v.txt"
    filename_2 = "w2v_json.txt"

    key_list = []
    value_list = []

    with open(filename_1, 'r', encoding="utf-8") as file_1:
        for line in file_1:
            line1 = line.strip()
            str1 = line1.replace(' ', ',')

            index_list = []
            str_cat = ''

            for item in str1[2:]:
                if item == ',':
                    index_list.append(float(str_cat))
                    str_cat = ''
                else:
                    str_cat = str_cat + item
            index_list.append(float(str_cat))
            str1 = str1.replace('\u200b', '')
            str1 = str1.replace('"', '')
            str1 = str1.replace("'", '')
            str1 = str1.replace('\xad', '')
            key_list.append(str1[0])
            value_list.append(index_list)

    with open(filename_2, 'w', encoding="utf-8") as file_2:
        mydict = {}
        for i in range(len(key_list)):
            mydict[key_list[i]] = value_list[i]

        str_mydict = str(mydict)
        str_mydict_re = str_mydict.replace('\'', '"')
        file_2.write(str_mydict_re)