from django.shortcuts import render

def scrape_emails(request): 
    return render(request, "scrape_emails.html")