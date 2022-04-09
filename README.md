# Parse_Gmail_Mbox

1. Generate mbox file from your gmail account, using Google Takeout https://takeout.google.com/
    ### [mbox file will have all your mails, in text form - Please dont share your mbox file with anyone]

2. Run `read_generate_data.py` to read mbox and create text file containing 'From' part of every email you have.

3. Run `analyse_data.py` to find the count of each email account your received the mail from. Output will be a `csv` file containing count.

4. Open `counted.csv` file in your spreadsheet software, and you are ready to play with your data.


These keys can be used in mbox object, you can choose as per your requirement
```py
['X-GM-THRID', 'X-Gmail-Labels', 'Delivered-To', 'Received', 'X-Received',
 'ARC-Seal', 'ARC-Message-Signature', 'ARC-Authentication-Results', 
'Return-Path', 'Received', 'Received-SPF', 'Authentication-Results', 
'DKIM-Signature', 'X-Google-DKIM-Signature', 'X-Gm-Message-State', 
'X-Google-Smtp-Source', 'MIME-Version', 'X-Received', 'Date', 'Reply-To',
 'X-Google-Id', 'Precedence', 'List-Unsubscribe', 'Feedback-ID', 'List-Id',
 'X-Notifications', 'X-Notifications-Bounce-Info', 'Message-ID', 'Subject',
 'From', 'To', 'Content-Type']
```

Note: we could have analysed the data by directly reading the file too, but parsing mbox is time consuming process. Better to have results generated in one go, then experiment on further results later.
