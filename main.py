import pandas as pd
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_email(recipient_email, supplier_name, attachment_path):
    """Send email with CSV attachment to supplier"""
    sender_email = "saicaterers.inquires@gmail.com"
    password = "pifz shlq juqs pkhj"
    
    if not sender_email or not password:
        print("Error: Email credentials not found in environment variables")
        return
    
    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"Stock Requirements Report - {datetime.now().strftime('%Y-%m-%d')}"
    
    # Email body
    body = "Hello, today's requirement sheet is as follows:"
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach CSV file
    with open(attachment_path, 'rb') as file:
        part = MIMEApplication(file.read(), Name=os.path.basename(attachment_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        msg.attach(part)
    
    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent to {supplier_name} at {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {supplier_name}: {str(e)}")

def generate_supplier_reports():
    """Generate supplier-specific CSV reports and send emails"""
    today_date = datetime.now().strftime("%Y-%m-%d")
    
    # Create output directory
    os.makedirs('output', exist_ok=True)
    
    # Load supplier data
    suppliers_df = pd.read_excel('your path here\\AutomationCA\\supplier_report_system\\data\\Cosmetic_Suppliers_List.xlsx')
    
    # Load stock buffer data
    stock_df = pd.read_excel('your path here\\AutomationCA\\supplier_report_system\\data\\Cosmetic_Stock_Buffer_Report.xlsx')
    
    # Process each supplier
    for index, row in suppliers_df.iterrows():
        supplier_name = row['Supplier Name']
        supplier_email = row['Email']
        
        # Filter stock items for current supplier
        supplier_items = stock_df[stock_df['Supplier Name'] == supplier_name]
        
        if not supplier_items.empty:
            # Create CSV filename
            filename = f"output/{supplier_name.replace(' ', '_')}_{today_date}.csv"
            
            # Save filtered data - CORRECTED COLUMN NAMES
            supplier_items[['Item Code', 'Item Description',"Stock" ,'Buffer', 'Supplier Name']]\
                .to_csv(filename, index=False)
            
            # Send email with attachment
            send_email(supplier_email, supplier_name, filename)
            print(f"Report generated for {supplier_name}")
        else:
            print(f"No stock items found for {supplier_name}")

if __name__ == "__main__":
    generate_supplier_reports()
