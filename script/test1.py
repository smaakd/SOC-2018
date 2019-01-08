import threading

import cognitive_face as CF
import glob
import datetime
from camapp.models import Person,TableAttendance,Fraud
from datetime import timezone
from django.utils import timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



def run_test1():
    KEY = '332c42de6f6b4b399f55c0aee49c371e'  # Replace with a valid Subscription Key here.
    CF.Key.set(KEY)

    BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)
    group_id = "22"
    unrecognized=0
    recognized=0
    Face_id_list_final = []
    output_final=[]
    t1 = threading.currentThread()
    for image in glob.glob("/home/saketh/soc/script/test/*.jpg"):


        p1 = TableAttendance.objects.all()
        if p1:
            print("aaaaaaaaaaaaaaaaaaaaaa")
            for people in p1:
                print("ffffffffffffffffffffffff")
                timediff = timezone.now() - people.date_time
                if timediff.seconds > 30:
                    personid = people.personId
                    check = Fraud.objects.filter(personId=personid, t1=people.ts)
                    print("INNNNNNNNAAAAAAAAAAAAAA")
                    if check:
                        for c in check:
                            c.t2 = datetime.datetime.now().time()
                            c.date = datetime.datetime.now().date()
                            c.date_time = datetime.datetime.now()
                            c.save()
                    else:
                        print("INNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
                        push_in_table2 = Fraud.objects.create()
                        push_in_table2.name = people.name
                        push_in_table2.personId = people.personId
                        push_in_table2.t1 = people.ts
                        push_in_table2.t2 = datetime.datetime.now().time()
                        push_in_table2.date = datetime.datetime.now().date()
                        push_in_table2.date_time = datetime.datetime.now()
                        push_in_table2.save()
                        people_in_person = Person.objects.filter(id = people.personId)
                        for pinp in people_in_person:
                            if (pinp.flag == 0):


                                emaild = pinp.emailId
                                name=pinp.name
                                msg = MIMEMultipart()
                                msg['From'] = "noreply.rollcam@gmail.com"
                                msg['To'] = emaild
                                password = "strive2win"
                                msg['Subject'] = "Attendance Alert"
                                body = "Hi "+ "<b>" + name +"</b>,"+ " <br><br>" + "It is to inform you that your Attendance has not been recorded for about an hour. Kindly mark your attendance as soon as possible."+"<br><br>"+ "If you find any discrepancy with regards to the above displayed message, please contact your Administrator"
                                msg.attach(MIMEText(body, 'html'))
                                print(msg)
                                server = smtplib.SMTP("smtp.gmail.com", 587)
                                server.starttls()
                                server.login(msg['From'], password)
                                server.sendmail(msg['From'], msg['To'], msg.as_string())
                                server.quit()


                                pinp.flag = 1
                                pinp.Fraud_number = pinp.Fraud_number + 1
                                pinp.Present_number = pinp.Present_number - 1
                                pinp.save()





        Face_id_list = []
        face_id = CF.face.detect(image)
        for eachface in face_id:
            Face_id_list.append(eachface['faceId'])
            Face_id_list_final.append(eachface)
        if Face_id_list:
            output = CF.face.identify(Face_id_list, person_group_id=group_id, threshold=0.6)
            output_final.append(output)
            for eachoutput in output:

                if (not eachoutput['candidates']):
                    unrecognized = unrecognized + 1
                    continue
                else:
                    p_id = eachoutput['candidates'][0]['personId']

                    '''
                    curname=""
                    with open(os.path.dirname(os.path.realpath(__file__))+'/details.json') as json_data:
                        d = json.load(json_data)
                        for it in d:
                            if it['personId'] == person_id:
                                curname = it['name']

                    flag=0
                    for n in name:
                        if(n==curname):
                            flag=1
                            break
                    if(flag==0):
                        name.append(curname)
                        '''
                    p = Person.objects.filter(person_id=p_id)
                    for man in p:
                        if man.person_present_status == False:

                            push_in_table = TableAttendance.objects.create()
                            push_in_table.name = man.name
                            push_in_table.personId = man.id
                            push_in_table.date = datetime.datetime.now().date()
                            push_in_table.time1 = datetime.datetime.now().time()
                            push_in_table.ts = datetime.datetime.now().time()
                            push_in_table.date_time = datetime.datetime.now()
                            push_in_table.save()

                            emaild = man.emailId
                            name = man.name
                            msg = MIMEMultipart()
                            msg['From'] = "noreply.rollcam@gmail.com"
                            msg['To'] = emaild
                            password = "strive2win"
                            msg['Subject'] = "Attendance Confirmation"
                            body = "Hi " + "<b>" + name + "</b>," + " <br><br>" + "This is to inform you that your today's Attendance has been recorded at "+str(datetime.datetime.now().time()) + " .<br><br>" + "If you find any discrepancy with regards to the above displayed message, please contact your Administrator"
                            msg.attach(MIMEText(body, 'html'))
                            print(msg)
                            server = smtplib.SMTP("smtp.gmail.com", 587)
                            server.starttls()
                            server.login(msg['From'], password)
                            server.sendmail(msg['From'], msg['To'], msg.as_string())
                            server.quit()



                            man.person_present_status = True
                            man.Present_number = man.Present_number + 1
                            man.save()
                            recognized = recognized + 1
                        else:
                            change_in_table = TableAttendance.objects.filter(personId=man.id)
                            for marked in change_in_table:
                                marked.ts = datetime.datetime.now().time()
                                marked.date_time = datetime.datetime.now()
                                marked.save()
    print ("recognized =",recognized)
    print ("unrecognized =",unrecognized)

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    run_test1()
