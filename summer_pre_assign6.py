import _mysql
import sys
import MySQLdb
import sys
from bs4 import BeautifulSoup
import click
import openpyxl
import os.path
import urllib.request
from openpyxl import Workbook
from openpyxl import load_workbook

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

@click.command()
@click.argument("acronym",nargs=1)
@click.pass_context
def sender(ctx,acronym):



    db = MySQLdb.connect("localhost", "root", "mysql","summer_pre_assign5_schema")
    cursor = db.cursor()

    q="SELECT studentname,college,total from marks where college=%s"
    cursor.execute(q,(acronym,))
    answer1=cursor.fetchall()

    q = "SELECT college,COUNT(*),MIN(total),MAX(total),AVG(total) FROM marks GROUP BY college"
    cursor.execute(q)
    answer2 = cursor.fetchall()

    q = "SELECT marks.studentname,marks.college,marks.total,current.emailid from marks,current WHERE marks.studentname=current.dbnames"
    cursor.execute(q)
    answer3 = cursor.fetchall()


    msg=""
    msg = '<head><style>body{background-color:blue;} p{color:yellow; align : center; font-style: italic;font-size: 30px;font-weight: bold;} th{color:blue;}</style></head> <body style="background-color:powderblue;"><p style="color:red;"><b> list of students and their marks</b></p>'
    msg += '<table><tr><th>Student Name</th><th>college</th><th> total marks</th> </tr>'


    for i in answer1:
        msg+='<tr><td>' + i[0] + '</td><td>' + str(i[1]) + '</td><td>' + str(i[2]) + '</td></tr>'
    msg += '</table>'
    msg += f'<p>Summary of the {acronym}college</p>'

    msg += '<table><tr><th>college </th><th>count</th><th>Minimum Marks </th><th> Maximum Marks </th><th> Average Marks</th></tr>'


    for i in answer2:
        msg += '<tr><td>' + str(i[0]) + '</td><td>' + str(i[1]) + '</td><td>' + str(i[2]) + '</td><td>' + str(i[3]) + '</td><td>' + str(i[4]) + '</td></tr>'

    msg += '</table>'

    msg += '<p style="color:green;"><b>GLOBAL SUMMARY OF WHOLE CLASS</b></p>'

    msg += '<table><tr><th>Student name </th><th> college</th><th> total </th><th> email id </th></tr>'


    for i in answer3:
        msg += '<tr><td>' + str(i[0]) + '</td><td>' + str(i[1]) + '</td><td>' + str(i[2]) + '</td><td>' + str(i[3]) + '</td><td>'

    msg += '</table>'
    msg += '</body></html>'

    print(msg)

    gmailaddress = input("what is your gmail address? \n ")
    gmailpassword = input("what is the password for that email address? \n  ")
    mailto = input("what email address do you want to send your message to? \n ")
    #msg = input("What is your message? \n ")




    try:
        client = None
        message = MIMEMultipart('alternative')
        message['from'] = gmailaddress
        message['to'] = mailto
        message['subject'] = f'college report of colllege {acronym}'
        part1 = MIMEText(msg, 'html')
        message.attach(part1)
        client = smtplib.SMTP("smtp.gmail.com", 587)
        client.ehlo()
        client.starttls()
        client.login(gmailaddress, gmailpassword)
        msg = message.as_string()
        client.sendmail(gmailaddress, mailto, msg)
        print("successfully mail sent")
    except smtplib.SMTPAuthenticationError:
        print("authentication failed try again  :)")
        return ;
    except smtplib.SMTPDataError:
        print("The SMTP server refused to accept the message data. :)")
        return ;
    except smtplib.SMTPConnectError:
        print("Error occurred during establishment of a connection with the server")
        return ;
    except smtplib.SMTPNotSupportedError:
        print("The command or option attempted is not supported by the server.:)")
        return ;
    except smtplib.SMTPException:
        print("smtp exception")
        return ;
    except smtplib.SMTPServerDisconnected:
        print("smtp server disconnected exception")
        return ;














if __name__=='__main__':
    sender(obj={})