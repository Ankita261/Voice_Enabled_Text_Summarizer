import smtplib 

def sendMail(message):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("search.summarizer@gmail.com", PASSWORD ) 
        s.sendmail("search.summarizer@gmail.com", RECEIVER , message) 
        s.quit()
        return "Mail Sent Successfully"
    except:
        return "Some Problem Occurred"

data = """ 

Growing up in Calcutta, I came to realize that the people of the region were just like its weather: warm all year long. The people of the region are called Bengalis, as the State is known as West Bengal. The regional Bengali language has its roots in Sanskrit, but is known for it's rounded "o" sounds. The distinctive sweetness and melodic tones of the Bengali language make even an admonition sound like a love song. """

print(sendMail(data))
