# A tool to generate import data for NyaaWorks
# Run this script with -i <filename.csv> to import csv file

import csv, sys, getopt, json, os

#read args
abs_path = os.path.abspath('.')
f_path = ''
o_path = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"h:i:o:",["help=","ifile=","ofile="])
except getopt.GetoptError:
    print ('Usage: import-data.py -i <f_path> [-o <f_path>]')
    sys.exit()
for opt, arg in opts:
    if opt == '-h':
         print ('Usage: import-data.py -i <f_path> [-o <f_path>]')
         sys.exit()
    elif opt in ("-i", "--ifile"):
         f_path = arg
    elif opt in ("-o", "--ofile"):
         o_path = arg
if f_path == '':
    print ('Usage: import-data.py -i <f_path>')
    sys.exit()
if o_path == '':
    o_path = 'output'

os.mkdir(abs_path + '/' + o_path + '/')
print('Reading from ', f_path)

#read file
rows = []
with open(f_path) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

#init file
propfile = open(abs_path + '/' + o_path + '/init_buildin_data.mcfunction', 'w')
propfile.write('data remove storage nw:fur_data_buildin fur\n')

recipe_list = open(abs_path + '/' + o_path + '/recipe_list.txt', 'w')

#template
recipe_shaped = {"type": "minecraft:crafting_shaped", "category": "building", "show_notification": True, "key": {}, "pattern": [], "result": {"count": 1, "id": "minecraft:firework_star", "components": {"minecraft:item_name": "Template", "minecraft:custom_model_data": 10000, "minecraft:custom_data": ""}}}
recipe_shapeless = {"type": "minecraft:crafting_shapeless", "category": "building", "show_notification": True, "ingredients": [], "result": {"count": 1, "id": "minecraft:firework_star", "components": {"minecraft:item_name": "Template", "minecraft:custom_model_data": 10000, "minecraft:custom_data": ""}}}

#generate command
for row in rows:
    writeline = 'data modify storage nw:fur_data_buildin fur append value {fur_id_buildin: '
    writeline += row[0]
    writeline += ', display_comp: {"minecraft:custom_data": {display_comp: {"minecraft:item_name": \'[{"text":"'
    if row[24] != '':
        writeline += '🛠 '
    writeline += row[1]
    writeline += '"}]\''
    writeline += ', "minecraft:custom_model_data": '
    writeline += row[2]
    writeline += '}'
    if row[9] == '1':
        writeline += ', nw_fur_orient: 1b'
    if row[24] != '':
        writeline += ', nw_fur_transfer_target_buildin: '
        writeline += row[24]
    writeline += ', state_a: {item_id: "minecraft:firework_star", auto_cd: 1, model: '
    writeline += row[2]
    if row[4] == '1':
#        if row[5] == '1':
#            writeline += ', istable: 1'
        if row[6] == '1':
            writeline += ', interaction: [{type: 12}]'
        if row[7] == '1':
            writeline += ', block: "minecraft:barrier"'
        elif row[8] == '1':
            writeline += ', block: "minecraft:light"'
    writeline += '}'
    writeline += ', nw_fur_id_buildin: '
    writeline += row[0]
    writeline += '}}}\n'
    propfile.write(writeline)
    if row[10] == '1':
        newfilename = '/furniture_' + row[0] + '.json'
        recipe_list.write('"nw:furniture_' + row[0] + '",\n')
        recipefile = open(abs_path + '/' + o_path + newfilename, 'w')
        if row[11] == '1':
            jsondata = recipe_shapeless
            jsondata['ingredients'] = []
            if row[15] != '':
                if row[15][0] == '#':
                    row[15] = row[15].lstrip('#')
                    jsondata['ingredients'].append({"tag": "Template"})
                    jsondata['ingredients'][-1]['tag'] = row[15]
                else:
                    jsondata['ingredients'].append({"item": "Template"})
                    jsondata['ingredients'][-1]['item'] = row[15]
            if row[16] != '':
                if row[16][0] == '#':
                    row[16] = row[16].lstrip('#')
                    jsondata['ingredients'].append({"tag": "Template"})
                    jsondata['ingredients'][-1]['tag'] = row[16]
                else:
                    jsondata['ingredients'].append({"item": "Template"})
                    jsondata['ingredients'][-1]['item'] = row[16]
            if row[17] != '':
                if row[17][0] == '#':
                    row[17] = row[17].lstrip('#')
                    jsondata['ingredients'].append({"tag": "Template"})
                    jsondata['ingredients'][-1]['tag'] = row[17]
                else:
                    jsondata['ingredients'].append({"item": "Template"})
                    jsondata['ingredients'][-1]['item'] = row[17]
            if row[18] != '':
                if row[18][0] == '#':
                    row[18] = row[18].lstrip('#')
                    jsondata['ingredients'].append({"tag": "Template"})
                    jsondata['ingredients'][-1]['tag'] = row[18]
                else:
                    jsondata['ingredients'].append({"item": "Template"})
                    jsondata['ingredients'][-1]['item'] = row[18]
            if row[19] != '':
                if row[19][0] == '#':
                    row[19] = row[19].lstrip('#')
                    jsondata['ingredients'].append({"tag": "Template"})
                    jsondata['ingredients'][-1]['tag'] = row[19]
                else:
                    jsondata['ingredients'].append({"item": "Template"})
                    jsondata['ingredients'][-1]['item'] = row[19]
            if row[20] != '':
                if row[20][0] == '#':
                    row[20] = row[20].lstrip('#')
                    jsondata['ingredients'].append({"tag": "Template"})
                    jsondata['ingredients'][-1]['tag'] = row[20]
                else:
                    jsondata['ingredients'].append({"item": "Template"})
                    jsondata['ingredients'][-1]['item'] = row[20]
            if row[21] != '':
                if row[21][0] == '#':
                    row[21] = row[21].lstrip('#')
                    jsondata['ingredients'].append({"tag": "Template"})
                    jsondata['ingredients'][-1]['tag'] = row[21]
                else:
                    jsondata['ingredients'].append({"item": "Template"})
                    jsondata['ingredients'][-1]['item'] = row[21]
            if row[22] != '':
                if row[22][0] == '#':
                    row[22] = row[22].lstrip('#')
                    jsondata['ingredients'].append({"tag": "Template"})
                    jsondata['ingredients'][-1]['tag'] = row[22]
                else:
                    jsondata['ingredients'].append({"item": "Template"})
                    jsondata['ingredients'][-1]['item'] = row[22]
            if row[23] != '':
                if row[23][0] == '#':
                    row[23] = row[23].lstrip('#')
                    jsondata['ingredients'].append({"tag": "Template"})
                    jsondata['ingredients'][-1]['tag'] = row[23]
                else:
                    jsondata['ingredients'].append({"item": "Template"})
                    jsondata['ingredients'][-1]['item'] = row[23]
        else:
            jsondata = recipe_shaped
            jsondata['pattern'] = []
            if row[12] != '':
                if len(row[12]) == 1:
                    row[12] += '  '
                if len(row[12]) == 2:
                    row[12] += ' '
                jsondata['pattern'].append(row[12])
            if row[13] != '':
                if len(row[13]) == 1:
                    row[13] += '  '
                if len(row[13]) == 2:
                    row[13] += ' '
                jsondata['pattern'].append(row[13])
            if row[14] != '':
                if len(row[14]) == 1:
                    row[14] += '  '
                if len(row[14]) == 2:
                    row[14] += ' '
                jsondata['pattern'].append(row[14])
            jsondata['key'] = {}
            if row[15] != '':
                if row[15][0] == '#':
                    row[15] = row[15].lstrip('#')
                    jsondata['key']['#'] = {"tag": "Template"}
                    jsondata['key']['#']['tag'] = row[15]
                else:
                    jsondata['key']['#'] = {"item": "Template"}
                    jsondata['key']['#']['item'] = row[15]
            if row[16] != '':
                if row[16][0] == '#':
                    row[16] = row[16].lstrip('#')
                    jsondata['key']['$'] = {"tag": "Template"}
                    jsondata['key']['$']['tag'] = row[16]
                else:
                    jsondata['key']['$'] = {"item": "Template"}
                    jsondata['key']['$']['item'] = row[16]
            if row[17] != '':
                if row[17][0] == '#':
                    row[17] = row[17].lstrip('#')
                    jsondata['key']['%'] = {"tag": "Template"}
                    jsondata['key']['%']['tag'] = row[17]
                else:
                    jsondata['key']['%'] = {"item": "Template"}
                    jsondata['key']['%']['item'] = row[17]
            if row[18] != '':
                if row[18][0] == '#':
                    row[18] = row[18].lstrip('#')
                    jsondata['key']['&'] = {"tag": "Template"}
                    jsondata['key']['&']['tag'] = row[18]
                else:
                    jsondata['key']['&'] = {"item": "Template"}
                    jsondata['key']['&']['item'] = row[18]
            if row[19] != '':
                if row[19][0] == '#':
                    row[19] = row[19].lstrip('#')
                    jsondata['key']['*'] = {"tag": "Template"}
                    jsondata['key']['*']['tag'] = row[19]
                else:
                    jsondata['key']['*'] = {"item": "Template"}
                    jsondata['key']['*']['item'] = row[19]
            if row[20] != '':
                if row[20][0] == '#':
                    row[20] = row[20].lstrip('#')
                    jsondata['key']['@'] = {"tag": "Template"}
                    jsondata['key']['@']['tag'] = row[20]
                else:
                    jsondata['key']['@'] = {"item": "Template"}
                    jsondata['key']['@']['item'] = row[20]
            if row[21] != '':
                if row[21][0] == '#':
                    row[21] = row[21].lstrip('#')
                    jsondata['key']['='] = {"tag": "Template"}
                    jsondata['key']['=']['tag'] = row[21]
                else:
                    jsondata['key']['='] = {"item": "Template"}
                    jsondata['key']['=']['item'] = row[21]
            if row[22] != '':
                if row[22][0] == '#':
                    row[22] = row[22].lstrip('#')
                    jsondata['key']['-'] = {"tag": "Template"}
                    jsondata['key']['-']['tag'] = row[22]
                else:
                    jsondata['key']['-'] = {"item": "Template"}
                    jsondata['key']['-']['item'] = row[22]
            if row[23] != '':
                if row[23][0] == '#':
                    row[23] = row[23].lstrip('#')
                    jsondata['key']['+'] = {"tag": "Template"}
                    jsondata['key']['+']['tag'] = row[23]
                else:
                    jsondata['key']['+'] = {"item": "Template"}
                    jsondata['key']['+']['item'] = row[23]
        jsondata['result']['components']['minecraft:item_name'] = '"'
        if row[24] != '':
            jsondata['result']['components']['minecraft:item_name'] = '"🛠 '
        jsondata['result']['components']['minecraft:item_name'] += row[1] + '"'
        jsondata['result']['components']['minecraft:custom_data'] = "{nw_fur: 1b, nw_fur_id_buildin: " + row[0] + "}"
        jsondata['result']['components']['minecraft:custom_model_data'] = int(row[2])
        jsondata['result']['components']['minecraft:firework_explosion'] = {"shape": "small_ball", "colors": [16777215]}
        jsondata['result']['components']['minecraft:hide_additional_tooltip'] = {}
        jsondata['result']['components']['minecraft:food'] = {"saturation": 0.0, "nutrition": 0, "can_always_eat": True, "eat_seconds": 1000000.0}
        if row[3] != '':
            jsondata['group'] = row[3]
        recipefile.write(json.dumps(jsondata))
        recipefile.close()
        #print("generated", row[0])

propfile.close()
recipe_list.close()

print(len(rows), 'files generated at', o_path)