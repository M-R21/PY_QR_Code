# here we will be generating 1-5 QRcodes with 1-5 different messages 
import qrcode



#this generator will get a number from 0 to 4 and creat a qr codes each with on digiti till reaching 5  
def qr_generator (number) : 
    while number != 5 :
        #this will creat a qr code caled the input +=1 till it reaches 5
        generate_model = qrcode.make("QR {} is generated automatically".format(number))
        #the qrcode is saved with a same name as the number on the message
        generate_model.save("QR_code_nr{}.png".format(number))
    
       
        number+=1














 
qr_generator(int(input("please enter the number of QR codes you would like to recieve: ")))