#!/usr/bin/python3

import csv
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.facebook # use the facebook database (automatically created if it doesn't exist)
posts = db.posts
reactions = db.reactions
comments = db.comments


if __name__ == '__main__':
    all_posts = list(posts.find({}))
    all_comments = list(comments.find({}))
    #all_reactions = list(reactions.find({}))
    
    
    with open('posts.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['_id', 'message', 'name', 'description', 'shares', 'link', 'created_time'])
        for p in all_posts:
            # [0] = _id, [1] = message, [2] = name, [3] = description, [4] = shares, [5] = link, [6] = created_time
            row = ['', '', '', '', '', '', '']
            if '_id' in p: row[0] = p['_id']
            if 'message' in p: row[1] = p['message']
            if 'name' in p: row[2] = p['name']
            if 'description' in p: row[3] = p['description']
            if 'shares' in p: row[4] = p['shares']
            if 'link' in p: row[5] = p['link']
            if 'created_time' in p: row[6] = p['created_time']
            csvwriter.writerow(row)

    with open('comments.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['_id', 'message', 'like_count', 'created_time'])
        for p in all_comments:
            # [0] = _id, [1] = message, [2] = like_count, [3] = created_time
            row = ['', '', '', '']
            if '_id' in p: row[0] = p['_id']
            if 'message' in p: row[1] = p['message']
            if 'like_count' in p: row[2] = p['like_count']
            if 'created_time' in p: row[3] = p['created_time']
            csvwriter.writerow(row)
