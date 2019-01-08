import cognitive_face as CF
KEY = '332c42de6f6b4b399f55c0aee49c371e'                               # Replace with a valid Subscription Key here
CF.Key.set(KEY)
BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
group_id = "22"

    # p=Person.objects.filter(id = pk)
    # for person1 in p:
    #     x = CF.person.create(group_id, person1.name)
    #     CF.person.add_face(person1.Image_1, group_id, x['personId'])
    #     CF.person.add_face(person1.Image_2, group_id, x['personId'])
    #     CF.person.add_face(person1.Image_3, group_id, x['personId'])
    #     CF.person.add_face(person1.Image_4, group_id, x['personId'])
    #     CF.person.add_face(person1.Image_5, group_id, x['personId'])'''

# p=Person.objects.filter(id = 3)
# for person1 in p:
#     print (person1.name)
#
x=CF.person.lists(group_id,0,100)
print(x)