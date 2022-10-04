from loko_extensions.model.components import Component, Input, Output, save_extensions, Select, Arg, Dynamic, MKVField, \
    MultiKeyValue, AsyncSelect

#########################   DOCS     ###########################

prescriptor_description = '''
### Description

This component allows to **make** optimized prescription, providing customized constraints and the desired ....?

### Input

.....


### Output

.....

 
'''


#########################   ARGS     ###########################

args_list = []

mkvfields = [MKVField(name='cond1', label='Cond1111', required=True),
             MKVField(name='cond2', label='cond2'),
             MKVField(name='cond3', label='Cond3'), ]

multikeyvalue = MultiKeyValue(name='CONSTRAINTS', label='CONSTRAINTS', fields=mkvfields,
                              group='Advanced Args')

task = AsyncSelect(name='task', label='Task', url='http://localhost:9999/routes/loko_prescriptor/saro')

args_list.append(multikeyvalue)
args_list.append(task)

#########################   INPUT   ###########################

create_model_service = "NOSERVICE"
save_ranges_service = "NOSERVICE"
input_list = [Input(id="create_model", label="Create Model", to="create_model", service= create_model_service),
              Input(id="save_ranges", label="Save Ranges", to="save_ranges", service=save_ranges_service)
              ]


#########################   OUTPUT   ###########################

output_list = [Output(id="create_model", label="create_model"),
               Output(id="save_ranges", label="save_ranges")
               ]

#########################   COMPONENT   ###########################

prescriptor = Component(name="prescriptor", description=prescriptor_description, inputs=input_list,
               outputs=output_list, args=args_list, configured=False)




save_extensions([prescriptor], path="../extensions")
