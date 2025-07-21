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
    o_path = 'output-1.21.5'

try:
    os.mkdir(abs_path + '/' + o_path + '/')
except FileExistsError: 
    print('directory alreay exists')

try:
    os.mkdir(abs_path + '/' + o_path + '/extra_recipes/')
except FileExistsError: 
    print('directory alreay exists')

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
rei_file = open(abs_path + '/' + o_path + '/favorites.json5', 'w', encoding="utf8")
emi_file = open(abs_path + '/' + o_path + '/emi.json', 'w', encoding="utf8")

rei_json = {
    "favorites": [
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;16383998],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"白色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;6192150],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"绿色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;1481884],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"青色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;3847130],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"淡蓝色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;3949738],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"蓝色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;8991416],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"紫色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;13061821],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"品红色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;15961002],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"粉红色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;10329495],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"淡灰色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;4673362],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"灰色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;1908001],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"黑色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;8606770],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"棕色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;11546150],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"红色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;16351261],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"橙色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;16701501],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"黄色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}",
		"{data:{value:{components:{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;8439583],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"黄绿色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}"
	],
    "hiddenFavorites": [],
    "displays": []
}

emi_json = {
  "favorites": [
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;16383998],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"白色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_1"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;10329495],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"淡灰色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_2"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;4673362],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"灰色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_3"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;1908001],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"黑色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_4"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;8606770],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"棕色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_5"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;11546150],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"红色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_6"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;16351261],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"橙色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_7"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;16701501],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"黄色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_8"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;8439583],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"黄绿色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_9"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;6192150],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"绿色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_10"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;1481884],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"青色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_11"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;3847130],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"淡蓝色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_12"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;3949738],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"蓝色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_13"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;8991416],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"紫色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_14"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;13061821],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"品红色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_15"
    },
    {
      "stack": "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_dye:1b},\"minecraft:custom_model_data\":{floats:[5001.0f]},\"minecraft:damage\":0,\"minecraft:firework_explosion\":{colors:[I;15961002],shape:\"small_ball\"},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"粉红色颜料刷\",\"minecraft:lore\":[{\"color\":\"gray\",\"italic\":false,\"text\":\"能够自由的为所有家具染色！\"},{\"color\":\"gray\",\"extra\":[{\"color\":\"white\",\"italic\":false,\"text\":\" 家具染色台 \"},{\"color\":\"gray\",\"italic\":false,\"text\":\"上使用\"}],\"italic\":false,\"text\":\"右键已放置的家具或在\"}],\"minecraft:max_damage\":125,\"minecraft:max_stack_size\":1}",
      "recipe": "nw:brush_16"
    }
  ],
  "recipe_defaults": {
    "added": [],
    "tags": {},
    "resolutions": {},
    "disabled": []
  },
  "hidden_stacks": []
}

#template
recipe_shaped = {
    "type": "minecraft:crafting_shaped", 
    "category": "building", 
    "show_notification": True, 
    "key": {}, 
    "pattern": [], 
    "result": {"count": 1, "id": "minecraft:firework_star", "components": {"minecraft:item_name": "Template", "minecraft:custom_model_data": {"floats":[10000]}, "minecraft:custom_data": ""}}
}
recipe_shapeless = {
    "type": "minecraft:crafting_shapeless", 
    "category": "building", 
    "show_notification": True, 
    "ingredients": [], 
    "result": {"count": 1, "id": "minecraft:firework_star", "components": {"minecraft:item_name": "Template", "minecraft:custom_model_data": {"floats":[10000]}, "minecraft:custom_data": ""}}
}
recipe_cut = {
    "type": "minecraft:stonecutting",
    "category": "building", 
    "show_notification": True, 
    "ingredient": {},
    "result": {"count": 1, "id": "minecraft:firework_star", "components": {"minecraft:item_name": "Template", "minecraft:custom_model_data": {"floats":[10000]}, "minecraft:custom_data": ""}}
}


#generate command
for row in rows:
    writeline = 'data modify storage nw:fur_data_buildin fur append value {fur_id_buildin: '
    writeline += row[0]
    writeline += ', display_comp: {"minecraft:custom_data": {display_comp: {"minecraft:item_name": [{"text":"'
    item_name = ""
    if row[24] != '':
        item_name += '🛠 '
    item_name += row[1]
    writeline += item_name
    writeline += '"}]'
    writeline += ', "minecraft:custom_model_data": {floats: ['
    writeline += row[2]
    writeline += '.0f]}}'
    if row[27] == '1':
        writeline += ', nw_salvage: 1b'
    if row[9] == '1':
        writeline += ', nw_fur_orient: 1b'
    if row[24] != '':
        writeline += ', nw_fur_transfer_target_buildin: '
        writeline += row[24]
    writeline += ', state_a: {item_id: "minecraft:firework_star", auto_cd: 1, model: {floats: ['
    writeline += row[2]
    writeline += '.0f]}'
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

    emi_append = {}
    if row[27] == '1':
        rei_append = "{data:{value:{components:{\"minecraft:custom_data\":{nw_salvage:1b,nw_fur:1b,nw_fur_id_buildin:" + row[0] + "},\"minecraft:custom_model_data\":{floats:[" + row[2] + ".0f]},\"minecraft:firework_explosion\":{colors:[I;16777215],shape:\"small_ball\"},\"minecraft:consumable\":{consume_seconds:100000.0f,animation:\"none\",sound:{sound_id:\"\"},has_consume_particles:false},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"" + item_name + "\"},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}"
        emi_append['stack'] = "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_salvage:1b,nw_fur:1b,nw_fur_id_buildin:" + row[0] + "},\"minecraft:custom_model_data\":{floats:[" + row[2] + ".0f]},\"minecraft:firework_explosion\":{colors:[I;16777215],shape:\"small_ball\"},\"minecraft:consumable\":{consume_seconds:100000.0f,animation:\"none\",sound:{sound_id:\"\"},has_consume_particles:false},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"" + item_name + "\"}"
    else:
        rei_append = "{data:{value:{components:{\"minecraft:custom_data\":{nw_fur:1b,nw_fur_id_buildin:" + row[0] + "},\"minecraft:custom_model_data\":{floats:[" + row[2] + ".0f]},\"minecraft:firework_explosion\":{colors:[I;16777215],shape:\"small_ball\"},\"minecraft:consumable\":{consume_seconds:100000.0f,animation:\"none\",sound:{sound_id:\"\"},has_consume_particles:false},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"" + item_name + "\"},count:1,id:\"minecraft:firework_star\"},type:\"minecraft:item\"},type:\"roughlyenoughitems:entry_stack\"}"
        emi_append['stack'] = "item:minecraft:firework_star{\"minecraft:custom_data\":{nw_fur:1b,nw_fur_id_buildin:" + row[0] + "},\"minecraft:custom_model_data\":{floats:[" + row[2] + ".0f]},\"minecraft:firework_explosion\":{colors:[I;16777215],shape:\"small_ball\"},\"minecraft:consumable\":{consume_seconds:100000.0f,animation:\"none\",sound:{sound_id:\"\"},has_consume_particles:false},\"minecraft:tooltip_display\":{\"hidden_components\":[\"fireworks\",\"firework_explosion\"]},\"minecraft:item_name\":\"" + item_name + "\"}"

    rei_json['favorites'].append(rei_append)
    if row[10] == '1':
        emi_append['recipe'] = "nw:furniture_" + row[0]
    if row[25] == '1':
        emi_append['recipe'] = "nw:furniture_" + row[0] + "_cut"
    emi_json['favorites'].append(emi_append)

    if row[25] == '1':
        newfilename = '/furniture_' + row[0] + '_cut.json'
        if row[27] == '1':
            recipe_list.write('"nwr:furniture_' + row[0] + '_cut",\n')
            recipefile = open(abs_path + '/' + o_path + '/extra_recipes' + newfilename, 'w')
        else:
            recipe_list.write('"nw:furniture_' + row[0] + '_cut",\n')
            recipefile = open(abs_path + '/' + o_path + newfilename, 'w')
        jsondata = recipe_cut
        jsondata['ingredient'] = row[26]
        jsondata['result']['components']['minecraft:item_name'] = ''
        if row[24] != '':
            jsondata['result']['components']['minecraft:item_name'] = '🛠 '
        jsondata['result']['components']['minecraft:item_name'] += row[1]
        jsondata['result']['components']['minecraft:custom_data'] = "{nw_fur: 1b, nw_fur_id_buildin: " + row[0] + "}"
        if row[27] == '1':
            jsondata['result']['components']['minecraft:custom_data'] = "{nw_fur: 1b, nw_fur_id_buildin: " + row[0] + ", nw_salvage: 1b}"
        jsondata['result']['components']['minecraft:custom_model_data']['floats'][0] = int(row[2])
        jsondata['result']['components']['minecraft:firework_explosion'] = {"shape": "small_ball", "colors": [16777215]}
        jsondata['result']['components']['minecraft:tooltip_display'] = {"hidden_components": ["fireworks", "firework_explosion"]}
        jsondata['result']['components']['minecraft:consumable'] = {"consume_seconds": 100000.0, "animation": "none", "sound": {"sound_id": ""}, "has_consume_particles": False}
        recipefile.write(json.dumps(jsondata,ensure_ascii=False))
        recipefile.close()
        #print("generated", row[0])

    if row[10] == '1':
        newfilename = '/furniture_' + row[0] + '.json'
        if row[27] == '1':
            recipe_list.write('"nwr:furniture_' + row[0] + '",\n')
            recipefile = open(abs_path + '/' + o_path + '/extra_recipes' + newfilename, 'w')
        else:
            recipe_list.write('"nw:furniture_' + row[0] + '",\n')
            recipefile = open(abs_path + '/' + o_path + newfilename, 'w')
        if row[11] == '1':
            jsondata = recipe_shapeless
            jsondata['ingredients'] = []
            if row[15] != '':
                jsondata['ingredients'].append(row[15])
            if row[16] != '':
                jsondata['ingredients'].append(row[16])
            if row[17] != '':
                jsondata['ingredients'].append(row[17])
            if row[18] != '':
                jsondata['ingredients'].append(row[18])
            if row[19] != '':
                jsondata['ingredients'].append(row[19])
            if row[20] != '':
                jsondata['ingredients'].append(row[20])
            if row[21] != '':
                jsondata['ingredients'].append(row[21])
            if row[22] != '':
                jsondata['ingredients'].append(row[22])
            if row[23] != '':
                jsondata['ingredients'].append(row[23])
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
                jsondata['key']['#'] = row[15]
            if row[16] != '':
                jsondata['key']['$'] = row[16]
            if row[17] != '':
                jsondata['key']['%'] = row[17]
            if row[18] != '':
                jsondata['key']['&'] = row[18]
            if row[19] != '':
                jsondata['key']['*'] = row[19]
            if row[20] != '':
                jsondata['key']['@'] = row[20]
            if row[21] != '':
                jsondata['key']['='] = row[21]
            if row[22] != '':
                jsondata['key']['-'] = row[22]
            if row[23] != '':
                jsondata['key']['+'] = row[23]
        jsondata['result']['components']['minecraft:item_name'] = ''
        if row[24] != '':
            jsondata['result']['components']['minecraft:item_name'] = '🛠 '
        jsondata['result']['components']['minecraft:item_name'] += row[1]
        jsondata['result']['components']['minecraft:custom_data'] = "{nw_fur: 1b, nw_fur_id_buildin: " + row[0] + "}"
        if row[27] == '1':
            jsondata['result']['components']['minecraft:custom_data'] = "{nw_fur: 1b, nw_fur_id_buildin: " + row[0] + ", nw_salvage: 1b}"
        jsondata['result']['components']['minecraft:custom_model_data']['floats'][0] = int(row[2])
        jsondata['result']['components']['minecraft:firework_explosion'] = {"shape": "small_ball", "colors": [16777215]}
        jsondata['result']['components']['minecraft:tooltip_display'] = {"hidden_components": ["fireworks", "firework_explosion"]}
        jsondata['result']['components']['minecraft:consumable'] = {"consume_seconds": 100000.0, "animation": "none", "sound": {"sound_id": ""}, "has_consume_particles": False}
        if 'group' in jsondata.keys():
            del jsondata['group']
        if row[3] != '':
            jsondata['group'] = row[3]
        recipefile.write(json.dumps(jsondata, ensure_ascii=False))
        recipefile.close()
        #print("generated", row[0])

propfile.close()
recipe_list.close()

rei_file.write(json.dumps(rei_json, indent=4, ensure_ascii=False))
rei_file.close()

emi_file.write(json.dumps(emi_json, indent=2))
emi_file.close()

print(len(rows), 'files generated at', o_path)