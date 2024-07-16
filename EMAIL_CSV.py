import os
import csv
from mysql.connector import connect, Error
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def fetch_data_and_write_to_csv():
    connection = None

    DB_USER = os.getenv("username", "admin")
    DB_PASS = os.getenv("password", "admin")

    try:
        connection = connect(
            host="localhost",
            user=DB_USER,
            password=DB_PASS,
            database="online_movie_rating"
        )
        start_ID = "32"
        end_ID = "80"
        query = f"SELECT * FROM movies WHERE ID BETWEEN '{start_ID}' AND '{end_ID}'"

        with connection.cursor() as cursor:
            cursor.execute(query)
            movies = cursor.fetchall()


            with open('/Users/pargatsingh/Cron/Reports/movies_report.csv', 'w', newline='') as csvfile:
                csvwriter = csv.writer(
                    csvfile)  # creates a "csvwriter" object which will be used to write data to the csvfile.
                csvwriter.writerow([i[0] for i in cursor.description])  # Write headers

                '''
                    cursor.description all the columns (
                        ('id', <other metadata>),
                        ('name', <other metadata>),
                        ('year', <other metadata>)
                    )
                    i will pick one column metadata 
                    i[0] will pick the name of the that column name
                    writerow will put that column name into first row in the csvwriter object

                    Within each tuple, i[0] accesses the first element of the tuple, which is the column name.
                    For example, if i is ('id', <other metadata>), then i[0] will be 'id'.

                '''

                csvwriter.writerows(movies)  # Write data rows

    except Error as e:
        with open("/Users/pargatsingh/Cron/Log/log_file.log", "a") as f:
            f.write(f"An error occurred: {e}\n")

    finally:
        if connection:
            connection.close()


def send_email(recipients, subject, body, attachment_path):
    sender = "sandhu.pargat07@gmail.com"
    password = "011259870Pq!"

    msg = MIMEMultipart() #creates a new multipart msg
    msg['From'] = sender #senders address
    msg['To'] = ', '.join(recipients) # receiver adddress
    msg['Subject'] = subject #subject

    msg.attach(MIMEText(body, 'plain')) #creates a plain text MIME object with the email bosy text , and msg.attach attaches the MIME
    #MIME text object to the email message.

    with open(attachment_path, "rb") as attachment:  #opens the attachemnt file in binary read "rb" mode
        part = MIMEBase('application', 'octet-stream') #creates a MIME base object for the attachement
        part.set_payload(attachment.read()) #reads the attachment file and sets it as the payload of the MIME base object
        encoders.encode_base64(part)  #encodes the payload to base64
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}') #adds a header to specify attachemnet
        msg.attach(part) #attaches the MIME base object to the email message

    #SMTP is helping in sending an email from receiver to sender

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server address
    server.starttls() #TLS encryption
    server.login(sender, password) #logs into the SMTP server using the sender's email address
    text = msg.as_string() # converts the multipart msg into string format
    server.sendmail(sender, recipients, text) #sends email
    server.quit() #closes the connection to the SMTP server


# Main execution flow
if __name__ == "__main__":
    fetch_data_and_write_to_csv()

    recipients = ["pargat.singh0522@gmail.com"]
    subject = "Weekly reports"
    body = "Please refer attached file for weekly report"
    attachment_path = "/Users/pargatsingh/Cron/Reports/movies_report.csv"

    #send_email(recipients, subject, body, attachment_path)
