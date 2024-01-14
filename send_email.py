import streamlit as st
from st_pages import hide_pages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email():
    try:
        # Set your email and password
        sender_email = st.secrets["sender_email"]
        sender_password = st.secrets["sender_password"]

        # Set the recipient's email address
        recipient_email = st.session_state["email"]

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Cc"] = sender_email
        message["Subject"] = "willowrevamp-service-request"

        # Add body text to the email
        body = '''
    Personal Details
        
    First Name : %s
    Last Name : %s
    Email : %s
    Whatsapp No: %s 
    Address : %s
        
    --------------------------------------------------
        
    Order Details
        
    %s
    
    ''' % (st.session_state["first_name"], st.session_state["last_name"], st.session_state["email"],
           st.session_state["mobile"], st.session_state["address"], st.session_state["df"])
        message.attach(MIMEText(body, "plain"))

        for key in st.session_state.keys():
            if "_uploaded_images" in key:
                user_uploaded_images = st.session_state[key]
                for uploaded_file in user_uploaded_images:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(uploaded_file.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename= {key.replace('_uploaded_images', '') + '_' + uploaded_file.name}")
                    message.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email + "," + sender_email, message.as_string())

        st.success('Thank you & you will be contacted shortly', icon="✅")
        st.balloons()
        hide_pages(['Message'])
        st.session_state.clear()
    except Exception as e:
        st.error('Could not place order, please close the browser tab and reinitiate the service request')
