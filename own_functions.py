# def hello():
#     print("hi")
#
#
# hello()
#
# #############################################################
#
#
# def hello_with_parameter(name):
#     print("hello", name)
#
#
# hello_with_parameter("Sohan")
parameters = {'include': 'name'}
#
# properties = ['id', 'key', 'created', 'updated', 'type', 'status', 'priority', 'group']
# properties = properties.append(parameters['include'])
# print(properties)


# parameters = {'include': 'name'}
# properties = ['id', 'key', 'created', 'updated', 'type', 'status', 'priority', 'group', parameters['include']]
# print(properties)

parameters = {'include': ['name', 'tags', 'description']}
properties = ['id', 'key', 'created', 'updated', 'type', 'status', 'priority', 'group']
properties = properties + parameters['include']

print(properties)