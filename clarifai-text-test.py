from clarifai import rest
from clarifai.rest import ClarifaiApp, Image

CLARIFAI_APP_ID = 'qRE1Uj_OVHIpXK8PwQ9egmECNLotdyjWS6_y6gqz'
CLARIFAI_APP_SECRET = '7QcCSGN1ChCCOobwGU7YWFGnEaQPJHW-V6mCiprE'

app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)

model = app.models.get('f97fb98258e14f15abacffafb7187873')

image = Image(file_obj=open("test2.jpg", 'rb'))

predict_return = model.predict([image])

print predict_return[u'outputs'][0][u'data'][u'concepts'][0][u'id']