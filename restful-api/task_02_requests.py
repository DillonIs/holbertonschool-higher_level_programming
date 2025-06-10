#!/usr/bin/python3
"""Fetches all posts from an API placeholder"""
import requests
import csv
"""task_02_requests using the requests library Python"""

def fetch_and_print_posts():
    """Fetches and prints from JSONPlaceholder"""
    try:
        res = requests.get("https://jsonplaceholder.typicode.com/posts")
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return

    print("Status Code: {}".format(res.status_code))

    if res.headers.get("Content-Type") == "application/json; charset=utf-8":
        json_data = res.json()
        for post in json_data:
            print(post["title"])

def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder and saves as csv file"""
    try:
        res = requests.get("https://jsonplaceholder.typicode.com/posts")
    except:
        print("Failed to retrieve data")
        return
    json_data = res.json()
    csvfile = "posts.csv"
    data_filtered = [{key: post[key] for key in ('id', 'title', 'body')} for post in json_data]
    headers = ['id', 'title', 'body']

    with open(csvfile, "w", newline="") as file:
        csv_write = csv.DictWriter(file, fieldnames=headers)
        csv_write.writeheader()
        csv_write.writerows(data_filtered)
