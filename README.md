
# Automated Supplier Portal

An automated system that generates supplier-specific stock requirement reports and sends them via email to cosmetic ingredient suppliers. This system streamlines inventory management by analyzing current stock levels against buffer requirements and automatically distributing personalized reports to each supplier.

## Overview

The Automated Supplier Portal helps cosmetic businesses manage their ingredient inventory by:  
- **Analyzing stock levels** against predefined buffer requirements  
- **Generating supplier-specific reports** containing only relevant items  
- **Automatically sending email reports** with CSV attachments to suppliers  
- **Creating organized output files** with date-stamped filenames  

## Key Features

### Intelligent Stock Analysis
- Compares current stock levels with buffer requirements  
- Identifies items that need restocking from each supplier  
- Filters data to show only relevant items per supplier  

### Automated Email Distribution
- Sends personalized emails to each supplier with their specific requirements  
- Attaches CSV reports containing item codes, descriptions, current stock, and buffer levels  
- Uses Gmail SMTP for reliable email delivery  
- Includes professional email formatting with date-stamped subjects  

### Data Management
- Processes Excel files for supplier information and stock data  
- Generates timestamped CSV files for record keeping  
- Handles multiple suppliers efficiently  

## Data Schema

**Cosmetic_Suppliers_List.xlsx**  
- **Supplier Name**: Company name  
- **Email**: Supplier contact email address  

**Cosmetic_Stock_Buffer_Report.xlsx**  
- **Item Code**: Unique identifier for each ingredient  
- **Item Description**: Full name and grade of the ingredient  
- **Supplier Name**: Associated supplier for the item  
- **Stock**: Current inventory quantity  
- **Buffer**: Minimum stock level threshold  

## How It Works

1. **Data Loading**  
   Reads supplier contact information and current stock data from Excel files.  
2. **Report Generation**  
   For each supplier, filters stock items and creates a CSV report containing:  
   - Item codes and descriptions  
   - Current stock levels  
   - Buffer requirements  
   - Supplier information  
3. **Email Distribution**  
   Automatically sends personalized emails with CSV attachments to each supplier.  
4. **File Management**  
   Saves all generated reports with descriptive, date-stamped filenames.  

## Installation

Clone the repository:
