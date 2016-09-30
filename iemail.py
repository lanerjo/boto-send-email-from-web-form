#!/usr/bin/python2.7
import cgi
import html
import boto.ses
import cgitb; cgitb.enable() #for troubleshooting

#print("Content-Type: text/html")
#print

def getdata():
    form = cgi.FieldStorage()
    name = form["name"].value
    company = form["company"].value
    phone = form["phone"].value
    email = form["email"].value
    category = form["category"].value
    message = form["message"].value
    
    return name, company, phone, email, category, message

#main Program
if __name__=="__main__":
    try:
        name, company, phone, email, category, message = getdata()
        conn = boto.ses.connect_to_region('us-west-2')
        conn.send_email(
            'admin@gmail.com',
            category,
            'Email: %r, Name: %r, Company: %r, Phone: %r Message: %r' % (email, name, company,
                                phone, message),
            to_addresses = 'admin@gmail.com'
            )

    except:
        cgi.print_exception()
     
    print("Location:http://mysite.com/index.html")
    print
    
