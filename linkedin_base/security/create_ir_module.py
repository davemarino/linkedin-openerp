# encoding: utf-8
# ==============  INIZIO CONFIGURAZIONI ==============
# read write create unlink per admin
# read per user
base_models = [
    'model_linkedin_configuration',
    'model_linkedin_position',
    'model_linkedin_backlog'
]

base_groups = [
    ("base.group_erp_manager", 1, 1, 1, 1),
    ("base.group_user", 1, 0, 0, 0),
]

# ==============  FINE CONFIGURAZIONI ==============
import os
import csv

headers = ["id","name","model_id:id","group_id:id",
           "perm_read","perm_write","perm_create","perm_unlink"]


def get_permissions(groups, models):
   rows=[]
   for group in groups:
       for model in models:
           row = {
               "id": "%s_%s" % (model.replace('model_', '').replace('.', '_'), group[0]),
               "name": "%s %s" % (model.replace('model_', '').replace('.', '_'), group[0]),
               "model_id:id": "%s" % model,
               "group_id:id": group[0],
               "perm_read": group[1],
               "perm_write": group[2],
               "perm_create": group[3],
               "perm_unlink": group[4],
           }
           rows.append(row)
   return rows


base_dir = os.path.dirname(__file__) or '.'
_filename = '%s/ir.model.access.csv' % base_dir
writer = csv.DictWriter(open(_filename, 'w'),
                                fieldnames=headers, 
                                delimiter=',', quotechar='"',
                                quoting = csv.QUOTE_NONNUMERIC)

first_row = {}
for i in headers:
    first_row[i] = i
writer.writerow(first_row)

for row in get_permissions(base_groups, base_models):
    writer.writerow(row)
